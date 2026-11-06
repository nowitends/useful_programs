# Diagnoza

| Błąd w [przed.tex](przed.tex) | Poprawka w [po.tex](po.tex) |
| --- | --- |
| `\section{Wyniki` nie zamyka argumentu, więc dalszy tekst jest wciągany do nagłówka. | Zamknąłem nawias: `\section{Wyniki}`. |
| Podkreślnik w nazwie `dane_wynikowe.csv` ma w LaTeX-u specjalne znaczenie. | Zapisałem `\texttt{dane\_wynikowe.csv}`. |
| Środowisko `itemize` nie ma `\end{itemize}`. | Zamknąłem listę przed następnym akapitem. |
| Znak `%` rozpoczyna komentarz, więc reszta wiersza znika. | Zapisałem `5\%`. |
| Brak ustawień języka i kodowania fontu utrudnia poprawny skład polskich znaków. | Dodałem `babel` z językiem polskim, `fontenc` T1 i `lmodern`. |

Skompilowany wynik: [po.pdf](po.pdf). Plik błędny pozostaje celowo bez PDF.
