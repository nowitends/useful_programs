# Zadania: grafika naukowa i użytkowa

**Folder na rozwiązania:** [`pages/solutions/06_sol_grafika_naukowa_uzytkowa/`](../solutions/06_sol_grafika_naukowa_uzytkowa/) w swoim forku.

To zestaw propozycji do wyboru przez prowadzącego. Zadania 1–5 tworzą podstawowy projekt; zadania 6–8 pozwalają porównać narzędzia i rozszerzyć pracę. Oddawaj **źródła oraz eksporty**, aby rysunek można było obejrzeć na GitHubie i później poprawić. Nie zmieniaj plików przykładów kursu: zapisuj własne wyniki tylko w folderze rozwiązań.

## Zadanie 1. Indeks grafik w repozytorium

Utwórz `README.md` z tytułem, tabelą wykonanych zadań i względnymi linkami do każdego źródła i wyniku. Przy każdej grafice napisz jedno zdanie: co przedstawia i czy powstała z danych, z ręcznie narysowanych obiektów czy z generatora obrazów. Dodaj checklistę postępu. Po Commit i Push otwórz README na stronie swojego forka.

**Sprawdzenie:** linki działają, pliki są w repozytorium, a pochodzenie każdej grafiki jest jednoznaczne.

---

## Zadanie 2. Edytowalny schemat w Inkscape

Przygotuj schemat pracy z danymi: **Pytanie → Dane → Analiza → Wniosek**. Zapisz `schemat.svg` jako źródło oraz wyeksportuj `schemat.pdf` i `schemat.png`. PNG powinien mieć szerokość co najmniej `1200 px`.

Schemat ma zawierać cztery podpisane pola, trzy strzałki, wyrównane odstępy i jeden konsekwentny zestaw kolorów. Dodaj przynajmniej jeden element objaśniający, np. małą adnotację pod „Analizą”. Użyj grupowania i narzędzi wyrównania w Inkscape. Sprawdź, czy tekst pozostaje czytelny, gdy rysunek ma około 8 cm szerokości w raporcie.

**Sprawdzenie:** SVG jest edytowalne, PDF i PNG pokazują tę samą treść, PNG ma wymaganą szerokość, a tekst i strzałki nie są ucięte.

---

## Zadanie 3. Raster i zmiana rozmiaru wielu plików

Wykorzystaj trzy istniejące obrazy z repozytorium: [energia.png](../examples/01_markdown/files/sprezyna/energia.png), [schemat.png](../examples/01_markdown/files/sprezyna/schemat.png) i [rezonans.png](../examples/01_markdown/files/sprezyna/rezonans.png). Zmień ich szerokość na **800 px** przy zachowaniu proporcji. Możesz użyć operacji wsadowej w IrfanView albo powtarzalnego skryptu. Zapisz wyniki jako `batch/energia_800.png`, `batch/schemat_800.png` i `batch/rezonans_800.png`.

W `raster_report.md` umieść tabelę z nazwą każdego pliku, rozmiarem przed, rozmiarem po i współczynnikiem skalowania. Wyjaśnij, dlaczego samo przemianowanie `.jpg` na `.png` nie jest konwersją formatu oraz dlaczego powiększenie małego rastra nie odtwarza utraconych szczegółów. W README podaj nazwy obrazów źródłowych; nie trzeba ich kopiować drugi raz.

**Sprawdzenie:** wynikowe pliki mają szerokość 800 px; wysokości zachowują proporcje z dokładnością wynikającą z zaokrąglenia do całego piksela; tabela zgadza się z plikami.

---

## Zadanie 4. Wykres naukowy z danych

Utwórz `wykres/wahadlo.csv` z poniższymi **przykładowymi, syntetycznymi danymi**. Ostatnia kolumna oznacza przykładową niepewność okresu w sekundach.

~~~csv
dlugosc_m,okres_s,niepewnosc_s
0.20,0.90,0.04
0.40,1.27,0.04
0.60,1.55,0.05
0.80,1.80,0.05
1.00,2.01,0.06
~~~

Napisz `wykres/generuj_wykres.py` lub notebook `wykres/generuj_wykres.ipynb`, który czyta CSV, rysuje punkty ze słupkami błędów i na tym samym rysunku pokazuje krzywą modelu $T=2\pi\sqrt{L/g}$ dla $g=9{,}81\,\mathrm{m/s^2}$. Zapisz `wykres/wahadlo.pdf` i `wykres/wahadlo.png`. Osie mają podawać wielkość i jednostkę; serie mają różnić się nie tylko kolorem, ale również znacznikiem lub rodzajem linii. Dodaj legendę i krótki podpis w `wykres/README.md`. W podpisie nazwij dane syntetycznymi.

