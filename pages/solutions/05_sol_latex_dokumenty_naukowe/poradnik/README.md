# Poradnik z plików składowych

Plik główny to [main.tex](main.tex). Wczytuje [wstep.tex](sections/wstep.tex) i [procedura.tex](sections/procedura.tex) przez `\input`. Wynik: [poradnik.pdf](poradnik.pdf).

Z tego katalogu uruchom `pdflatex -jobname=poradnik main.tex` dwa razy, aby otrzymać `poradnik.pdf` z aktualnym spisem treści i numerami odwołań. Użyto MiKTeX `pdflatex` i standardowych pakietów widocznych w preambule.
