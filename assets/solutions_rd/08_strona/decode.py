#!/usr/bin/env python3
"""Dekoder raportów LaTeX Drill Lab V4 (18 zadań), także starszych V3/V2.

Przykłady:
    python teacher/decode.py raport.txt --details
    python teacher/decode.py raporty/ --csv wyniki.csv --json-dir odczytane/

Base64 + Caesar +1 jest jedynie obfuskacją, bez uwierzytelnienia danych.
"""
from __future__ import annotations

import argparse
import base64
import binascii
import csv
import json
import re
import sys
from pathlib import Path

SPECS = {
    2: {"header": "LATEX-DRILL/20/V2", "total": 20},
    3: {"header": "LATEX-DRILL/20/V3", "total": 20},
    4: {"header": "LATEX-DRILL/18/V4", "total": 18},
}


def shift_back_one(ch: str) -> str:
    """Odwróć przesunięcie A-Z, a-z oraz 0-9 o jedną pozycję."""
    if "A" <= ch <= "Z":
        return chr((ord(ch) - ord("A") - 1) % 26 + ord("A"))
    if "a" <= ch <= "z":
        return chr((ord(ch) - ord("a") - 1) % 26 + ord("a"))
    if "0" <= ch <= "9":
        return chr((ord(ch) - ord("0") - 1) % 10 + ord("0"))
    return ch


def decode_text(raw: str) -> dict:
    lines = raw.lstrip("\ufeff").splitlines()
    version = next((v for v, spec in SPECS.items() if lines and lines[0].strip() == spec["header"]), None)
    if version is None:
        raise ValueError("Nieobsługiwany nagłówek. Dostępne formaty: V2, V3, V4")
    try:
        start = lines.index("BEGIN-DATA") + 1
        end = lines.index("END-DATA", start)
    except ValueError as e:
        raise ValueError("Brak znaczników BEGIN-DATA / END-DATA") from e
    payload = "".join(line.strip() for line in lines[start:end])
    if not payload or not re.fullmatch(r"[A-Za-z0-9+/=]+", payload):
        raise ValueError("Niepoprawny ciąg danych")
    b64 = "".join(shift_back_one(ch) for ch in payload)
    try:
        report = json.loads(base64.b64decode(b64, validate=True).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError, binascii.Error) as e:
        raise ValueError("Nie można odczytać zawartości Base64/JSON — plik może być uszkodzony") from e
    validate_report(report, expected_version=version)
    return report


def validate_report(report: dict, expected_version: int | None = None) -> None:
    if not isinstance(report, dict) or report.get("format") != "LATEX_DRILL_REPORT":
        raise ValueError("Niewłaściwy format raportu")
    version = report.get("version")
    if version not in SPECS or (expected_version is not None and version != expected_version):
        raise ValueError("Niespójna wersja raportu")
    total = SPECS[version]["total"]
    tasks = report.get("exercises")
    if not isinstance(tasks, list) or len(tasks) != total:
        raise ValueError(f"Raport V{version} powinien zawierać {total} zadań")
    student = report.get("student")
    if not isinstance(student, dict):
        raise ValueError("Brak danych uczestnika")
    if version == 4 and (not isinstance(student.get("initials"), str) or
                         not re.fullmatch(r"[A-ZĄĆĘŁŃÓŚŹŻ]{2,6}", student["initials"])):
        raise ValueError("Nieprawidłowe inicjały uczestnika")
    seen = set()
    for num, task in enumerate(tasks, 1):
        if not isinstance(task, dict) or type(task.get("number")) is not int or task["number"] != num:
            raise ValueError(f"Nieprawidłowy numer zadania {num}")
        task_id = task.get("id")
        if not isinstance(task_id, str) or not task_id or task_id in seen:
            raise ValueError(f"Zduplikowane lub błędne ID zadania {num}")
        seen.add(task_id)
        status = task.get("status")
        if status not in {"correct", "skipped"}:
            raise ValueError(f"Zadanie {num} nie zostało zakończone")
        history = task.get("history")
        if not isinstance(history, list) or len(history) > 5 or (status == "correct" and not history):
            raise ValueError(f"Nieprawidłowa liczba prób w zadaniu {num}")
        if type(task.get("attempts")) is not int or task["attempts"] != len(history):
            raise ValueError(f"Niespójna liczba prób w zadaniu {num}")
        if any(not isinstance(h, dict) or not isinstance(h.get("value"), str)
               or type(h.get("correct")) is not bool for h in history):
            raise ValueError(f"Nieprawidłowa historia odpowiedzi w zadaniu {num}")
        if version == 4 and task.get("finalAnswer") != (history[-1]["value"] if history else ""):
            raise ValueError(f"Niespójna ostatnia odpowiedź w zadaniu {num}")
        if status == "correct":
            if not history[-1]["correct"] or any(h["correct"] for h in history[:-1]):
                raise ValueError(f"Niespójny zapis poprawnej odpowiedzi w zadaniu {num}")
            if version >= 3 and task.get("skipReason") is not None:
                raise ValueError(f"Błędny powód pominięcia w zaliczonym zadaniu {num}")
        else:
            if any(h["correct"] for h in history):
                raise ValueError(f"Pominięte zadanie {num} zawiera poprawną odpowiedź")
            if version == 2:
                if len(history) != 5:
                    raise ValueError(f"V2: pominięte zadanie {num} musi mieć 5 prób")
            else:
                reason = task.get("skipReason")
                if reason == "limit" and len(history) != 5:
                    raise ValueError(f"V{version}: limit w zadaniu {num} wymaga 5 prób")
                if reason == "empty" and len(history) >= 5:
                    raise ValueError(f"V{version}: pominięcie pustej odpowiedzi wymaga 0–4 prób")
                if reason not in {"empty", "limit"}:
                    raise ValueError(f"V{version}: nieprawidłowy powód pominięcia zadania {num}")
    summary = report.get("summary")
    if not isinstance(summary, dict):
        raise ValueError("Brak podsumowania")
    correct = sum(t["status"] == "correct" for t in tasks)
    skipped = sum(t["status"] == "skipped" for t in tasks)
    attempts = sum(t["attempts"] for t in tasks)
    if (summary.get("total") != total or summary.get("correct") != correct or
        summary.get("skipped") != skipped or summary.get("attempts") != attempts):
        raise ValueError("Podsumowanie nie zgadza się z odpowiedziami")
    if version >= 3:
        empty = sum(t.get("skipReason") == "empty" for t in tasks)
        limit = sum(t.get("skipReason") == "limit" for t in tasks)
        if summary.get("skippedEmpty") != empty or summary.get("skippedLimit") != limit or empty + limit != skipped:
            raise ValueError("Niespójny podział pominiętych zadań")


