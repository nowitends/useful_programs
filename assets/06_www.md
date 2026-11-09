# WWW — interaktywne materiały i publikacja w sieci

W tym bloku przejdziemy od **prostego pliku HTML** do **interaktywnej strony edukacyjnej opublikowanej w internecie**. Będziemy korzystać z HTML, CSS, JavaScript, GitHuba, GitHub Pages, MkDocs (tylko dla zaawansowanych) oraz narzędzi AI.

Nie jest to kurs profesjonalnego programowania frontendu. Celem jest zrozumienie podstaw, umiejętność współpracy z AI przy tworzeniu stron oraz samodzielne sprawdzanie, poprawianie i publikowanie gotowych rezultatów.

| Narzędzie | Do czego służy? |
| --- | --- |
| **HTML** | Struktura i zawartość strony: tekst, nagłówki, linki, obrazy, tabele |
| **CSS** | Wygląd strony: kolory, czcionki, odstępy, rozmieszczenie elementów |
| **JavaScript** | Interakcja: przyciski, suwaki, obliczenia, animacje, pobieranie danych |
| **GitHub** | Przechowywanie kodu, historia zmian i współpraca |
| **GitHub Pages** | Publikowanie statycznych stron pod publicznym adresem |
| **MkDocs** | Zamiana zestawu plików Markdown w serwis dokumentacyjny |
| **AI i agenci programistyczni** | Pomoc w projektowaniu, pisaniu, analizie i poprawianiu kodu |

---

## 1. Od pliku HTML do strony WWW

### Co otwiera przeglądarka?

Przeglądarka potrafi odczytać plik HTML i wyświetlić jego zawartość. HTML opisuje przede wszystkim **strukturę dokumentu**, a nie jego wygląd.

Utwórz plik `index.html` z następującą zawartością:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Moja pierwsza strona</title>
</head>
<body>
    <h1>Moja pierwsza strona</h1>
    <p>To jest przykładowy akapit.</p>
    <p>Odwiedź <a href="https://www.wikipedia.org/">Wikipedię</a>.</p>
</body>
</html>
```

Zapisz plik w kodowaniu UTF-8, a następnie otwórz go w przeglądarce. **Nie potrzebujesz jeszcze serwera ani GitHub Pages.** Przeglądarka otworzy dokument lokalnie, zwykle pod adresem zaczynającym się od `file:///`.

Gdy opublikujesz te same pliki na serwerze WWW, strona będzie dostępna przez adres zaczynający się od `https://`.

### Najważniejsze elementy HTML

| Znacznik | Znaczenie |
| --- | --- |
| `<h1>`–`<h6>` | Nagłówki kolejnych poziomów |
| `<p>` | Akapit tekstu |
| `<strong>`, `<em>` | Wyróżnienie i zaakcentowanie tekstu |
| `<ul>`, `<ol>`, `<li>` | Lista punktowana, numerowana i jej element |
| `<a href="...">` | Odnośnik do innej strony lub pliku |
| `<img src="..." alt="...">` | Obraz z opisem alternatywnym |
| `<table>`, `<tr>`, `<th>`, `<td>` | Tabela, wiersz, nagłówek kolumny i komórka |
| `<button>`, `<input>` | Elementy interfejsu użytkownika |
| `<section>`, `<div>` | Grupowanie elementów strony |

## Elementy HTML

Większość elementów HTML ma znacznik otwierający i zamykający.

### Akapit

~~~html
<p>To jest akapit.</p>
~~~

Tutaj:

- `<p>` — otwiera akapit,
- `</p>` — zamyka akapit,
- tekst pomiędzy nimi jest zawartością.

---

### Nagłówki

~~~html
<h1>Tytuł strony</h1>
<h2>Wyniki</h2>
<h3>Eksperyment 1</h3>
~~~

Efekt odpowiada mniej więcej hierarchii:

# Tytuł strony

## Wyniki

### Eksperyment 1

