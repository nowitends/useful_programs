# WWW, Interaktywne materiały i publikacja w sieci

W tym bloku poznamy:

| Narzędzie | Zastosowanie |
| --- | --- |
| **HTML** | budowa strony internetowej |
| **CSS** | wygląd strony |
| **JavaScript** | zachowanie i interakcja |
| **MkDocs** | tworzenie stron dokumentacji z plików Markdown |
| **GitHub Pages** | publikacja statycznej strony |
| **Chatgpt Sites** | tworzenie stron z wykorzystaniem ChatGPT |
| **Interaktywne materiały** | tworzenie interaktywnychaplikacji, wizualizacji i eksperymentów (Matplotlib, Plotly) |

---

# Od pliku do strony WWW

## Co właściwie otwiera przeglądarka?

Przeglądarka potrafi wyświetlić plik HTML. HTML jest przede wszystkim językiem opisującym **strukturę dokumentu internetowego**.

Najprostszy przykład:

~~~html
<!doctype html>
<html lang="pl">
<head>
    <meta charset="utf-8">
    <title>Moja pierwsza strona</title>
</head>
<body>
    <h1>Ogłoszenia</h1>

    <p>To jest moja pierwsza strona HTML.</p>
</body>
</html>
~~~

Jeżeli zapiszemy ten tekst w pliku tekstowym (ze zmianą rozszerzenia na `.html`) jako:

~~~text
index.html
~~~

i otworzymy plik w przeglądarce, zobaczymy stronę z nagłówkiem i akapitem.

Plik html musisz wysłać na serwer WWW, aby był dostępny w sieci. Inaczej będzie można go otworzyć tylko lokalnie na swoim komputerze lub po przesłaniu mejlem lub komunikatorami na komputer innej osoby.

---

# HTML

## Elementy HTML

Większość elementów HTML ma znacznik otwierający i zamykający.

Przykład:

~~~html
<p>To jest akapit.</p>
~~~

Tutaj:

- `<p>` — otwiera akapit,
- `</p>` — zamyka akapit,
- tekst pomiędzy nimi jest zawartością.

---

## Nagłówki

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

---

## Akapit

~~~html
<p>
    Badanie dotyczy zależności y od x.
</p>
~~~

Element `p` oznacza akapit.

---

## Lista

~~~html
<ul>
    <li>Python</li>
    <li>NumPy</li>
    <li>Plotly</li>
</ul>
~~~

`ul` oznacza listę nieuporządkowaną, a `li` pojedynczy element listy.

Lista numerowana używa `ol`:

~~~html
<ol>
    <li>Wczytaj dane</li>
    <li>Wykonaj obliczenia</li>
    <li>Narysuj wykres</li>
</ol>
~~~

---

## Link

~~~html
<a href="https://github.com/">GitHub</a>
~~~

Element `a` tworzy link.

Atrybut `href` zawiera adres docelowy.

---

## Obraz

~~~html
<img src="wykres.png" alt="Wykres wyników">
~~~

Atrybuty:

- `src` — wskazuje plik obrazu,
- `alt` — opisuje obraz.

Opis alternatywny jest ważny także wtedy, gdy obraz z jakiegoś powodu nie może się załadować.

---

## Tabela

~~~html
<table>
    <tr>
        <th>x</th>
        <th>y</th>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
    </tr>
</table>
~~~

Najważniejsze znaczniki:

- `table` — tabela,
- `tr` — wiersz,
- `th` — komórka nagłówkowa,
- `td` — zwykła komórka.

---

# CSS — wygląd strony

HTML skupia się na strukturze i zawartościstrony. **CSS** odpowiada za wygląd strony. Podobnie jak LaTeX oddziela treść od formatu, HTML oddziela strukturę od wyglądu.

Przykład:

~~~html
<style>
body {
    font-family: sans-serif;
    max-width: 900px;
    margin: 40px auto;
    line-height: 1.6;
}

h1 {
    border-bottom: 1px solid #ccc;
}
</style>
~~~

Po dodaniu takiego fragmentu do sekcji `head` strona będzie miała czytelniejszy układ.

W tym kursie nie będziemy uczyć się projektowania stron WWW jako osobnej specjalności. Wystarczy rozumieć, że:

~~~text
HTML       → struktura
CSS        → wygląd
JavaScript → zachowanie
~~~

---

# JavaScript — prosta interakcja

HTML opisuje strukturę dokumentu. JavaScript pozwala dodać do strony reakcje na działania użytkownika.

Poniższy fragment łączy HTML z JavaScriptem. Po kliknięciu przycisku licznik zwiększy się o 1:

~~~html
<p id="wynik">0</p>

