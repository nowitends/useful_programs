# Kontrola paczki źródłowej raportu

Wybrany dokument: [raport.pdf](raport/raport.pdf). Pliki niezbędne do odtworzenia:

- [x] Plik główny: [raport/raport.tex](raport/raport.tex).
- [x] Bibliografia: [raport/references.bib](raport/references.bib).
- [x] Dane wejściowe: [raport/dane.csv](raport/dane.csv).
- [x] Kod generujący rysunek: [raport/generuj_wykres.py](raport/generuj_wykres.py).
- [x] Wygenerowana grafika do składu: [raport/wykres.pdf](raport/wykres.pdf).
- [x] Pliki klasy lub stylu: brak lokalnych; wymagane są standardowe pakiety MiKTeX widoczne w preambule.

Kompilator: `pdflatex`; bibliografia: `bibtex`. Python wymaga NumPy i Matplotlib. Z folderu `raport/` uruchom `python generuj_wykres.py`, `pdflatex raport.tex`, `bibtex raport`, a następnie dwa razy `pdflatex raport.tex`.

Próbę wykonałem w osobnym, pustym folderze, kopiując tylko cztery pliki źródłowe (`raport.tex`, `references.bib`, `dane.csv`, `generuj_wykres.py`). Po ponownym wygenerowaniu `wykres.pdf` i podanej sekwencji kompilacji otrzymano trzystronicowy PDF bez brakujących odwołań. Nie brakowało plików. Pliki tymczasowe (`.aux`, `.log`, `.bbl`, `.blg`, `.out`) nie są częścią paczki do archiwizacji.