W HTML dostępne są poziomy od `h1` do `h6`.

Przykład listy oraz tabeli:

```html
<h2>Narzędzia</h2>
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>

<table>
    <tr><th>x</th><th>x²</th></tr>
    <tr><td>1</td><td>1</td></tr>
    <tr><td>2</td><td>4</td></tr>
    <tr><td>3</td><td>9</td></tr>
</table>
```

### Obrazy lokalne i z internetu

Obraz znajdujący się w podfolderze `images` można wyświetlić tak:

```html
<img src="images/wykres.png" alt="Wykres zależności y od x">
```

Obraz z Wikimedia Commons można również wyświetlić bezpośrednio z jego **adresu pliku graficznego** (np. z domeny `upload.wikimedia.org`), bez pobierania go do repozytorium. Upewnij się, że podajesz adres obrazu, a nie adres strony z opisem obrazu. Podaj źródło i przestrzegaj jego licencji.

**Ważne:** ścieżka `images/wykres.png` jest względna względem położenia pliku HTML. W nazwach plików wielkość liter ma znaczenie, szczególnie po publikacji na GitHub Pages.

---

## 2. CSS — wygląd strony

HTML określa *co* znajduje się na stronie, a CSS — *jak* ma to wyglądać. W drugim zadaniu użyjemy **oddzielnego pliku CSS**.

Przykładowa struktura:

```text
moja-strona/
├── index.html
├── style.css
└── images/
    └── wykres.png
```

W sekcji `<head>` pliku `index.html` umieść odwołanie do arkusza stylów:

```html
<link rel="stylesheet" href="style.css">
```

Przykładowa zawartość `style.css`:

```css
body {
    max-width: 900px;
    margin: 40px auto;
    padding: 0 20px;
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #e91e83;
    background: #f6f8fc;
}

h1 {
    color: #167fe0;
    border-bottom: 2px solid #175b99;
}

img {
    max-width: 100%;
    height: auto;
}
```

Zmieniaj kolory, odstępy i szerokość strony, aby zobaczyć, jak jeden plik CSS wpływa na wygląd całego dokumentu.

---

## 3. JavaScript — interakcja i wizualizacja

JavaScript pozwala reagować na działania użytkownika, wykonywać obliczenia i aktualizować elementy strony bez jej ponownego wczytywania.

Poniższy przykład wyświetla aktualną wartość suwaka.

```html
<label for="parametr">Parametr a: <output id="wartosc">2</output></label>
<input id="parametr" type="range" min="0" max="10" step="0.5" value="2">

<script>
    const suwak = document.getElementById("parametr");
    const wynik = document.getElementById("wartosc");

    suwak.addEventListener("input", () => {
        wynik.textContent = suwak.value;
    });
</script>
```

Pełna strona:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Interaktywny suwak</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<label for="parametr">Parametr a: <output id="wartosc">2</output></label>
<input id="parametr" type="range" min="0" max="10" step="0.5" value="2">

<script>
    const suwak = document.getElementById("parametr");
    const wynik = document.getElementById("wartosc");

    suwak.addEventListener("input", () => {
        wynik.textContent = suwak.value;
    });
</script>

