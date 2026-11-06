# Grafika naukowa i użytkowa

Grafika w pracy naukowej może być wykresem danych, schematem aparatury, diagramem zależności, ilustracją koncepcyjną albo elementem prezentacji.

Nie każdą grafikę tworzymy tym samym narzędziem.

Po wykładach o Markdownie, Colabie, GitHubie i LaTeX-u potrafimy już zapisać dane, uruchomić kod i złożyć raport. Teraz zadbamy o to, aby rysunki w tych plikach były **czytelne, wierne danym i możliwe do poprawienia**. Dlatego obok końcowego obrazu zachowujemy jego źródło: SVG, kod wykresu albo kod TikZ.

| Narzędzie | Zastosowanie |
| --- | --- |
| **Inkscape** | grafika wektorowa, schematy, diagramy |
| **Matplotlib** | wykresy tworzone z danych przez kod Pythona |
| **Generatory obrazów AI** | ilustracje koncepcyjne i warianty stylistyczne |
| **IrfanView** | konwersja, skalowanie i operacje wsadowe |
| **TikZ** | diagramy zintegrowane z LaTeX-em |
| **TikZiT** | graficzna edycja diagramów z węzłów i połączeń, zapisanych w podzbiorze TikZ |

---

# Raster i wektor

## Grafika rastrowa

Grafika rastrowa składa się z pikseli.

Typowe formaty:

~~~text
PNG
JPG
GIF
TIFF
~~~

Obraz:

~~~text
1200 × 800 px
~~~

ma 1200 pikseli w poziomie i 800 w pionie.

Raster dobrze nadaje się do:

- zdjęć,
- zrzutów ekranu,
- obrazów generowanych przez AI,
- wyników symulacji zapisanych jako obraz.

Jeżeli mały raster mocno powiększymy, zaczniemy widzieć piksele. Samo zwiększenie liczby pikseli nie odzyskuje informacji, której wcześniej w obrazie nie było.

---

## Grafika wektorowa

Grafika wektorowa przechowuje obiekty geometryczne:

- linie,
- krzywe,
- okręgi,
- prostokąty,
- tekst.

Typowy format:

~~~text
SVG
~~~

Zamiast pamiętać kolor każdego piksela, plik może przechowywać informację w rodzaju:

~~~text
narysuj okrąg
o środku (100,100)
i promieniu 40
~~~

Dlatego grafikę wektorową można zwykle skalować bez utraty ostrości.

---

## Kiedy którego formatu użyć?

| Materiał | Dobry wybór |
| --- | --- |
| zdjęcie | JPG / PNG |
| zrzut ekranu | PNG |
| logo | SVG / PDF |
| schemat | SVG / PDF |
| diagram do publikacji | SVG / PDF / TikZ |
| wykres naukowy | PDF / SVG albo dobrej jakości PNG |
| ilustracja AI | zwykle PNG / JPG |

Dobra zasada:

> Jeśli grafika składa się głównie z linii, tekstu i prostych kształtów, warto rozważyć format wektorowy.

---

# Rozdzielczość i rozmiar w druku

Rozmiar obrazu na ekranie opisujemy zwykle liczbą pikseli.

Przykład:

~~~text
1920 × 1080 px
~~~

Przy przygotowaniu rastra do druku ważna jest **efektywna liczba pikseli na cal wydruku**, czyli PPI (*pixels per inch*). DPI (*dots per inch*) opisuje punkty nanoszone przez drukarkę; w rozmowach o obrazach oba skróty bywają mylone. Sam wpis „300 DPI” w metadanych nie doda pikseli do małego pliku.

Jeżeli chcemy wydrukować obraz o szerokości $6\,\mathrm{in}$ przy $300\,\mathrm{ppi}$, potrzebujemy:

$$
6\cdot300=1800
$$

pikseli w poziomie.

Obraz o szerokości $10\,\mathrm{cm}$ ma około:

$$
\frac{10}{2.54}\approx3.94\,\mathrm{in}
$$

Przy $300\,\mathrm{ppi}$ daje to około:

$$
3.94\cdot300\approx1182
$$

piksele.

Ta zależność dotyczy grafiki rastrowej. Wykres wektorowy można zwykle skalować bez dobierania liczby pikseli, choć umieszczone w nim zdjęcia nadal mają skończoną rozdzielczość.

