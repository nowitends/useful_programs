# Rozwiązania do 06_www.md

Ten folder zawiera pliki potrzebne do wykonania siedmiu zadań z [06_www.md](../06_www.md).

| Zadanie | Pliki | Stan |
| --- | --- | --- |
| 1. Prosta strona HTML | `01_sol_html/index.html` | Gotowa do otwarcia lokalnie |
| 2. HTML, CSS i obraz | `02_sol_html/index.html`, `style.css`, `images/rzut.png` | Gotowa do otwarcia lokalnie |
| 3. Symulacja rzutu | `03_sol_html/index.html` | Gotowa do otwarcia lokalnie |
| 4. Publikacja symulacji | `03_sol_html/index.html`, `04_sol_html/LINK.md` | Wymaga osobnego repozytorium `rzut` i publikacji |
| 5. Strona edukacyjna | `projekty/edukacja/index.html`, `05_sol_html/LINK.md` | Kod gotowy, wymaga publikacji |
| 6. Quiz | `projekty/quiz/index.html`, `06_sol_html/LINK.md` | Kod gotowy, wymaga publikacji |
| 7. Dane z API | `projekty/pogoda/index.html`, `07_sol_html/LINK.md` | Kod gotowy, wymaga publikacji; potrzebny internet |

## Jak użyć plików

1. Otwórz pliki `index.html` z zadań 1–3 w przeglądarce. Nie wymagają instalowania bibliotek.
2. Dla zadania 4 utwórz osobne publiczne repozytorium `rzut`, skopiuj do niego `03_sol_html/index.html`, włącz GitHub Pages i wpisz oba prawdziwe adresy w `04_sol_html/LINK.md`.
3. Dla zadań 5–7 utwórz osobne publiczne repozytoria `edukacja`, `quiz` i `pogoda`. Do każdego skopiuj odpowiedni plik z `projekty/` jako główny `index.html`. Po publikacji uzupełnij odpowiedni `LINK.md`.
4. `LINK.md` zawierają pola do uzupełnienia. Nie wpisano fikcyjnych adresów, ponieważ strony nie zostały opublikowane.

Strona pogodowa korzysta z [Open-Meteo](https://open-meteo.com/en/docs) i [API wyszukiwania miejscowości](https://open-meteo.com/en/docs/geocoding-api). Pobiera prognozę na żywo bez klucza API. Przy braku połączenia pokazuje komunikat o błędzie.