</body>
</html>
```

Zobacz przykład: [java_index.html](examples/java_index.html).

### Statyczna strona a interaktywność

„Statyczna” oznacza, że serwer udostępnia gotowe pliki, np. `index.html`, `style.css` i `script.js`. JavaScript działa następnie w przeglądarce użytkownika i może obsługiwać animacje, quizy, symulacje, a nawet pobierać aktualne dane z zewnętrznego API.

Usługa GitHub Pages, z której skorzystamy do publikacji strony, **nie uruchamia po stronie serwera** aplikacji napisanych w Pythonie, PHP ani systemów wymagających własnej bazy danych i backendu.

Dynamiczne strony wymagają zazwyczaj backendu, który generuje treść w odpowiedzi na żądania użytkownika. Dostępne darmowe rozwiązania to np. serwery w chmurze, platformy typu Heroku czy Vercel, które umożliwiają uruchamianie aplikacji z backendem.

---

## 4. AI jako narzędzie do tworzenia stron

Nie musisz pisać wszystkiego od zera. Możesz poprosić AI o przygotowanie kodu, zaproponowanie układu strony, dodanie animacji czy naprawienie błędów. **Za ostateczne działanie strony odpowiadasz jednak Ty.**

Dobry sposób pracy:

1. Określ temat, odbiorcę i konkretne funkcje strony.
2. Podaj ograniczenia techniczne, np. „jeden plik `index.html`, bez serwera, do publikacji na GitHub Pages”.
3. Uruchom lokalnie wygenerowaną stronę i sprawdź wszystkie elementy interaktywne.
4. Zgłoś AI konkretne błędy i poprawiaj projekt iteracyjnie.
5. Sprawdź wynik po **publikacji**, a nie tylko w podglądzie narzędzia AI.

**Przykładowe polecenie:**

> Stwórz pojedynczy plik `index.html` przedstawiający interaktywną symulację rzutu ukośnego. Dodaj suwaki prędkości początkowej, kąta i przyspieszenia grawitacyjnego, animację toru, wykres oraz przyciski Start, Pauza i Reset. Wszystkie sterowania muszą działać. Strona ma otwierać się lokalnie i nadawać do publikacji na GitHub Pages.

Nie umieszczaj w publicznym kodzie haseł, prywatnych danych ani tajnych kluczy API. Jeśli korzystasz z bibliotek, obrazów lub materiałów zewnętrznych, podaj ich źródła i sprawdź warunki wykorzystania.

### Przykłady stron ode mnie

* Juliusz Cezar: [https://remigiuszdurka.github.io/waipages/Cezar.html](https://remigiuszdurka.github.io/waipages/Cezar.html) (pierwsza moja AI strona)
  
* Aleksander Wielki: [https://remigiuszdurka.github.io/waipages/Aleksander.html](https://remigiuszdurka.github.io/waipages/Aleksander.html)

* Stożek świetlny: [https://remigiuszdurka.github.io/waipages/stozek.html](https://remigiuszdurka.github.io/waipages/stozek.html)

* Podróż w czasie: [https://remigiuszdurka.github.io/waipages/novikov.html](https://remigiuszdurka.github.io/waipages/novikov.html)

* LaTeX — ćwiczenia: [https://remigiuszdurka.github.io/latex_drill/](https://remigiuszdurka.github.io/latex_drill/)

* Prompting: [https://prompt-engineering-a59a57.gitlab.io/](https://prompt-engineering-a59a57.gitlab.io/) (GitLab zamiast GitHuba)
  
* Warsztaty "n-body": [https://remigiuszdurka.github.io/fizykatomniefascynuje/fizyka-Alicja/Alicja-n-body(e=0,01).html](https://remigiuszdurka.github.io/fizykatomniefascynuje/fizyka-Alicja/Alicja-n-body(e=0,01).html)

* Warsztaty "fala": [https://remigiuszdurka.github.io/fizykatomniefascynuje/fizyka-Antonina/Fala1.html](https://remigiuszdurka.github.io/fizykatomniefascynuje/fizyka-Antonina/Fala1.html)

* Slider: [https://remigiuszdurka.github.io/waipages/slider.html](https://remigiuszdurka.github.io/waipages/slider.html)

* Markdown jako strona: [https://remigiuszdurka.github.io/waipages/markdown_example.md](https://remigiuszdurka.github.io/waipages/markdown_example.md) — przeglądarka wyświetla plik Markdown jako tekst.

---

## 5. GitHub Pages — publikacja strony internetowej

GitHub Pages umożliwia publikację gotowych plików strony z repozytorium GitHub.

Kiedy tworzysz nowe repozytorium na GitHub, otrzymuje ono adres w postaci:

```text
https://github.com/NAZWA-UZYTKOWNIKA/nazwa-repozytorium/
```

**Po opublikowaniu strony** typowy adres strony projektu wygląda następująco:

```text
https://NAZWA-UZYTKOWNIKA.github.io/nazwa-repozytorium/
```

### Dwie rzeczy, których nie należy mylić przy robieniu zadań

- **Fork repozytorium przedmiotu** — miejsce, w którym oddajesz zadania i pliki wskazane przez prowadzącego.
- **Nowe repozytorium projektu** — osobne publiczne repozytorium na Twoim koncie, z którego publikujesz swoją stronę WWW. W zadaniach stworzysz serię nowych repozytoriów dla kolejnych projektów, które skończą się publikacją jako pełnoprawne strony WWW. Następnie w forkowanym kursowym repozytorium będziesz oddawać pliki oraz wskazywać link do opublikowanej strony.

### Najprostsza publikacja krok po kroku

1. Utwórz nowe **publiczne** (!) repozytorium z nazwą opisującą projekt, np. `motion`.
2. Dodaj plik `index.html` (wygenerowany wcześniej lub utworzony ręcznie). Dla najprostszego projektu `index.html` umieść w katalogu głównym.
3. W nowym repozytorium otwórz **Settings → Pages**.
4. W sekcji **Build and deployment** wybierz **Deploy from a branch**, gałąź `main` i folder `/(root)`, a następnie zapisz ustawienia, klikając przycisk **Save**.
5. Tworzenie strony chwilę trwa. Postęp publikacji możesz śledzić w zakładce **Actions** repozytorium.
6. Po około minucie otwórz **Settings → Pages**, odczytaj adres strony i sprawdź, czy działa.
7. Warto dodać do repozytorium plik `README.md` z linkiem do opublikowanej strony. Link przyda Ci się też do oddania zadania.

**Uwaga na ścieżki:** w stronach projektów GitHub Pages odwołania typu `images/wykres.png` lub `./style.css` są zwykle bezpieczniejsze od odwołań zaczynających się od `/`, które wskazują katalog główny domeny, a nie katalog projektu. Poruszanie się po strukturze katalogów projektu za pomocą względnych ścieżek przećwiczymy później przy okazji Basha. Na razie skorzystaj z AI, aby uporządkować pliki i sprawdzić ścieżki do zasobów.

Dokumentacja: [GitHub Pages](https://docs.github.com/en/pages) · [Konfiguracja źródła publikacji](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

---

## 6. Markdown → MkDocs → strona WWW

### Zagadnienie tylko dla zaawansowanych użytkowników

Markdown dobrze nadaje się do pisania treści, ale nie zapewnia samodzielnie całego serwisu z menu, motywem i wyszukiwarką. **MkDocs** tworzy z plików `.md` gotową, statyczną stronę dokumentacyjną.

Jako przykład podam stronę wykładową powstałą z serii plików Markdown, przekształconą następnie w statyczną stronę WWW za pomocą MkDocs.

- link do repozytorium: [https://github.com/RemigiuszDurka/port_issp](https://github.com/RemigiuszDurka/port_issp)

- link do opublikowanej strony MkDocs: [https://remigiuszdurka.github.io/port_issp/](https://remigiuszdurka.github.io/port_issp/)

Idea polega na tym, że podstawowe treści projektu zapisujesz w plikach Markdown, a następnie za pomocą MkDocs generujesz z nich kompletną stronę WWW z menu, motywem i wyszukiwarką. Jest to wygodne rozwiązanie, gdy chcesz szybko przekształcić **dokumentację** w atrakcyjną wizualnie stronę internetową.

```text
Pliki Markdown → MkDocs → HTML/CSS/JavaScript → GitHub Pages
```

### Struktura projektu

```text
moje-materialy/
├── mkdocs.yml
└── docs/
    ├── index.md
    ├── wyniki.md
    └── assets/
        └── wykres.png