<button id="przycisk" type="button">Kliknij</button>

<script>
let licznik = 0;
const wynik = document.getElementById("wynik");

document.getElementById("przycisk").addEventListener("click", function () {
    licznik = licznik + 1;
    wynik.textContent = licznik;
});
</script>
~~~

Obsługa zdarzenia `click` uruchamia funkcję po kliknięciu przycisku. Funkcja zwiększa wartość zmiennej `licznik` i wyświetla nową wartość w akapicie.

Mamy tu trzy elementy:

1. akapit, w którym wyświetlamy licznik,
2. przycisk, któremu przypisujemy obsługę kliknięcia,
3. kod JavaScript, który zwiększa licznik i aktualizuje akapit.

Nie trzeba teraz szczegółowo poznawać JavaScriptu. Ważne jest zrozumienie, skąd bierze się interaktywność strony.

---

# Strona statyczna

Strona zbudowana z plików takich jak:

~~~text
index.html
style.css
wykres.png
script.js
~~~

może działać bez serwera wykonującego Python czy PHP.

Taki zestaw plików nazywamy tutaj **stroną statyczną**. Dynamiczna strona wymagałaby serwera generującego zawartość w locie.  „Statyczna” nie oznacza, że strona nie może być interaktywna. JavaScript może wykonywać się w przeglądarce. Oznacza raczej, że serwer nie musi przy każdym wejściu użytkownika wykonywać kodu generującego stronę.

---

# Od pliku index.html do strony internetowej

Strona internetowa zaczyna się od pliku `index.html`. To on jest otwierany jako pierwszy przez przeglądarkę.

Pozostałe pliki, takie jak obrazy, arkusze stylów CSS czy skrypty JavaScript, są dołączane do tego pliku i tworzą kompletną stronę.

Taką stronę możemy odpalić lokalnie na swoim komputerze, otwierając plik `index.html` w przeglądarce. W następnych sekcjach pokażemy, jak opublikować ją w Internecie za pomocą GitHub Pages.

---

# GitHub Pages

## Co to jest GitHub Pages?

**GitHub Pages** pozwala opublikować statyczną stronę internetową bezpośrednio na podstawie plików znajdujących się w repozytorium GitHub. Strona projektu może otrzymać adres w rodzaju:

~~~text
https://nazwa-uzytkownika.github.io/nazwa-repozytorium/
~~~

Nie musimy:

- kupować serwera,
- konfigurować Apache,
- utrzymywać własnej maszyny dostępnej przez Internet.

---

## Co może opublikować GitHub Pages?

Dobrze nadają się:

- HTML,
- CSS,
- JavaScript,
- obrazy,
- dokumentacja projektu,
- statyczne raporty,
- interaktywne wykresy działające w przeglądarce.

GitHub Pages nie służy do uruchamiania dowolnego programu Python po stronie serwera.

Jeżeli przygotowaliśmy plik HTML **wcześniej**, możemy go opublikować.

Jeżeli strona wymaga uruchomienia Pythona za każdym wejściem użytkownika, potrzebne jest inne rozwiązanie.

---

## Plik wejściowy

Typową stroną główną jest:

~~~text
index.html
~~~

Przeglądarka otwiera go jako punkt startowy serwisu.

Przykładowa struktura:

~~~text
site/
├── index.html
├── animation.gif
└── interactive_plot.html
~~~

---

## Publikacja z repozytorium

Dokładny interfejs GitHuba może się zmieniać, ale ogólna idea jest stała:

1. pliki strony znajdują się w repozytorium,
2. w ustawieniach repozytorium włączamy GitHub Pages,
3. wskazujemy źródło publikacji,
4. GitHub publikuje stronę,
5. otrzymujemy adres `github.io`.

Po publikacji trzeba zawsze sprawdzić stronę w przeglądarce.

To, że plik istnieje w repozytorium, nie gwarantuje jeszcze, że:

- ścieżki do obrazów są poprawne,
- wielkość liter w nazwach jest zgodna,
- linki względne prowadzą do właściwego miejsca.

Oficjalne materiały:

