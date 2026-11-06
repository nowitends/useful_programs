# Rozwiązania: LaTeX i dokumenty naukowe

Przykłady skompilowano lokalnie programem MiKTeX `pdflatex`; bibliografie przetworzono przez `bibtex`. Wykresy wygenerowano Pythonem z NumPy i Matplotlib. Źródła oraz PDF-y są w repozytorium, więc gotowy wygląd można porównać z kodem.

| Zadanie | Źródła i opis | Wynik |
| --- | --- | --- |
| 2. Miniartykuł | [raport.tex](raport/raport.tex), [CSV](raport/dane.csv), [skrypt](raport/generuj_wykres.py), [BibTeX](raport/references.bib), [instrukcja](raport/README.md) | [raport.pdf](raport/raport.pdf) |
| 3. CV postaci | [cv.tex](cv/cv.tex), [opis szablonu](cv/README.md) | [cv.pdf](cv/cv.pdf) |
| 4. Beamer | [prezentacja.tex](prezentacja/prezentacja.tex), [opis](prezentacja/README.md) | [prezentacja.pdf](prezentacja/prezentacja.pdf) |
| 5. Stylizacja | [stylizacja.tex](stylizacja/stylizacja.tex), [komentarz](stylizacja/README.md) | [stylizacja.pdf](stylizacja/stylizacja.pdf) |
| 6. Markdown i LaTeX | [fragment.md](porownanie/fragment.md), [fragment.tex](porownanie/fragment.tex), [uwagi](porownanie/uwagi.md) | [fragment.pdf](porownanie/fragment.pdf) |
| 7. Naprawa | [przed.tex](naprawa/przed.tex), [po.tex](naprawa/po.tex), [diagnoza](naprawa/diagnoza.md) | [po.pdf](naprawa/po.pdf) |
| 8. Wykres | [CSV](wykres/dane.csv), [skrypt](wykres/generuj_wykres.py), [nota.tex](wykres/nota.tex) | [wykres.pdf](wykres/wykres.pdf), [PNG](wykres/wykres.png), [nota.pdf](wykres/nota.pdf) |
| 9. Bibliografia | [bibliografia.tex](bibliografia/bibliografia.tex), [references.bib](bibliografia/references.bib), [kontrola](bibliografia/kontrola.md) | [bibliografia.pdf](bibliografia/bibliografia.pdf) |
| 10. Poradnik | [main.tex](poradnik/main.tex), [pliki sekcji](poradnik/README.md) | [poradnik.pdf](poradnik/poradnik.pdf) |
| 11. Recenzja CV | [ocena_cv.md](ocena_cv.md) | [CV do oceny](cv/cv.pdf) |
| 12. Paczka źródłowa | [kontrola_zrodel.md](kontrola_zrodel.md) | [raport.pdf](raport/raport.pdf) |

W zadaniu 3 użyto klasy ModernCV autorstwa Xaviera Danaux i opiekunów projektu, na licencji LPPL 1.3c. Pozostałe grafiki są generowane z danych ćwiczeniowych, a ilustracje zewnętrzne nie są osadzone. Raport i prezentacja wykorzystują dane **syntetyczne**, nie pomiary.

- [x] Źródła i wymagane PDF-y dla wszystkich dwunastu propozycji zapisane.
- [x] CV ma fikcyjny kontakt, a źródła są opisane.
- [x] Raport, slajdy i opowiadanie złożone w PDF.
- [ ] Po własnym Commit i Push sprawdzić linki w widoku forka na GitHubie.


# Zadania

Idea jest taka by wykonać całą pracę w Overleafie i na koniec przenieść wyniki pracy w odpowiednie miejsca na githubie (w toku).

1. Załóż konto na  https://www.overleaf.com (poza tym w domu (!) postyaraj się o lokalną instalację Latexa oraz instalację TexStudio lub zapewnienie możliwości pracy w VS Code).
2. Stwórz projekt `Start` z plikiem start.tex. Otwórz plik z md z listy zadań 01_Markdowna, który prezentował możliwości md. Teraz masz dokładnie te same elementy wyrazić za pomocą składni tex. Zadbaj o poprawne formatowanie i strukturę dokumentu oraz bezbłędność kompilacji.
3. Stwórz projekt `CV` z plikiem cv.tex. Używająć AI oraz galerii szablonów stwórz jakieś eleganckie CV fikcyjnej postaci z książek/filmów aplikujących o jakąś pracę.
4. Stwórz projekt `Publikacja`. Ściagnij z arxive artykuł https://arxiv.org/abs/1110.6812. Zmień autorów na postacie fikcyjne z fikcyjnego uniwersytetu!. Skompiluj dokument a nastepnie używając AI każ przeprowadzić audyt by znaleźć wszystkiue błedy jezykowe (zaznaczyć je kolorem niebiskim) i ulepszyć artykuł merytorycznie (stosując kolor czerwony). Postaraj się rozszerzyć artykuł o naalize numeryczną (a może rozwiązać analitycznie postawiony na końcu problem) i dopisać końcowy rozwdział. Kaz użyć koloru niebieskiego i czerwonego by zaznaczyć wszystkie poprawki w tekście oraz zielonego by wskazać fragmenty do usunięcia. 
5. Stwórz projekt `Prezentacja`. Wykonaj prezentację na 10 stron wybierając jeden z trzech tematów: fizyka, matematyka lub algorytmy. Użyj klasy `beamer` i stwórz slajdy z odpowiednią strukturą, listami, wzorami i grafikami. PRzentacja poziwnna miec boxy, frame title, przynajmniej jeden slajd z dwoma kolumnami, spis tresć (\tableofcontents), wzory, punktowane listy, wyliczalne listy.
6. Stwórz projekt `Praca domowa`. Weź jakąś listę zadań i wykonaj rozwiązanie w latexu.