```

Przykładowy plik `mkdocs.yml` (z motywem **Material for MkDocs**):

```yaml
site_name: Moje materiały edukacyjne
theme:
  name: material
  language: pl
nav:
  - Start: index.md
  - Wyniki: wyniki.md
```

Przykład pliku `docs/index.md`:

```markdown
# Moje materiały

Witamy na stronie projektu.

- [Przejdź do wyników](wyniki.md)
```

Przykład fragmentu `docs/wyniki.md`:

```markdown
# Wyniki

Poniżej przedstawiono wykres:

![Opis wykresu](assets/wykres.png)
```

### Instalacja i podgląd

W terminalu (w systemie Windows można użyć również `py -m pip`):

```bash
python -m pip install mkdocs-material
```

W katalogu z plikiem `mkdocs.yml` uruchom:

```bash
mkdocs serve
```

Następnie otwórz wskazany lokalny adres, zwykle `http://127.0.0.1:8000/`.

Aby zbudować gotowe pliki strony, użyj:

```bash
mkdocs build
```

Wynik znajdziesz domyślnie w katalogu `site/`. Nie należy mylić tego katalogu z folderem `docs/`, który przechowuje pliki źródłowe Markdown.

### Wzory matematyczne w MkDocs

Jeżeli dokumentacja zawiera matematykę, skonfiguruj jej renderowanie, np. za pomocą **Arithmatex i MathJax**. W pliku `mkdocs.yml` można dodać:

