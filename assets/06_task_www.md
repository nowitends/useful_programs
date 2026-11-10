## Zadania: www

Ważne rozróżnienie:

**Zadania 1–3:** wykonujesz lokalne strony HTML i zapisujesz je w odpowiednich folderach **swojego forka repozytorium przedmiotu**. Nie publikujesz ich jeszcze przez GitHub Pages.

**Zadania 4–7:** publikujesz projekty w internecie w swoich osobistych repozytoriach (muszą być publiczne). W odpowiednim folderze **forka repozytorium przedmiotu** umieszczasz tylko informacje o swoich repozytoriach i opublikowanych stronach (w plikach `LINK_4.md`, `LINK_5.md`, `LINK_6.md`, `LINK_7.md` podając adres **działającej strony** oraz **repozytorium projektu**).

W forku repozytorium przedmiotu zachowaj przygotowaną strukturę katalogów:

```text
01_sol/
└── index.html
02_sol/
├── index.html
├── style.css
└── images/
    └── obraz.png
03_sol/
└── index.html
04_sol/
└── LINK_4.md
05_sol/
└── LINK_5.md
06_sol/
└── LINK_6.md
07_sol/
└── LINK_7.md
```

Szablon pliku `LINK_N.md`:

```markdown
# Publikacja strony N (np. 4, 5, 6, 7)

## Strona

https://NAZWA-UZYTKOWNIKA.github.io/nazwa-repozytorium/ (np. rzut, edukacja, quiz)

## Repozytorium

https://github.com/NAZWA-UZYTKOWNIKA/nazwa-repozytorium/ (np. rzut, edukacja, quiz)
```

---

### Zadanie 1. Prosta strona HTML

Utwórz `01_sol/index.html`. Strona ma zawierać nagłówek, co najmniej dwa akapity, listę, tabelę i link do innej strony. Zadbaj o poprawną strukturę HTML, tytuł dokumentu i UTF-8. **Nie używaj CSS ani JavaScript.**

### Zadanie 2. HTML + CSS + obrazy

Przygotuj w folderze `02_sol/` nową wersję strony z zadania 1. Dodaj oddzielny `style.css`, jakiś niewielki obrazek w formacie PNG lub JPG w podfolderze `images/` oraz użyj go w treści strony.

### Zadanie 3. Interaktywna strona I — rzut ukośny

Z pomocą AI stwórz jedną interaktywną stronę HTML (z przyciskami i suwakami) dotyczącą **rzutu ukośnego**. Mają być **co najmniej trzy suwaki**, przyciski sterujące oraz reagujący na zmiany parametrów wykres, animację lub symulację. Dodaj wyświetlanie wektorów prędkości i przyspieszenia. Preferowany jest **jeden samodzielny plik**, który powinien znajdować się w `03_sol/index.html`.

Uwaga: czasem zamiast pliku do pobrania AI podaje kod HTML jako tekst. Wklej go wtedy do pliku `.txt` i zmień rozszerzenie na `.html`. Jeśli AI otworzy działający podgląd strony, zapisz jej kod do pliku.

### Zadanie 4. Publikacja przez GitHub Pages

Utwórz na swoim koncie **nowe publiczne repozytorium** o nazwie `rzut`. Umieść w nim stronę HTML z **zadania 3** i opublikuj ją przez GitHub Pages. W pliku `04_sol/LINK_4.md` na forku przedmiotu podaj link do działającej strony oraz do nowego repozytorium.

### Zadanie 5. Profesjonalna strona edukacyjna z AI

Utwórz na swoim koncie **nowe publiczne repozytorium** o nazwie `edukacja`. Wykorzystaj najbardziej zaawansowane narzędzia AI, jakie masz, do stworzenia **nowoczesnej, estetycznej i rozbudowanej strony edukacyjnej** o wybranym zagadnieniu z **matematyki, fizyki lub algorytmiki**. Oczekiwane są: atrakcyjna sekcja powitalna, spójna stylistyka, animacja w banerze strony, inne animacje, interaktywne wykresy lub symulacje, suwaki oraz wygodna i dynamiczna nawigacja. Strona powinna poprawnie działać również na telefonie. Opublikuj stronę i wpisz jej **adres** oraz **adres repozytorium** do `05_sol/LINK_5.md`.

### Zadanie 6. Interaktywny quiz

Utwórz na swoim koncie **nowe publiczne repozytorium** o nazwie `quiz`. Przygotuj stronę z **co najmniej 10 pytaniami** dotyczącymi wybranego zagadnienia. Dodaj różne typy pytań, automatyczne sprawdzanie, wynik, wyjaśnienia odpowiedzi i możliwość rozpoczęcia testu od nowa. Opublikuj projekt i dodaj linki do `06_sol/LINK_6.md`.

### Zadanie 7. Strona wykorzystująca publiczne API

API to interfejs umożliwiający pobieranie danych z zewnętrznych źródeł w sposób ustandaryzowany. Akronim pochodzi od angielskiego terminu **Application Programming Interface**. Jest to sposób komunikacji między różnymi aplikacjami, który pozwala na korzystanie z funkcji lub danych udostępnionych przez inne systemy.

Stwórz stronę pobierającą **rzeczywiste dane** (np. pogodowe, astronomiczne lub statystyczne, itd.) z publicznego API (np. OpenWeatherMap, NASA lub GUS). Zaprezentuj je na wykresie lub w tabeli, dodaj interaktywne filtry i obsłuż błędy pobierania danych. Korzystaj z API dostępnego z przeglądarki, bez ujawniania tajnych kluczy. Opublikuj stronę i dodaj linki do `07_sol/LINK_7.md`.