**Sprawdzenie:** kod odtwarza obie grafiki z CSV; punkty i słupki błędów odpowiadają danym; PDF zachowuje czytelność po powiększeniu, a PNG w docelowym rozmiarze.

---

## Zadanie 5. Ten sam schemat zapisany w TikZ

Napisz `tikz/schemat.tex` i skompiluj go do `tikz/schemat.pdf`. Przedstaw tę samą sekwencję czterech etapów co w zadaniu 2. Użyj `\node`, `\draw`, przynajmniej jednego własnego stylu węzła oraz czytelnych strzałek. Zadbaj, aby tekst mieścił się w polach.

W `tikz/README.md` zapisz użyty kompilator i jedno zdanie o tym, co łatwiej poprawia się w kodzie TikZ, a co w edytorze Inkscape. Nie wystarczy wstawić gotowego PNG do dokumentu `.tex`: schemat ma powstać z poleceń TikZ.

**Sprawdzenie:** źródło zawiera cztery węzły i trzy połączenia, kompiluje się z repozytorium, a PDF jest zgodny znaczeniowo ze schematem SVG.

---

## Zadanie 6. Diagram w TikZiT — propozycja dodatkowa

W TikZiT narysuj mały graf z **co najmniej czterema węzłami i czterema połączeniami**, np. dwie drogi prowadzące od „Danych” do „Wniosku”. Zapisz `tikzit/graf.tikz`, plik stylów `.tikzstyles` i `tikzit/graf.pdf` uzyskany po złożeniu w LaTeX-u. Dodaj główny plik `.tex` i ewentualny plik stylu wymagany przez projekt, tak aby dało się ponownie zbudować PDF.

W `tikzit/README.md` napisz, jaką rolę pełnią TikZ i TikZiT. Wskaż jedną rzecz, którą wygodnie zmieniałeś myszą, oraz jedną, którą łatwiej byłoby poprawić w kodzie.

**Sprawdzenie:** plik `.tikz` zawiera edytowalny diagram, wszystkie zależności są w repozytorium, a PDF odpowiada zapisanej wersji grafu.

## Zadanie 7. Ilustracja koncepcyjna z AI — propozycja dodatkowa

Przygotuj **ilustrację pomysłu** „od danych do wiedzy”, bez liczb i osi udających rzeczywiste wyniki. Zapisz `ai/ilustracja.png`, dokładną treść promptu w `ai/prompt.md` oraz `ai/ocena.md` z opisem celu, dwóch udanych elementów, dwóch poprawek i informacją, jak oznaczyłbyś obraz w raporcie. Jeśli wykonujesz kilka prób, zachowaj co najmniej pierwszą i ostatnią wersję. Nie używaj tego obrazu jako wykresu w zadaniu 4.

**Sprawdzenie:** prompt i przegląd zmian odpowiadają końcowemu obrazowi; grafika jest opisana jako ilustracja, bez sugestii, że przedstawia wynik pomiaru.

## Zadanie 8. Porównanie i kontrola końcowa

W `porownanie.md` zestaw `schemat.svg`, `tikz/schemat.tex` i `wykres/wahadlo.pdf`. Porównaj sposób edycji, możliwość odtworzenia i zastosowanie każdego pliku. Dodaj tabelę PNG–JPG–SVG–PDF z jednym rozsądnym zastosowaniem i jednym ograniczeniem każdego formatu. Wybierz najlepszy format do wstawienia schematu i wykresu do raportu LaTeX oraz uzasadnij wybór.

**Sprawdzenie:** porównanie odwołuje się do rzeczywistych prac z folderu, a podane zastosowania nie mylą źródła edytowalnego z końcowym obrazem.

---

# Checklista przed wysłaniem

- [ ] W README są działające linki do wykonanych prac.
- [ ] Źródła i eksporty są zapisane w forku, bez modyfikowania przykładów kursu.
- [ ] Każdy PDF i PNG został otwarty po ostatnim eksporcie.
- [ ] Wykres ma jednostki, podpis i informację o pochodzeniu danych.
- [ ] Pliki grafiki AI są jednoznacznie opisane, jeśli powstały.
- [ ] Po Commit i Push na GitHubie widać aktualną wersję plików.
