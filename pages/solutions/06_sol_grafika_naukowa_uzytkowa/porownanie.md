# Porównanie sposobów tworzenia grafiki

| Plik | Edycja | Odtworzenie | Zastosowanie |
| --- | --- | --- | --- |
| [schemat.svg](schemat.svg) | Obiekty wektorowe, tekst i warstwy można przesuwać w Inkscape. | Źródłem jest sam plik SVG; eksport do [PDF](schemat.pdf) i [PNG](schemat.png) wykonał Inkscape. | Diagram procesu na stronie lub w raporcie. |
| [tikz/schemat.tex](tikz/schemat.tex) | Pozycje, style i etykiety zmienia się w kodzie. | `pdflatex schemat.tex` tworzy [PDF](tikz/schemat.pdf). | Diagram zintegrowany z projektem LaTeX. |
| [wykres/wahadlo.pdf](wykres/wahadlo.pdf) | Sam PDF jest eksportem; zmiany danych lub skali należy zrobić w [CSV](wykres/wahadlo.csv) i [skrypcie](wykres/generuj_wykres.py). | `python generuj_wykres.py` tworzy PDF i [PNG](wykres/wahadlo.png). | Rysunek naukowy z osią, jednostką i niepewnościami. |

Schemat SVG i diagram TikZ przedstawiają tę samą kolejność etapów. Pierwszy łatwiej dostroić wizualnie, drugi powtarzalnie zmienić dla wielu podobnych rysunków. Wykres ma inną rolę: pokazuje dane syntetyczne i model, dlatego jego właściwym źródłem są CSV i kod, a nie ręczna edycja krzywej.

| Format | Rozsądne zastosowanie | Ograniczenie |
| --- | --- | --- |
| PNG | Zrzut ekranu lub podgląd na GitHubie. | Piksele stają się widoczne przy dużym powiększeniu. |
| JPG | Fotografia o wielu odcieniach. | Stratna kompresja może rozmyć cienkie linie i tekst. |
| SVG | Edytowalny schemat z kształtów i tekstu. | Nie każdy program składający PDF obsługuje SVG bez konwersji. |
| PDF | Wektorowy wykres lub schemat w raporcie LaTeX. | Eksport PDF zwykle nie jest najwygodniejszym źródłem do zmiany danych. |

Do raportu LaTeX wstawiłbym [schemat.pdf](schemat.pdf) i [wykres/wahadlo.pdf](wykres/wahadlo.pdf): zachowują ostrość linii i tekstu. Edytowalne źródła (`schemat.svg`, pliki TikZ, CSV i Python) archiwizowałbym obok PDF-ów.