---

# PNG, JPG, SVG i PDF

## PNG

PNG stosuje kompresję bezstratną. Dobrze nadaje się do wykresów, zrzutów ekranu i grafiki z przezroczystością.

## JPG

JPG stosuje kompresję stratną. Dobrze nadaje się do zdjęć, ale zwykle gorzej do diagramów z cienkimi liniami i tekstem.

## SVG

SVG jest tekstowym formatem wektorowym opartym na XML.

Przykład:

~~~xml
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="300"
    height="120"
>
    <circle
        cx="60"
        cy="60"
        r="35"
        fill="none"
        stroke="black"
    />

    <text
        x="120"
        y="65"
        font-size="24"
    >
        wynik
    </text>
</svg>
~~~

Po otwarciu w przeglądarce zobaczymy okrąg i tekst.

## PDF

PDF może przechowywać grafikę wektorową.

Przykład z Matplotlib:

~~~python
plt.savefig("plot.pdf")
~~~

Taki wykres może zachować ostre linie i tekst przy powiększaniu.

Nie każdy PDF jest jednak automatycznie wektorowy. PDF może również zawierać zwykły raster.

Zmiana rozszerzenia pliku z `.jpg` na `.png` lub wklejenie małego PNG do PDF nie poprawia jakości obrazu. Konwersja zmienia sposób zapisu, a ponowne wygenerowanie z danych lub źródła SVG może rzeczywiście dać ostrzejszy wynik.

---

# Inkscape

## Co to jest Inkscape?

**Inkscape** jest edytorem grafiki wektorowej. Jego podstawowym formatem jest SVG.

Nadaje się bardzo dobrze do:

- schematów,
- ikon,
- diagramów,
- prostych ilustracji naukowych,
- składania kilku elementów,
- eksportu do SVG, PDF i PNG.

---

## Proste obiekty

W Inkscape możemy tworzyć:

- prostokąty,
- elipsy,
- linie,
- krzywe Béziera,
- tekst,
- strzałki.

Wiele dobrych diagramów technicznych powstaje z bardzo prostego zestawu:

~~~text
prostokąt + strzałka + tekst
~~~

---

## Wyrównanie i odstępy

Przy schematach bardzo ważne są:

- **Align** — wyrównanie,
- **Distribute** — równomierne rozłożenie,
- **Snap** — przyciąganie do punktów i prowadnic.

Trzy prawie równo ustawione elementy wyglądają gorzej niż trzy dokładnie wyrównane.

---

## Grupowanie

Kilka elementów można połączyć w grupę.

Przykład:

~~~text
[okrąg] + [tekst "A"]
          ↓
        grupa
~~~

Po zgrupowaniu można przesuwać całość jako jeden obiekt.

---

## Warstwy

Przy większym rysunku wygodny może być podział:

~~~text
warstwa 1 — tło
warstwa 2 — główny diagram
warstwa 3 — opisy
warstwa 4 — adnotacje
~~~

Warstwy ułatwiają ukrywanie i blokowanie fragmentów grafiki.

---

## Krzywe i węzły

Ścieżka wektorowa składa się z węzłów i odcinków lub krzywych między nimi.

Warto umieć:

- dodać węzeł,
- przesunąć węzeł,
- zmienić kształt krzywej,
- zamknąć ścieżkę.

---

# Tekst w grafice

Tekst powinien być czytelny w **docelowym rozmiarze** grafiki.

Rysunek może wyglądać dobrze na całym ekranie, ale po zmniejszeniu do szerokości $8\,\mathrm{cm}$ podpisy mogą stać się nieczytelne.

Dlatego grafikę warto obejrzeć również w takim rozmiarze, w jakim trafi do raportu lub prezentacji.

---

# Eksport

Typowy workflow:

~~~text
diagram.svg
    ↓
eksport
    ↓
diagram.pdf
diagram.png
~~~

SVG zachowujemy jako źródło edytowalne.

PDF może trafić do LaTeX-a.

PNG może być użyty na stronie WWW lub w prezentacji.

Nie warto zachowywać wyłącznie PNG, jeśli oryginalna grafika powstała jako wektor.

Po eksporcie otwórz **każdy** format. Sprawdź brakujące czcionki, ucięte podpisy, przezroczystość tła oraz to, czy tekst nadal można odczytać po wstawieniu do dokumentu. Plik PDF może wyglądać inaczej niż widok SVG w edytorze.

