# Rozwiązania zadań WWW

Pliki odpowiadają zadaniom z [06_task_www.md](../06_task_www.md).

| Zadanie | Rozwiązanie | Stan |
| --- | --- | --- |
| 1. Sam HTML | [01_sol/index.html](01_sol/index.html) | Gotowe lokalnie |
| 2. HTML, CSS i obraz | [02_sol/index.html](02_sol/index.html), [style.css](02_sol/style.css), [obraz.png](02_sol/images/obraz.png) | Gotowe lokalnie |
| 3. Rzut ukośny | [03_sol/index.html](03_sol/index.html) | Gotowe lokalnie |
| 4. Publikacja rzutu | [kod strony](do_publikacji/rzut/index.html), [LINK_4.md](04_sol/LINK_4.md) | Kod gotowy; publikacja oczekuje |
| 5. Strona edukacyjna | [kod strony](do_publikacji/edukacja/index.html), [LINK_5.md](05_sol/LINK_5.md) | Kod gotowy; publikacja oczekuje |
| 6. Quiz | [kod strony](do_publikacji/quiz/index.html), [LINK_6.md](06_sol/LINK_6.md) | Kod gotowy; publikacja oczekuje |
| 7. Dane z API | [kod strony](do_publikacji/pogoda/index.html), [LINK_7.md](07_sol/LINK_7.md) | Kod gotowy; publikacja oczekuje |

Zgodnie z treścią zadań foldery `04_sol`–`07_sol` zawierają tylko pliki na adresy publikacji. Kody stron do osobnych repozytoriów są w `do_publikacji/`. Dla zadania 4 użyto tej samej strony, co w zadaniu 3.

Do dokończenia publikacji trzeba utworzyć publiczne repozytoria `rzut`, `edukacja`, `quiz` i `pogoda`, umieścić w każdym odpowiedni `index.html` w katalogu głównym, włączyć GitHub Pages dla gałęzi `main` i dopiero po sprawdzeniu działania strony wpisać prawdziwe adresy do `LINK_4.md`–`LINK_7.md`. Obecne pliki z linkami nie udają opublikowanych stron.

Strona pogodowa pobiera prognozę z [Open-Meteo](https://open-meteo.com/en/docs) oraz lokalizacje z [Geocoding API](https://open-meteo.com/en/docs/geocoding-api). Do jej działania potrzebny jest internet; nie używa klucza API.

## Sprawdzenie

Strony zostały sprawdzone lokalnie w Chrome, także przy szerokości telefonu. Test `python tests/smoke.py` sprawdza suwaki, animacje, wynik i reset quizu, filtry pogody oraz obsługę błędu API. W teście prognoza jest podstawiona, aby wynik był powtarzalny. Osobno sprawdzono pobieranie rzeczywistych danych Open-Meteo w przeglądarce. Do ponownego uruchomienia testu potrzebne są Python, Playwright i Chrome.
