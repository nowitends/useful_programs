# Miniartykuł o wahadle

[raport.tex](raport.tex) składa się do [raport.pdf](raport.pdf), a [dane.csv](dane.csv) są wejściem [generuj_wykres.py](generuj_wykres.py). Źródła bibliograficzne są w [references.bib](references.bib). Liczby w CSV są **przykładowe**, bez protokołu pomiarowego.

Z tego folderu uruchom:

~~~text
python generuj_wykres.py
pdflatex raport.tex
bibtex raport
pdflatex raport.tex
pdflatex raport.tex
~~~

Potrzebne są Python z NumPy i Matplotlib oraz dystrybucja LaTeX z pakietami wymienionymi w preambule. Skrypt tworzy [wykres.pdf](wykres.pdf) i [wykres.png](wykres.png). Wynikowy artykuł ma trzy strony A4.
