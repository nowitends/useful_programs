# WWW — interaktywne materiały i publikacja w sieci

W tym bloku przejdziemy od **prostego pliku HTML** do **interaktywnej strony edukacyjnej opublikowanej w internecie**. Będziemy korzystać z HTML, CSS, JavaScript, GitHuba, GitHub Pages, MkDocs oraz narzędzi AI.

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

> **Najważniejsze rozróżnienie:** plik zapisany na GitHubie nie jest automatycznie opublikowaną stroną WWW. Do publikacji wykorzystamy GitHub Pages.

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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
    color: #233247;
    background: #f6f8fc;
}

h1 {
    color: #175b99;
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

Poniższy przykład wyświetla aktualną wartość suwaka:

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

Połączenie suwaków z obliczeniami, wykresami i animacjami pozwala tworzyć interaktywne doświadczenia z fizyki, matematyki czy algorytmiki. Do wykresów można użyć np. **Plotly.js** lub własnego kodu rysującego w **SVG** albo **Canvas**. **Matplotlib** może służyć do przygotowywania ilustracji i animacji eksportowanych z Pythona, ale sam kod Pythona nie uruchomi się w przeglądarce dzięki GitHub Pages.

### Czy strona statyczna może być interaktywna?

**Tak.** „Statyczna” oznacza, że serwer udostępnia gotowe pliki, np. `index.html`, `style.css` i `script.js`. JavaScript działa następnie w przeglądarce użytkownika i może obsługiwać animacje, quizy, symulacje, a nawet pobierać aktualne dane z zewnętrznego API.

GitHub Pages **nie uruchamia po stronie serwera** aplikacji napisanych w Pythonie, PHP ani systemów wymagających własnej bazy danych i backendu.

---

## 4. GitHub Pages — publikacja strony

GitHub Pages umożliwia publikację gotowych plików strony z repozytorium GitHub. Typowy adres strony projektu wygląda następująco:

```text
https://NAZWA-UZYTKOWNIKA.github.io/NAZWA-REPOZYTORIUM/
```

### Dwie rzeczy, których nie należy mylić

- **Fork repozytorium przedmiotu** — miejsce, w którym oddajesz zadania i pliki wskazane przez prowadzącego.
- **Nowe repozytorium projektu** — osobne publiczne repozytorium na Twoim koncie, z którego publikujesz swoją stronę WWW.

W zadaniu 4 należy utworzyć **nowe repozytorium**, a nie kolejny fork ani podfolder nazwany `Strona1`.

### Najprostsza publikacja krok po kroku

1. Utwórz nowe **publiczne** repozytorium z nazwą opisującą projekt, np. `motion-simulator`.
2. Dodaj plik `index.html` i ewentualne obrazy, style oraz skrypty. Dla najprostszego projektu `index.html` umieść w katalogu głównym.
3. Otwórz **Settings → Pages** w repozytorium projektu.
4. W sekcji **Build and deployment** wybierz **Deploy from a branch**, gałąź `main` i folder `/(root)`, a następnie zapisz ustawienia.
5. Otwórz adres strony z sekcji Pages i sprawdź, czy strona faktycznie działa. Publikacja i późniejsze aktualizacje mogą pojawiać się z opóźnieniem.

**Uwaga na ścieżki:** w stronach projektów GitHub Pages odwołania typu `images/wykres.png` lub `./style.css` są zwykle bezpieczniejsze od odwołań zaczynających się od `/`, które wskazują katalog główny domeny, a nie katalog projektu.

**Sprawdź przed oddaniem:** stronę w oknie prywatnym, obrazy, przyciski, wykresy, odnośniki i widok mobilny. Link do samego pliku `index.html` w serwisie `github.com` **nie zastępuje** adresu opublikowanej strony `github.io`.

Dokumentacja: [GitHub Pages](https://docs.github.com/en/pages) · [Konfiguracja źródła publikacji](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

---

## 5. Markdown → MkDocs → strona WWW

Markdown dobrze nadaje się do pisania treści, ale nie zapewnia samodzielnie całego serwisu z menu, motywem i wyszukiwarką. **MkDocs** tworzy z plików `.md` gotową, statyczną stronę dokumentacyjną.

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

W plikach Markdown zapisuj wzory wewnątrz tekstu jako `$a^2+b^2=c^2$`, a wzory blokowe w osobnych liniach między `$$`:

```latex
$$
A=\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\qquad \det A=-2.
$$
```

W przykładach Markdown **nie zamieniaj** podwójnego ukośnika `\\` oddzielającego wiersze macierzy na pojedynczy `\`.

### Publikacja MkDocs

Po sprawdzeniu projektu przez `mkdocs serve` oraz `mkdocs build`, w **repozytorium projektu MkDocs** możesz użyć:

```bash
mkdocs gh-deploy
```

Polecenie buduje dokumentację i wysyła wygenerowaną stronę do gałęzi `gh-pages`. Jeżeli jest to potrzebne, wybierz w **Settings → Pages** gałąź `gh-pages` i katalog `/(root)`. Nie edytuj ręcznie plików w gałęzi `gh-pages` — kolejne wdrożenie może je nadpisać.

Dokumentacja: [MkDocs](https://www.mkdocs.org/) · [Publikacja MkDocs](https://www.mkdocs.org/user-guide/deploying-your-docs/) · [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

---

## 6. AI jako narzędzie do tworzenia stron

Nie musisz pisać wszystkiego od zera. Możesz poprosić AI o przygotowanie kodu, zaproponowanie układu strony, dodanie animacji czy naprawienie błędów. **Za ostateczne działanie strony odpowiadasz jednak Ty.**

Dobry sposób pracy:

1. Określ temat, odbiorcę i konkretne funkcje strony.
2. Podaj ograniczenia techniczne, np. „jeden plik `index.html`, bez serwera, do publikacji na GitHub Pages”.
3. Uruchom wygenerowaną stronę i sprawdź wszystkie elementy interaktywne.
4. Zgłoś AI konkretne błędy i poprawiaj projekt iteracyjnie.
5. Sprawdź wynik po **publikacji**, a nie tylko w podglądzie narzędzia AI.

**Przykładowe polecenie:**

> Stwórz pojedynczy plik `index.html` przedstawiający interaktywną symulację rzutu ukośnego. Dodaj suwaki prędkości początkowej, kąta i przyspieszenia grawitacyjnego, animację toru, wykres oraz przyciski Start, Pauza i Reset. Wszystkie sterowania muszą działać. Strona ma otwierać się lokalnie i nadawać do publikacji na GitHub Pages.

Nie umieszczaj w publicznym kodzie haseł, prywatnych danych ani tajnych kluczy API. Jeśli korzystasz z bibliotek, obrazów lub materiałów zewnętrznych, podaj ich źródła i sprawdź warunki wykorzystania.

---

## 7. Zadania — strony internetowe

**Zadania 1–3:** wykonujesz lokalne strony i zapisujesz je w odpowiednich folderach **swojego forka repozytorium przedmiotu**. Nie publikujesz ich jeszcze przez GitHub Pages.

**Zadania 4–8:** publikujesz projekty w internecie. W odpowiednim folderze forka umieszczasz `LINK.md` z adresem **działającej strony** oraz **repozytorium projektu**.

### Zadanie 1. Prosta strona HTML

Utwórz `01_sol_html/index.html`. Strona ma zawierać nagłówek, co najmniej dwa akapity, listę, tabelę i link do innej strony. Zadbaj o poprawną strukturę HTML, tytuł dokumentu i UTF-8. **Nie używaj CSS ani JavaScript.**

### Zadanie 2. HTML + CSS + obrazy

Przygotuj w folderze `02_sol_html/` nową wersję strony z zadania 1. Dodaj oddzielny `style.css`, obraz lokalny w podfolderze `images/` oraz obraz z Wikipedii lub Wikimedia Commons wyświetlany z jego internetowego adresu. Zadbaj o czytelny układ i wskaż źródło grafiki.

### Zadanie 3. Interaktywna strona edukacyjna

Z pomocą AI stwórz lokalną stronę dotyczącą **matematyki, fizyki lub algorytmiki**. Dodaj **co najmniej trzy suwaki**, przyciski sterujące oraz reagujący na zmiany parametrów wykres, animację lub symulację. Preferowany jest **jeden samodzielny plik `03_sol_html/index.html`** z HTML, CSS i JavaScript.

### Zadanie 4. Publikacja przez GitHub Pages

Utwórz na swoim koncie **nowe publiczne repozytorium** o nazwie związanej z tematyką zadania 3 (nie `Strona1` ani `Zadanie4`). Umieść w nim stronę i opublikuj ją przez GitHub Pages. W pliku **`04_sol_html/LINK.md` na forku przedmiotu** podaj link do działającej strony oraz do nowego repozytorium.

### Zadanie 5. Markdown → MkDocs

Z udostępnionych przez prowadzącego plików Markdown zbuduj stronę dokumentacyjną w **MkDocs**, najlepiej z motywem Material. Zorganizuj menu, zadbaj o działające odnośniki i poprawne wyświetlanie ilustracji, tabel i wzorów (jeżeli występują). Opublikuj projekt przez GitHub Pages. Linki zapisz w **`05_sol_html/LINK.md`** na forku przedmiotu; nie usuwaj przygotowanych plików źródłowych.

### Zadanie 6. Profesjonalna strona edukacyjna z AI

Wykorzystaj zaawansowane narzędzia AI do stworzenia **nowoczesnej, estetycznej i rozbudowanej strony edukacyjnej** o wybranym zagadnieniu. Oczekiwane są: atrakcyjna sekcja powitalna, spójna stylistyka, animacje, interaktywne wykresy lub symulacje, suwaki oraz wygodna nawigacja. Strona powinna poprawnie działać również na telefonie.

**Wzorce jakości i sposobu prezentacji:**

1. [Prompt Engineering 2026 — interaktywne materiały edukacyjne](https://prompt-engineering-a59a57.gitlab.io/)
2. **[PRZYKŁAD 2 — LINK DO UZUPEŁNIENIA]**
3. **[PRZYKŁAD 3 — LINK DO UZUPEŁNIENIA]**

Przykłady są **inspiracją**, a nie szablonem do kopiowania. Przygotuj własny temat i własne rozwiązania. Opublikuj stronę i wpisz jej adres oraz adres repozytorium do **`06_sol_html/LINK.md`**.

### Zadanie 7. Interaktywny quiz

Przygotuj stronę z **co najmniej 10 pytaniami** dotyczącymi wybranego zagadnienia. Dodaj różne typy pytań, automatyczne sprawdzanie, wynik, wyjaśnienia odpowiedzi i możliwość rozpoczęcia testu od nowa. Zapisuj ostatni wynik w przeglądarce przez `localStorage`. Opublikuj projekt i dodaj linki do **`07_sol_html/LINK.md`**.

### Zadanie 8. Strona wykorzystująca publiczne API

Stwórz stronę pobierającą **rzeczywiste dane** z publicznego API, np. pogodowego, astronomicznego lub statystycznego. Zaprezentuj je na wykresie lub w tabeli, dodaj interaktywne filtry i obsłuż błędy pobierania danych. Korzystaj z API dostępnego z przeglądarki, bez ujawniania tajnych kluczy. Opublikuj stronę i dodaj linki do **`08_sol_html/LINK.md`**.

---

## 8. Oddawanie zadań i automatyczne sprawdzanie

W forku repozytorium przedmiotu zachowaj przygotowaną strukturę katalogów. Przykładowy układ plików do oddania:

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
├── ... (materiały dostarczone przez prowadzącego)
└── LINK.md
06_sol_html/
└── LINK.md
07_sol_html/
└── LINK.md
08_sol_html/
└── LINK.md
```

W zadaniach 4–8 **kod opublikowanej strony znajduje się w repozytorium projektu**, natomiast `LINK.md` w forku przedmiotu wskazuje, gdzie go znaleźć. Jeśli foldery 5–8 w przygotowanym repozytorium mają inne nazwy, użyj nazw nadanych przez prowadzącego — nie twórz równoległej struktury.

Szablon pliku `LINK.md`:

```markdown
# Publikacja — zadanie N

- Strona: https://NAZWA-UZYTKOWNIKA.github.io/NAZWA-REPOZYTORIUM/
- Repozytorium: https://github.com/NAZWA-UZYTKOWNIKA/NAZWA-REPOZYTORIUM
```

**Przed oddaniem sprawdź:**

- Czy wszystkie wymagane pliki są w odpowiednich folderach i czy nazwy plików są poprawne.
- Czy strona otwiera się bez błędów, a obrazy, wykresy i przyciski działają.
- Czy adres `github.io` prowadzi do **opublikowanej strony**, a nie do pliku na GitHubie.
- Czy strona jest dostępna publicznie także w trybie prywatnym przeglądarki.
- Czy plik `LINK.md` zawiera **dwa prawidłowe linki**, które można automatycznie sprawdzić.

Możesz korzystać z AI na każdym etapie. Oceniamy jednak **działający rezultat**, poprawność merytoryczną, jakość wykonania i spełnienie wymagań — nie samo wygenerowanie kodu.
