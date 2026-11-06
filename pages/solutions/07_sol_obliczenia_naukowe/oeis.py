"""Wyrazy ciągu silni dla n od 1 do 9."""

from math import factorial
from pathlib import Path

values = [factorial(n) for n in range(1, 10)]
result = "sequence=" + ", ".join(map(str, values)) + "\n"
(Path(__file__).resolve().parent / "oeis_results.txt").write_text(result, encoding="utf-8")
print(result, end="")