---

## Dobre materiały o Inkscape

- [Inkscape — Tutorials](https://inkscape.org/learn/tutorials/)
- [Inkscape — Learn](https://inkscape.org/learn/)
- [Inkscape Manual](https://inkscape-manuals.readthedocs.io/)

---

# Grafika naukowa ma przekazywać informację

Przed przygotowaniem rysunku warto odpowiedzieć:

1. Co odbiorca ma zrozumieć?
2. Który element jest najważniejszy?
3. Czy podpisy są czytelne?
4. Czy strzałki mają jednoznaczny sens?
5. Czy kolory są potrzebne?
6. Czy rysunek można zrozumieć bez ustnego komentarza?

Estetyka jest ważna, ale nie powinna utrudniać odczytania informacji.

## Wykres danych a ilustracja

Wykres powstaje z **określonych danych i sposobu ich przetworzenia**. Powinien mieć osie z nazwami wielkości i jednostkami, czytelną skalę, podpis oraz legendę, jeżeli pokazuje kilka serii. Jeśli niepewność pomiaru jest znana i ma znaczenie, warto ją pokazać, np. słupkami błędów.

Kolor może rozróżniać serie, ale nie powinien być jedyną wskazówką: użyj także różnych znaczników lub rodzajów linii. Sprawdź rysunek w skali docelowej oraz po wydrukowaniu w odcieniach szarości. Nie zmieniaj zakresu osi w sposób, który ukrywa ważny fragment danych lub wyolbrzymia różnicę bez wyjaśnienia.

Ilustracja koncepcyjna może objaśniać pomysł, ale nie jest zapisem pomiaru. W podpisie lub opisie projektu odróżnij ją od wykresu i wskaż jej pochodzenie.

---

# Wykres z kodu Pythona

Matplotlib rysuje wykres z wartości przekazanych przez program. Poniższe liczby są **syntetycznym przykładem**, a słupki błędów pokazują przyjętą niepewność odczytu:

~~~python
import matplotlib.pyplot as plt

czas_s = [0, 1, 2, 3, 4]
temperatura_C = [20.1, 22.0, 23.8, 26.2, 27.9]
niepewnosc_C = [0.3, 0.3, 0.4, 0.4, 0.5]
model_C = [20 + 2 * t for t in czas_s]

fig, ax = plt.subplots(figsize=(6, 4))
ax.errorbar(czas_s, temperatura_C, yerr=niepewnosc_C,
            fmt="o", capsize=3, label="dane przykładowe")
ax.plot(czas_s, model_C, "--", label="model liniowy")
ax.set_xlabel("Czas (s)")
ax.set_ylabel("Temperatura (°C)")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("temperatura.pdf")
fig.savefig("temperatura.png", dpi=200)
plt.close(fig)
~~~

Kod zapisuje dwa widoki tego samego rysunku. Wartości `yerr` są podane w jednostkach osi pionowej. Parametr `dpi` wpływa na raster PNG; PDF z liniami i tekstem może pozostać wektorowy. Obejrzyj oba pliki i sprawdź, czy legenda nie zasłania danych. Jeśli dane pochodzą z eksperymentu, opisz metodę pomiaru i znaczenie niepewności.

- [Matplotlib — wykres ze słupkami błędów](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html)
- [Matplotlib — zapisywanie grafiki](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html)

---

# AI i grafika

## Gdzie AI jest użyteczne?

Generatywne modele obrazu mogą dobrze sprawdzić się przy:

- ilustracjach koncepcyjnych,
- ikonach,
- grafice promocyjnej,
- wariantach stylistycznych,
- prostych infografikach,
- inspiracji wizualnej,
- edycji istniejących ilustracji.

---

## Ilustracja to nie wynik naukowy

AI nie powinno być traktowane jako źródło danych naukowych.

Jeżeli model wygeneruje wykres, mapę, zdjęcie aparatury albo strukturę techniczną, nie wolno zakładać, że szczegóły są poprawne tylko dlatego, że obraz wygląda realistycznie.

Bezpieczniejszy przykład:

~~~text
Wygeneruj minimalistyczną ilustrację
koncepcyjną pokazującą przepływ:
dane → analiza → wynik.
~~~

Ryzykowny przykład:

~~~text
Wygeneruj wykres wyników eksperymentu,
którego danych nie posiadamy.
~~~

Dane powinny wynikać z pomiaru, obliczenia albo jawnego modelu, a nie z preferencji generatora obrazu.

---

# Dobry prompt do obrazu

Prompt graficzny również może być specyfikacją.

Przykład:

~~~text
Cel:
ilustracja koncepcyjna do slajdu
o analizie danych.

Kompozycja:
laptop po lewej,
wykres liniowy po prawej,
między nimi jedna strzałka.

Styl:
minimalistyczna grafika,
jasne tło,
bez fotorealizmu.

Ograniczenia:
bez dodatkowego tekstu,
bez logo,
bez znaków wodnych,
bez liczb udających dane.

Format:
poziomy 16:9.
~~~

To dużo bardziej kontrolowane niż:

~~~text
zrób fajną grafikę o danych
~~~

---

# Iteracja i review grafiki AI

Typowy workflow:

~~~text
prompt
  ↓
obraz 1
  ↓
ocena
  ↓
konkretna poprawka
  ↓
obraz 2
  ↓
kontrola
~~~

Jeśli obraz AI jest częścią projektu, warto zachować:

~~~text
ai_prompt.md
ai_image.png
ai_review.md
~~~

W review zapisujemy:

- cel,
- mocne strony wyniku,
- błędy,
- wykonane poprawki,
- ocenę, czy obraz mógłby zostać pomylony z wynikiem naukowym.

---

# IrfanView

## Po co proste narzędzie?

Nie każda operacja wymaga rozbudowanego edytora.

Czasem chcemy tylko:

- sprawdzić wymiary,
- zmienić format,
- zmniejszyć rozdzielczość,
- przyciąć obraz,
- wykonać tę samą operację na wielu plikach.

Do takich zadań wygodny jest **IrfanView**.

---

## Skalowanie

Załóżmy, że mamy obraz:

~~~text
2400 × 1600 px
~~~

a potrzebujemy wersji o szerokości:

~~~text
1200 px
~~~

Przy zachowaniu proporcji wysokość wyniesie:

$$
1600\cdot\frac{1200}{2400}=800
$$

czyli:

~~~text
1200 × 800 px
~~~

---

## Konwersja

Zmiana nazwy:

~~~text
obraz.jpg → obraz.png
~~~

nie jest konwersją formatu.

Program musi rzeczywiście odczytać dane w jednym formacie i zapisać je w drugim.

---

## Operacje wsadowe

**Batch processing** oznacza wykonanie tej samej operacji na wielu plikach.

Przykład:

~~~text
image01.png
image02.png
image03.png
      ↓
zmniejsz do szerokości 800 px
      ↓
small_01.png
small_02.png
small_03.png
~~~

To bardzo praktyczne przy przygotowaniu wielu grafik do strony lub prezentacji.

---

## Dobre materiały o IrfanView

- [IrfanView](https://www.irfanview.com/)
- [IrfanView — FAQ](https://www.irfanview.com/faq.htm)

---

# TikZ

## Co to jest TikZ?

**TikZ** jest warstwą składniową pakietu PGF do tworzenia grafiki bezpośrednio w TeX-u.

Zamiast rysować diagram myszką, opisujemy go tekstowo.

Przykład:

~~~latex
\begin{tikzpicture}

\node (data) at (0,0) {Dane};
\node (analysis) at (3,0) {Analiza};
\node (result) at (6,0) {Wynik};

\draw[->] (data) -- (analysis);
\draw[->] (analysis) -- (result);

\end{tikzpicture}
~~~

Efekt logiczny:

~~~text
Dane → Analiza → Wynik
~~~

---

## Minimalny dokument TikZ

~~~latex
\documentclass{standalone}

\usepackage{tikz}

\begin{document}

\begin{tikzpicture}

\draw (0,0) circle (1);

\end{tikzpicture}

\end{document}
~~~

Po kompilacji otrzymamy mały PDF z okręgiem.

---

## Węzły

~~~latex
\node (A) at (0,0) {A};
\node (B) at (3,0) {B};

\draw[->] (A) -- (B);
~~~

Nazwy `A` i `B` pozwalają później odwoływać się do położenia węzłów.

---

## Style

Zamiast powtarzać wygląd każdego węzła, możemy zdefiniować styl.

~~~latex
\begin{tikzpicture}[
    box/.style={
        draw,
        rounded corners,
        minimum width=2.5cm,
        minimum height=1cm
    }
]

\node[box] (a) at (0,0) {Dane};
\node[box] (b) at (4,0) {Wynik};

\draw[->] (a) -- (b);

\end{tikzpicture}
~~~

Zmiana definicji `box` zmienia wszystkie węzły korzystające z tego stylu.

---

# TikZiT

**TikZ** jest językiem opisu rysunku. **TikZiT** jest programem z interfejsem graficznym, który zapisuje diagram jako **podzbiór kodu TikZ**. W TikZiT można przesuwać węzły myszą i łączyć je krawędziami, a wynikowy plik `.tikz` dołączyć do dokumentu LaTeX. Do złożenia końcowego PDF nadal potrzebny jest LaTeX.

Dobrze nadaje się do diagramów typu:

- węzły,
- krawędzie,
- połączenia,
- powtarzalne style.

| Pytanie | Sam TikZ | TikZiT |
| --- | --- | --- |
| Jak edytuję? | piszę polecenia w `.tex` | układam węzły i połączenia w edytorze |
| Zakres możliwości | pełna składnia TikZ | obsługiwany przez program podzbiór |
| Kiedy wybrać? | nietypowy rysunek, precyzyjne sterowanie kodem | szybkie układanie grafu lub schematu połączeń |

TikZiT może zapisać plik, który LaTeX rozumie, ale nie musi umieć ponownie otworzyć **dowolnego** ręcznie napisanego kodu TikZ. Jeśli używasz tego programu, zachowaj też plik stylów `.tikzstyles` i ewentualne pliki potrzebne do kompilacji. [Dokumentacja TikZiT](https://tikzit.github.io/) pokazuje sposób dołączenia rysunku do LaTeX-a.

Workflow:

~~~text
edycja wizualna
      ↓
kod TikZ
      ↓
LaTeX
      ↓
PDF
~~~

Materiały:

- [TikZiT](https://tikzit.github.io/)
- [PGF/TikZ na CTAN](https://ctan.org/pkg/pgf)

---

# Inkscape czy TikZ?

| Sytuacja | Dobry wybór |
| --- | --- |
| swobodny diagram z wieloma kształtami | Inkscape |
| logo lub ikona | Inkscape |
| diagram związany z matematyką | TikZ |
| grafika wersjonowana razem z kodem | TikZ |
| szybka ręczna korekta położenia | Inkscape |
| diagram węzły–krawędzie | TikZ / TikZiT |

TikZiT pomaga **edytować** wybrane diagramy TikZ; nie jest osobnym formatem gotowej grafiki. W Inkscape źródłem jest zwykle SVG, a w TikZ — kod rysunku. W obu przypadkach można uzyskać PDF do raportu.

---

# Hybrydowy workflow

Przykład:

~~~text
Python
  ↓
wykres PDF
  ↓
Inkscape
  ↓
dodanie strzałek i opisów
  ↓
final_figure.svg
  ↓
final_figure.pdf
  ↓
LaTeX
~~~

Podczas ręcznej edycji nie wolno zmieniać znaczenia danych.

Przesunięcie podpisu jest czymś innym niż przesunięcie punktu pomiarowego.

---

# Sprawdzenie przed oddaniem grafiki

- [ ] Plik źródłowy SVG, `.tex` lub kod wykresu jest w repozytorium.
- [ ] Wszystkie użyte obrazy wejściowe i dane mają podane pochodzenie.
- [ ] Wykres ma czytelne osie, jednostki, legendę i podpis.
- [ ] Tekst da się przeczytać w docelowym rozmiarze w raporcie lub na slajdzie.
- [ ] Eksportowane SVG, PNG i PDF otwierają się poprawnie.
- [ ] Przekształcenia obrazu nie zmieniły znaczenia danych.
- [ ] Ilustracja AI jest wyraźnie opisana jako ilustracja, jeśli została użyta.

[Zadania do tego wykładu](tasks/06_task_grafika_naukowa_uzytkowa.md) znajdują się w osobnym pliku, tak jak w poprzednich blokach kursu.

---