```yaml
markdown_extensions:
  - pymdownx.arithmatex:
      generic: true
extra_javascript:
  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js
```

### Publikacja MkDocs

Po sprawdzeniu projektu przez `mkdocs serve` oraz `mkdocs build`, w **repozytorium projektu MkDocs** możesz użyć:

```bash
mkdocs gh-deploy
```

Polecenie buduje dokumentację i wysyła wygenerowaną stronę do gałęzi `gh-pages`. Jeżeli jest to potrzebne, wybierz w **Settings → Pages** gałąź `gh-pages` i katalog `/(root)`. Nie edytuj ręcznie plików w gałęzi `gh-pages` — kolejne wdrożenie może je nadpisać.

Dokumentacja: [MkDocs](https://www.mkdocs.org/) · [Publikacja MkDocs](https://www.mkdocs.org/user-guide/deploying-your-docs/) · [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

---

## 7. Uwagi dotyczące zadań

Ważne:

**Zadania 1–3:** wykonujesz lokalne strony HTML i zapisujesz je w odpowiednich folderach **swojego forka repozytorium przedmiotu**. Nie publikujesz ich jeszcze przez GitHub Pages.

**Zadania 4–7:** publikujesz projekty w internecie w swoich osobistych repozytoriach (muszą być publiczne). W odpowiednim folderze **forka repozytorium przedmiotu** umieszczasz tylko informacje o swoich repozytoriach i opublikowanych stronach (w plikach `LINK.md` podając adres **działającej strony** oraz **repozytorium projektu**).

W forku repozytorium przedmiotu zachowaj przygotowaną strukturę katalogów:

```text
01_sol_html/
└── index.html
02_sol_html/
├── index.html
├── style.css
└── images/
    └── obraz.png
03_sol_html/
└── index.html
04_sol_html/
└── LINK.md
05_sol_html/
└── LINK.md
06_sol_html/
└── LINK.md
07_sol_html/
└── LINK.md
```

Szablon pliku `LINK.md`:

```markdown
# Publikacja strony N

## Strona

https://NAZWA-UZYTKOWNIKA.github.io/nazwa-repozytorium/

## Repozytorium

https://github.com/NAZWA-UZYTKOWNIKA/nazwa-repozytorium/
```

---

### Zadanie 1. Prosta strona HTML

Utwórz `01_sol_html/index.html`. Strona ma zawierać nagłówek, co najmniej dwa akapity, listę, tabelę i link do innej strony. Zadbaj o poprawną strukturę HTML, tytuł dokumentu i UTF-8. **Nie używaj CSS ani JavaScript.**

### Zadanie 2. HTML + CSS + obrazy

Przygotuj w folderze `02_sol_html/` nową wersję strony z zadania 1. Dodaj oddzielny `style.css`, jakiś niewielki obrazek w formacie PNG lub JPG w podfolderze `images/` oraz użyj go w treści strony.

### Zadanie 3. Interaktywna strona I — rzut ukośny

Z pomocą AI stwórz jedną interaktywną stronę HTML (z przyciskami i suwakami) dotyczącą **rzutu ukośnego**. Mają być **co najmniej trzy suwaki**, przyciski sterujące oraz reagujący na zmiany parametrów wykres, animację lub symulację. Dodaj wyświetlanie wektorów prędkości i przyspieszenia. Preferowany jest **jeden samodzielny plik**, który powinien znajdować się w `03_sol_html/index.html`.

Uwaga: czasem zamiast pliku do pobrania AI podaje kod HTML jako tekst. Wklej go wtedy do pliku `.txt` i zmień rozszerzenie na `.html`. Jeśli AI otworzy działający podgląd strony, zapisz jej kod do pliku.

### Zadanie 4. Publikacja przez GitHub Pages

Utwórz na swoim koncie **nowe publiczne repozytorium** o nazwie `rzut`. Umieść w nim stronę HTML z **zadania 3** i opublikuj ją przez GitHub Pages. W pliku `04_sol_html/LINK.md` na forku przedmiotu podaj link do działającej strony oraz do nowego repozytorium.

### Zadanie 5. Profesjonalna strona edukacyjna z AI

Utwórz na swoim koncie **nowe publiczne repozytorium** o nazwie `edukacja`. Wykorzystaj najbardziej zaawansowane narzędzia AI, jakie masz, do stworzenia **nowoczesnej, estetycznej i rozbudowanej strony edukacyjnej** o wybranym zagadnieniu z **matematyki, fizyki lub algorytmiki**. Oczekiwane są: atrakcyjna sekcja powitalna, spójna stylistyka, animacja w banerze strony, inne animacje, interaktywne wykresy lub symulacje, suwaki oraz wygodna i dynamiczna nawigacja. Strona powinna poprawnie działać również na telefonie. Opublikuj stronę i wpisz jej **adres** oraz **adres repozytorium** do `05_sol_html/LINK.md`.

### Zadanie 6. Interaktywny quiz

Utwórz na swoim koncie **nowe publiczne repozytorium** o nazwie `quiz`. Przygotuj stronę z **co najmniej 10 pytaniami** dotyczącymi wybranego zagadnienia. Dodaj różne typy pytań, automatyczne sprawdzanie, wynik, wyjaśnienia odpowiedzi i możliwość rozpoczęcia testu od nowa. Opublikuj projekt i dodaj linki do `06_sol_html/LINK.md`.

### Zadanie 7. Strona wykorzystująca publiczne API

API to interfejs umożliwiający pobieranie danych z zewnętrznych źródeł w sposób ustandaryzowany. Akronim pochodzi od angielskiego terminu **Application Programming Interface**. Jest to sposób komunikacji między różnymi aplikacjami, który pozwala na korzystanie z funkcji lub danych udostępnionych przez inne systemy.

Stwórz stronę pobierającą **rzeczywiste dane** (np. pogodowe, astronomiczne lub statystyczne, itd.) z publicznego API (np. OpenWeatherMap, NASA lub GUS). Zaprezentuj je na wykresie lub w tabeli, dodaj interaktywne filtry i obsłuż błędy pobierania danych. Korzystaj z API dostępnego z przeglądarki, bez ujawniania tajnych kluczy. Opublikuj stronę i dodaj linki do `07_sol_html/LINK.md`.