- [GitHub Pages — dokumentacja](https://docs.github.com/en/pages)
- [GitHub Pages — Getting started](https://docs.github.com/en/pages/getting-started-with-github-pages)

---

# Markdown a strona internetowa

Markdown i HTML nie są konkurentami.

Markdown jest wygodny do pisania treści.

HTML jest formatem, który rozumie przeglądarka.

Wiele narzędzi działa według schematu:

~~~text
Markdown
   ↓
generator strony
   ↓
HTML
   ↓
przeglądarka
~~~

Jednym z takich generatorów jest MkDocs.

---

# MkDocs

## Co to jest MkDocs?

**MkDocs** jest generatorem statycznej dokumentacji.

Pisząc pliki Markdown, możemy zbudować z nich uporządkowaną stronę WWW.

To bardzo wygodne dla:

- dokumentacji projektu,
- materiałów kursowych,
- instrukcji,
- notatek technicznych,
- małych stron projektów.

---

## Najprostszy projekt

Struktura:

~~~text
mkdocs.yml
docs/
├── index.md
└── results.md
~~~

Plik `mkdocs.yml` może zawierać:

~~~yaml
site_name: Moje wyniki

nav:
  - Start: index.md
  - Wyniki: results.md
~~~

`nav` opisuje menu strony.

---

## `docs/index.md`

~~~markdown
# Moje wyniki

To jest strona główna dokumentacji.

## Materiały

- [Wyniki](results.md)
~~~

---

## `docs/results.md`

~~~markdown
# Wyniki

Najważniejsze wyniki projektu.

## Animacja

![Animacja](assets/animation.gif)

## Wykres

[Otwórz interaktywny wykres](assets/interactive_plot.html)
~~~

---

## Instalacja

Jeżeli MkDocs nie jest jeszcze zainstalowany:

~~~bash
python3 -m pip install mkdocs
~~~

Sprawdzenie:

~~~bash
mkdocs --version
~~~

---

## Lokalny podgląd

W katalogu zawierającym `mkdocs.yml`:

~~~bash
mkdocs serve
~~~

W terminalu pojawi się lokalny adres, zwykle zbliżony do:

~~~text
http://127.0.0.1:8000/
~~~

Po otwarciu go w przeglądarce zobaczymy dokumentację.

---

## Budowanie strony

~~~bash
mkdocs build
~~~

MkDocs utworzy gotową stronę statyczną, domyślnie w katalogu:

~~~text
site/
~~~

Czyli:

~~~text
Markdown
   ↓
mkdocs build
   ↓
HTML / CSS / pozostałe pliki
~~~

To dobry przykład oddzielenia:

- **źródła** — pliki Markdown,
- **wyniku procesu budowania** — gotowa strona.

---

## Publikacja MkDocs

MkDocs potrafi publikować zbudowaną dokumentację na GitHub Pages.

Jedna z dostępnych metod wykorzystuje:

~~~bash
mkdocs gh-deploy
~~~

Przed użyciem tej komendy trzeba rozumieć, że narzędzie będzie tworzyć i wysyłać wygenerowaną wersję strony do repozytorium.

Najpierw zawsze warto sprawdzić lokalnie:

~~~bash
mkdocs build
~~~

oraz:

~~~bash
mkdocs serve
~~~

Dopiero potem publikować.

Oficjalna dokumentacja:

- [MkDocs](https://www.mkdocs.org/)
- [MkDocs — Getting Started](https://www.mkdocs.org/getting-started/)

---

## Zadanie 1. Mała strona HTML

Utwórz:

~~~text
index.html
~~~

Strona ma zawierać:

- poprawną strukturę HTML,
- kodowanie UTF-8,
- tytuł strony,
- nagłówek `h1`,
- co najmniej dwa akapity,
- listę,
- link
- obrazek

---
## Zadanie 6. Publikacja na GitHub Pages

Opublikuj przygotowaną dokumentację jako GitHub Pages.

Możesz użyć mechanizmu publikacji dostępnego dla MkDocs, np.:

~~~bash
mkdocs gh-deploy
~~~

albo skonfigurować GitHub Pages zgodnie z aktualną dokumentacją GitHuba.

Po publikacji utwórz:

~~~text
publication.md
~~~

Plik ma zawierać:

~~~markdown
# Publikacja

## Adres strony

...

## Co zostało opublikowane?

...

## Test

...

## Uwagi

...
~~~

W części **Adres strony** podaj działający adres `github.io`.

W części **Test** napisz, czy sprawdziłeś:

- stronę główną,
- przejście do Wyników,
- animację,
- interaktywny wykres.

Jeżeli publikacja GitHub Pages nie jest możliwa z powodów technicznych lub ograniczeń konta, opisz dokładnie problem w sekcji **Uwagi** i pozostaw działający lokalny build MkDocs.

### Sprawdzenie

Można sprawdzić:

- istnienie `publication.md`,
- obecność adresu strony,
- publiczną dostępność strony, jeśli została opublikowana,
- strukturę lokalnego projektu niezależnie od publikacji.

---

# Zadania

# Lista zadań — Strony internetowe

Celem zadań jest poznanie podstaw HTML, CSS i JavaScript, a następnie tworzenie i publikowanie stron internetowych z wykorzystaniem GitHub Pages, MkDocs oraz narzędzi AI.

## Zadanie 1. Prosta strona HTML

Stwórz prostą stronę internetową zawierającą nagłówki, tekst, listy, tabelę i odnośniki. Całość zapisz w podfolderze `01_sol_html` w jednym pliku `index.html`, bez CSS i JavaScript.

## Zadanie 2. HTML + CSS

Rozbuduj stronę z zadania 1, dodając:
- Oddzielny plik `style.css` odpowiedzialny za wygląd strony.
- Obraz zapisany lokalnie w podfolderze `images`.
- Obraz z Wikipedii lub Wikimedia Commons wyświetlany bezpośrednio z internetu.

Zadbaj o estetykę i poprawne formatowanie. Umieść nową wersję `index.html` w podfolderze `02_sol_html` w repozytorium.

## Zadanie 3. Interaktywna strona edukacyjna

Wykorzystując AI, stwórz interaktywną stronę dotyczącą zagadnienia z **matematyki, fizyki lub algorytmiki**.

Strona powinna zawierać liczne suwaki, przyciski, przełączniki, dynamiczne wykresy i animacje. Użytkownik musi mieć możliwość zmieniania parametrów i obserwowania efektów.

Preferowany jest pojedynczy plik `index.html` zawierający HTML, CSS i JavaScript. Umieść go w podfolderze `03_sol_html` w repozytorium.

## Zadanie 4. Publikacja na GitHub Pages

Utwórz **nowe, publiczne repozytorium GitHub** o nazwie związanej z tematyką projektu (nie `Strona1`, `Zadanie4` itp.).

Przenieś do niego stronę z zadania 3 i opublikuj ją za pomocą GitHub Pages. Umieść ją w podfolderze `04_sol_html` w repozytorium.

W przygotowanym folderze zadania 4 na forku repozytorium przedmiotu umieść w pliku `LINK.md` (w podfolderze `04_sol_html`):

- Link do działającej strony.

- Link do repozytorium z kodem.

## Zadanie 6. Profesjonalna strona edukacyjna z AI

Wykorzystaj najbardziej zaawansowane narzędzia AI, do których masz dostęp, aby stworzyć **nowoczesną, efektowną i profesjonalną stronę edukacyjną**.

Strona powinna zawierać animacje, atrakcyjne banery, interaktywne wizualizacje, suwaki, wykresy oraz dobrze przygotowane treści edukacyjne. Zadbaj o estetykę, funkcjonalność i działanie na urządzeniach mobilnych.

**Przykładowe strony, na których należy się wzorować:**
- [PRZYKŁAD 1 — LINK]
- [PRZYKŁAD 2 — LINK]
- [PRZYKŁAD 3 — LINK]

Stwórz stronę o podobnym poziomie wizualnym i funkcjonalnym, ale dotyczącą własnego zagadnienia.

Opublikuj ją przez GitHub Pages i umieść odpowiednie linki w `LINK.md`.

## Zadanie 7. Interaktywny quiz

Stwórz stronę umożliwiającą sprawdzanie wiedzy z wybranego zagadnienia.

Powinna zawierać pytania różnych typów, automatyczne sprawdzanie odpowiedzi, punktację, podsumowanie wyników i możliwość ponownego rozwiązania testu.

Wykorzystaj `localStorage` do zapisywania wyników w przeglądarce. Opublikuj stronę przez GitHub Pages.

## Zadanie 8. Strona wykorzystująca API

Stwórz stronę pobierającą rzeczywiste dane z internetu przez publiczne API, np. pogodowe, astronomiczne, ekonomiczne lub statystyczne.

Dane powinny być prezentowane w formie interaktywnych wykresów, tabel lub wizualizacji. Użytkownik powinien mieć możliwość zmiany wyświetlanych informacji.

Opublikuj stronę przez GitHub Pages.


## Zadanie 5. Markdown → MkDocs

W przygotowanym folderze znajdziesz zestaw plików Markdown.

Wykorzystaj **MkDocs (najlepiej Material for MkDocs)**, aby przekształcić je w estetyczną stronę dokumentacyjną z poprawną nawigacją.

Opublikuj stronę przez GitHub Pages. W pliku `LINK.md` umieść adres strony i repozytorium.


---

**Zasady:** Zadania 1–3 realizujemy lokalnie i umieszczamy w odpowiednich folderach forka repozytorium przedmiotu. Zadania 4–8 wymagają publikacji w internecie oraz umieszczenia linków do działających stron i repozytoriów w odpowiednich plikach `LINK.md`. Wszystkie projekty mogą być realizowane z pomocą AI, ale muszą działać poprawnie i spełniać wymagania.