def reason(task: dict, version: int) -> str:
    if task["status"] == "correct":
        return "OK"
    if version == 2 or task.get("skipReason") == "limit":
        return "LIMIT"
    return "PUSTE"


def brief_row(path: Path, report: dict) -> dict:
    user, summary = report["student"], report["summary"]
    initials = user.get("initials", "")
    row = {
        "plik": str(path), "inicjaly": initials,
        "identyfikator": initials or user.get("github", ""),
        "liczba_zadan": summary["total"], "poprawne": summary["correct"],
        "pominiete": summary["skipped"], "pominiete_puste": summary.get("skippedEmpty", 0),
        "pominiete_limit": summary.get("skippedLimit", summary["skipped"]),
        "proby": summary["attempts"], "id_sesji": report.get("sessionId", ""),
        "start": report.get("startedAt", ""), "koniec": report.get("finishedAt", ""),
        "wersja": report["version"], "blad": "",
    }
    for i, task in enumerate(report["exercises"], 1):
        row[f"Q{i:02d}"] = f"{reason(task, report['version'])} ({task['attempts']}/5)"
    return row


def display_report(path: Path, report: dict, details: bool) -> None:
    user, summary = report["student"], report["summary"]
    version = report["version"]
    participant = (f"Inicjały: {user['initials']}" if version == 4 else
                   f"Login (stary format): {user.get('github', '---')}")
    print(f"\nPLIK: {path.name} (V{version})")
    print(f"  {participant}")
    print(f"  Wynik: {summary['correct']}/{summary['total']} | pominięto: {summary['skipped']} | prób razem: {summary['attempts']}")
    if version >= 3:
        print(f"  Pominięte: puste pole: {summary['skippedEmpty']}, limit 5 prób: {summary['skippedLimit']}")
    print(f"  Sesja: {report.get('sessionId', '-')}")
    if details:
        print("  Zadania:")
        for task in report["exercises"]:
            status = reason(task, version)
            print(f"   {task['number']:02d}. [{status:5}] {task['title']} ({task['attempts']}/5)")
            for i, answer in enumerate(task["history"], 1):
                print(f"        {i}. {'✓' if answer['correct'] else '×'}  {answer['value']!r}")
            if not task["history"] and status == "PUSTE":
                print("        (pominięto bez wpisania odpowiedzi)")


def files_in(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(p for p in path.rglob("*.txt") if p.is_file())
    raise FileNotFoundError(path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Dekodowanie raportów LaTeX Drill Lab V4/V3/V2 offline")
    parser.add_argument("input", type=Path, help="Plik TXT lub folder raportów")
    parser.add_argument("--details", action="store_true", help="Pokaż wszystkie wpisane odpowiedzi")
    parser.add_argument("--csv", type=Path, help="Wyeksportuj zbiorczą tabelę CSV")
    parser.add_argument("--json-dir", type=Path, help="Wyeksportuj rozkodowane JSON")
    args = parser.parse_args()
    try:
        files = files_in(args.input)
    except FileNotFoundError:
        print(f"Nie znaleziono: {args.input}", file=sys.stderr)
        return 2
    if not files:
        print("Brak plików TXT", file=sys.stderr)
        return 2
    rows = []
    failures = 0
    for file in files:
        try:
            report = decode_text(file.read_text(encoding="utf-8-sig"))
            display_report(file, report, args.details)
            rows.append(brief_row(file, report))
            if args.json_dir:
                args.json_dir.mkdir(parents=True, exist_ok=True)
                (args.json_dir / (file.stem + ".json")).write_text(
                    json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        except (OSError, ValueError, KeyError, TypeError) as e:
            failures += 1
            print(f"BŁĄD w {file}: {e}", file=sys.stderr)
            rows.append({"plik": str(file), "blad": str(e)})
    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        max_questions = max((r.get("liczba_zadan", 18) for r in rows), default=18)
        keys = ["plik", "inicjaly", "identyfikator", "liczba_zadan", "poprawne",
                "pominiete", "pominiete_puste", "pominiete_limit", "proby", "id_sesji",
                "start", "koniec", "wersja", "blad"] + [f"Q{i:02d}" for i in range(1, max_questions + 1)]
        with args.csv.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=keys, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nZapisano CSV: {args.csv}")
    print("\nUwaga: raporty są zakodowane, ale nie są podpisane kryptograficznie.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
