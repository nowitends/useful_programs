# LaTeX i dokumenty naukowe

W poprzednich wykładach pisaliśmy w Markdown, wykonywaliśmy obliczenia w Colabie i przechowywaliśmy pliki na GitHubie. Teraz przygotujemy dokument, którego **źródłem jest tekst**, a gotowym wynikiem — starannie złożony PDF. Tak pracuje się między innymi nad artykułami, raportami, pracami dyplomowymi, CV i prezentacjami.

LaTeX szczególnie pomaga wtedy, gdy dokument zawiera wiele wzorów, rysunków, tabel, cytowań i odwołań. Nie trzeba ręcznie aktualizować numerów po każdej zmianie. Nadal jednak to autor odpowiada za treść, poprawność danych i czytelność końcowego PDF.

---

# TeX, LaTeX, Overleaf i PDF

**TeX** jest systemem składu tekstu. **LaTeX** dodaje do niego wygodny język opisu struktury dokumentu. Zwykle edytujemy plik `.tex`, a kompilator tworzy z niego `.pdf`.

~~~text
raport.tex + bibliografia.bib + rysunki
                 ↓ kompilacja
              raport.pdf
~~~

**Overleaf** to edytor LaTeX-a w przeglądarce. **VS Code** może służyć do tej samej pracy lokalnie, jeśli na komputerze jest zainstalowana dystrybucja TeX, na przykład MiKTeX lub TeX Live. Edytor, kompilator i format pliku to trzy różne rzeczy.

Podobnie jak w poprzednich zadaniach, projekt przechowujemy w repozytorium GitHub. Warto zachować zarówno źródła, jak i wynikowy PDF: czytelnik może od razu obejrzeć dokument, a autor może go później poprawić i ponownie wygenerować.

## Markdown a LaTeX

| Pytanie | Markdown | LaTeX |
| --- | --- | --- |
| Co piszemy? | prosty tekst z lekkim formatowaniem | tekst z poleceniami opisującymi skład |
| Typowy plik | `.md` | `.tex` |
| Gdzie oglądamy wynik? | GitHub, Colab, podgląd edytora | najczęściej PDF |
| Mocna strona | szybka dokumentacja | precyzyjny skład większych dokumentów i matematyki |

Markdown nadal przyda się do `README.md` projektu. LaTeX będzie źródłem raportu lub prezentacji.

---

# Pierwszy dokument

Utwórz plik `pierwszy.tex`:

~~~latex
\documentclass[a4paper,11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[polish]{babel}
\usepackage{lmodern}

\title{Pierwszy dokument}
\author{Jan Kowalski}
\date{\today}

\begin{document}

\maketitle

\section{Cel}
Sprawdzam, jak powstaje dokument PDF z pliku źródłowego.

\section{Wynik}
To jest drugi akapit mojego dokumentu.

\end{document}
~~~

Zapisz plik w UTF-8. W Overleaf wybierz nowy pusty projekt, wklej kod i kliknij **Recompile**. Lokalnie, w terminalu otwartym w katalogu pliku, uruchom:

~~~bash
pdflatex pierwszy.tex
~~~

Powinien pojawić się `pierwszy.pdf`. W tym przykładzie `fontenc`, `babel` i `lmodern` zapewniają poprawny skład polskiego tekstu przy użyciu **pdfLaTeX-a**. Nowe instalacje LaTeX-a domyślnie rozumieją źródła UTF-8; w starszych instrukcjach można jeszcze spotkać `\usepackage[utf8]{inputenc}`. W gotowym szablonie sprawdź jego własne ustawienia czcionek i kompilatora, zanim dopiszesz te pakiety.

## Co jest czym?

- `\documentclass{article}` wybiera typ dokumentu.
- Polecenia `\usepackage{...}` ładują pakiety.
- Wszystko przed `\begin{document}` to **preambuła**: ustawienia, tytuł, autor i własne definicje.
- Między `\begin{document}` a `\end{document}` znajduje się treść.
- `\maketitle` wstawia tytuł w miejscu, w którym występuje.
- `\section{...}` tworzy numerowaną sekcję.

Klasy `article`, `report` i `book` służą do tekstów o różnej skali, a `beamer` — do slajdów. Nie każdy szablon używa `article`: CV może mieć własną klasę, na przykład `altacv` albo `moderncv`.

---

# Struktura i formatowanie

LaTeX automatycznie numeruje sekcje. Podsekcję tworzymy poleceniem `\subsection{...}`. W dłuższym dokumencie można dodać spis treści przez `\tableofcontents`; aby numery stron i odwołania się uzupełniły, czasem trzeba ponownie skompilować źródło.

~~~latex
\section{Wprowadzenie}
Krótki opis zagadnienia.

\subsection{Cel}
Pytanie, na które odpowiada dokument.
~~~

Nowy akapit zaczynamy po pustej linii. Pojedynczy Enter w źródle zwykle nie rozpoczyna nowego akapitu. Nie wyrównujemy tekstu spacjami ani wieloma poleceniami `\\`.

Podstawowe wyróżnienia:

~~~latex
\textbf{tekst pogrubiony}, \textit{tekst pochylony}
oraz \emph{fragment wymagający podkreślenia znaczenia}.
~~~

Listy zapisujemy w środowiskach:

~~~latex
\begin{itemize}
    \item źródło danych,
    \item metoda,
    \item wynik.
\end{itemize}

\begin{enumerate}
    \item Przygotuj dane.
    \item Wykonaj obliczenia.
    \item Sprawdź wynik.
\end{enumerate}
~~~

Listy pomagają porządkować informacje, ale raport naukowy potrzebuje też zdań objaśniających, co dane i wyniki znaczą.

## Znaki specjalne

Znaki `%`, `_`, `&`, `#`, `$`, `{`, `}` i `\` mają w źródle szczególną rolę. Gdy chcemy wyświetlić je jako zwykły tekst, używamy odpowiednich poleceń:

~~~latex
Wynik wzrósł o 5\%. Plik nazywa się dane\_pomiarowe.csv.
Zapisujemy A \& B, numer \#1 i cenę 10\$.
~~~

Znak `%` rozpoczyna komentarz aż do końca linii. Nieosłonięty `_` w zwykłym tekście często prowadzi do błędu `Missing $ inserted`. Dla dłuższych nazw plików lub adresów URL użyj `\verb|nazwa_pliku.tex|` albo pakietu `hyperref` i polecenia `\url{https://example.org}`.

---

# Matematyka w pliku `.tex`

Wzór w akapicie można zapisać między `$...$` albo `\(...\)`:

~~~latex
Dla promienia $r$ pole koła wynosi $P=\pi r^2$.
~~~

Wzór w osobnym wierszu, **bez numeru**, zapisujemy w LaTeX-u tak:

~~~latex
\[
P=\pi r^2.
\]
~~~

W notatkach **Markdown** na GitHubie do wzoru blokowego używamy `$$...$$`, zgodnie z [zasadami tego kursu](hints.md). W źródle **LaTeX** zalecanym odpowiednikiem jest `\[...\]`. Zapis zależy więc od rodzaju pliku, w którym pracujemy.

Jeżeli chcemy powołać się na numer równania, używamy środowiska `equation` i etykiety:

~~~latex
\begin{equation}
    T=2\pi\sqrt{\frac{L}{g}}.
    \label{eq:wahadlo}
\end{equation}

Z równania~\eqref{eq:wahadlo} wynika, że okres rośnie z długością.
~~~

Polecenie `\eqref` pochodzi z pakietu `amsmath` i dodaje nawiasy wokół numeru. Dla kilku wyrównanych równań też używamy `amsmath`:

~~~latex
\begin{align}
    y &= ax+b, \\
    a &= 2, \qquad b=1.
\end{align}
~~~

Znak `&` wskazuje miejsce wyrównania, a `\\` kończy wiersz. Gwiazdka w `align*` wyłącza numerację.

Macierz:

~~~latex
\[
A=\begin{pmatrix}
    2 & 1 \\
    1 & 3
\end{pmatrix}.
\]
~~~

Środowisko `pmatrix` również zapewnia pakiet `amsmath`.

---

# Tabele, rysunki i odwołania

W LaTeX-u tabela i rysunek mogą być **obiektami pływającymi**. Kompilator może przenieść je tam, gdzie lepiej mieszczą się na stronie. Opcja `[htbp]` podpowiada dopuszczalne miejsca, ale nie jest gwarancją dokładnej pozycji. Dlatego piszemy „w tabeli 1”, a nie „w tabeli poniżej”.

## Tabela

~~~latex
\begin{table}[htbp]
    \centering
    \begin{tabular}{r r}
        \hline
        Długość $L$ (m) & Okres $T$ (s) \\
        \hline
        0,20 & 0,90 \\
        0,40 & 1,27 \\
        0,60 & 1,55 \\
        \hline
    \end{tabular}
    \caption{Przykładowe pomiary wahadła.}
    \label{tab:pomiary}
\end{table}

W tabeli~\ref{tab:pomiary} zestawiono wyniki pomiarów.
~~~

Podpis wyjaśnia, co przedstawia tabela; nazwy kolumn zawierają jednostki. Etykietę umieszczamy **po** `\caption`, aby otrzymać poprawny numer.

## Rysunek

Do wstawiania grafik potrzebny jest pakiet `graphicx` w preambule:

~~~latex
\usepackage{graphicx}
~~~

Jeżeli w katalogu projektu znajduje się `wykres.pdf`, w treści wpisujemy:

~~~latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth]{wykres.pdf}
    \caption{Okres wahadła w funkcji jego długości.}
    \label{fig:okres}
\end{figure}

Na rysunku~\ref{fig:okres} widać wzrost okresu.
~~~

Ścieżka do grafiki musi odpowiadać rzeczywistemu położeniu pliku względem głównego pliku `.tex`. Dla pliku `figures/wykres.pdf` wpisz `\includegraphics{figures/wykres.pdf}`. Do projektu GitHub dodaj również samą grafikę, inaczej ktoś inny nie odtworzy PDF.

| Format | Zastosowanie |
| --- | --- |
| PNG | zrzuty ekranu, obrazy rastrowe |
| JPG | fotografie |
| PDF | wykresy i diagramy wektorowe, jeżeli eksport zachowuje wektory |
| SVG | grafika wektorowa do WWW; dla typowego `pdflatex` zwykle trzeba ją najpierw przekonwertować |

Przykład zapisu wykresu z Matplotlib:

~~~python
plt.xlabel("Długość L (m)")
plt.ylabel("Okres T (s)")
plt.savefig("wykres.pdf", bbox_inches="tight")
~~~

Nie każdy PDF zawiera grafikę wektorową: fotografia wklejona do PDF nadal pozostaje obrazem rastrowym.

## Dobre etykiety

Stosuj czytelne prefiksy: `eq:wahadlo`, `fig:okres`, `tab:pomiary`, `sec:metoda`. W tekście używaj `\ref{...}` albo `\eqref{...}` zamiast wpisywać numery ręcznie. Po zmianie dokumentu skompiluj go ponownie i sprawdź, czy zamiast numerów nie pojawia się `??`.

---

# Bibliografia: plik `.bib` i cytowania

Bibliografia pozwala wskazać źródło modelu, danych, definicji lub programu. Każda pozycja ma **klucz**, którego używamy w dokumencie. W pliku `references.bib` można zapisać na przykład:

~~~bibtex
@book{lamport1994,
    author    = {Leslie Lamport},
    title     = {LaTeX: A Document Preparation System},
    publisher = {Addison-Wesley},
    year      = {1994},
    edition   = {2}
}
~~~

W `report.tex`:

~~~latex
Opis składni LaTeX-a można znaleźć w książce~\cite{lamport1994}.

\bibliographystyle{plain}
\bibliography{references}
~~~

`\bibliography{references}` wskazuje plik `references.bib`, ale bez rozszerzenia. Nazwa w `\cite{...}` musi dokładnie odpowiadać kluczowi w `.bib`.

Do nauki wystarczy klasyczny **BibTeX**. W większych projektach można spotkać również `biblatex` i program `biber`; to inny sposób konfiguracji bibliografii. Nie mieszamy obu sposobów bez potrzeby.

## Skąd wziąć poprawne dane?

Opis publikacji można pobrać od wydawcy, z katalogu bibliotecznego albo przez DOI. Sprawdź ręcznie autora, tytuł, rok i identyfikator. AI może pomóc uporządkować wpis, ale potrafi wymyślić nieistniejące źródło. Cytowanie musi prowadzić do rzeczywistej pozycji, którą da się odnaleźć.

## Kolejność kompilacji

Dla `report.tex` i `references.bib` klasyczna sekwencja wygląda tak:

~~~bash
pdflatex report.tex
bibtex report
pdflatex report.tex
pdflatex report.tex
~~~

Po pierwszym przebiegu powstają pliki pomocnicze; BibTeX przygotowuje bibliografię; kolejne przebiegi uzupełniają cytowania i odwołania. Narzędzie `latexmk` zwykle wykonuje potrzebne kroki automatycznie:

~~~bash
latexmk -pdf report.tex
~~~

W Overleaf przycisk **Recompile** obsługuje typowy projekt z BibTeX-em. Jeżeli cytowania pozostają puste, zajrzyj do logu i sprawdź nazwę pliku `.bib` oraz klucze.

---

# Overleaf, VS Code i GitHub: pełny cykl pracy

1. Utwórz folder projektu i plik główny `.tex`.
2. Dodaj używane pliki `.bib`, grafiki oraz ewentualne pliki szablonu `.cls` i `.sty`.
3. Kompiluj w Overleaf lub lokalnie. Szablon może wymagać konkretnego kompilatora: **pdfLaTeX**, **XeLaTeX** albo **LuaLaTeX**.
4. Otwórz PDF i sprawdź wszystkie strony, nie tylko pierwszą.
5. Wyślij źródła i końcowy PDF do swojego forka przez Commit i Push.
6. Otwórz repozytorium na GitHubie i sprawdź, czy pliki są dostępne oraz czy ścieżki w `README.md` działają.

Przykładowy folder:

~~~text
projekt/
├── README.md
├── report.tex
├── references.bib
├── figures/
│   └── wykres.pdf
└── report.pdf
~~~

`README.md` wyjaśnia, jaki dokument powstał, jak go skompilować i skąd pochodzą dane oraz użyty szablon. **PDF nie zastępuje źródeł**. Z kolei same źródła bez PDF utrudniają szybkie obejrzenie efektu na GitHubie.

Pliki pomocnicze kompilacji, np. `.aux`, `.log`, `.out` czy `.synctex.gz`, nie są częścią oddawanego dokumentu. Jeśli pracujesz lokalnie, możesz je pominąć w commicie. W repozytorium z wieloma dokumentami rób to rozważnie, aby przypadkiem nie wykluczyć gotowych plików `.pdf`.

## Co zrobić, gdy kompilacja się nie udaje?

Najpierw znajdź **pierwszy istotny błąd** w logu; późniejsze komunikaty bywają jego skutkiem. Sprawdź:

- czy wszystkie `{` mają odpowiadające `}` i wszystkie środowiska mają `\end{...}`,
- czy nazwy plików i wielkość liter w ścieżkach się zgadzają,
- czy używany pakiet jest dostępny,
- czy specjalny znak nie trafił do zwykłego tekstu bez osłony,
- czy kompilator zgadza się z wymaganiami szablonu,
- czy cytowania i etykiety są zapisane identycznie w obu miejscach.

Overleaf i lokalna instalacja mogą mieć różne wersje pakietów. Jeżeli jeden projekt kompiluje się tylko w jednym z tych środowisk, zapisz w `README.md`, którego użyto i co trzeba zainstalować lub ustawić.

W Overleaf kilka osób może edytować ten sam projekt. Uzgodnijcie, kto odpowiada za tekst, wykresy i bibliografię, a po większej zmianie sprawdźcie PDF. Historia zmian projektu w Overleaf i historia commitów w GitHubie mają różne cele; gotową wersję nadal warto zapisać w repozytorium razem ze źródłami.

---

# Większy dokument

Dłuższy raport można podzielić na pliki:

~~~text
praca/
├── main.tex
├── references.bib
├── chapters/
│   ├── wstep.tex
│   ├── metoda.tex
│   └── wyniki.tex
└── figures/
    └── wykres.pdf
~~~

W `main.tex` umieszczamy:

~~~latex
\input{chapters/wstep}
\input{chapters/metoda}
\input{chapters/wyniki}
~~~

Kompilujemy **główny** plik, a nie każdy rozdział osobno. W pracy dyplomowej dochodzą jeszcze wymagania uczelni dotyczące struktury, strony tytułowej i sposobu cytowania. Wybór szablonu nigdy nie zwalnia z ich sprawdzenia.

## Preprint i paczka źródłowa

**Preprint** to publicznie udostępniony tekst naukowy, który może poprzedzać publikację w czasopiśmie. [arXiv](https://info.arxiv.org/help/) jest przykładem serwisu służącego do udostępniania takich prac. Samo umieszczenie tekstu w repozytorium preprintów nie jest równoznaczne z recenzją czasopisma.

Przed przekazaniem artykułu innej osobie albo do systemu publikacyjnego sprawdź, czy paczka zawiera główny `.tex`, wszystkie dołączane pliki, bibliografię, grafiki i potrzebne pliki stylu. Usuń pliki testowe, prywatne komentarze oraz dane, których nie należy upubliczniać. Na tych zajęciach ćwiczymy **przygotowanie paczki**, bez wysyłania pracy do arXiv.

---

# CV w LaTeX-u

CV musi być łatwe do przeczytania: ważniejsze są hierarchia informacji, czytelna czcionka i konkretna treść niż liczba ozdobników. LaTeX pozwala przygotować taki sam układ dla kolejnych wersji i zachować jego źródło w Git.

Na ćwiczeniach stworzymy **fikcyjne CV postaci literackiej** aplikującej o wybrane stanowisko. Dzięki temu można ćwiczyć formę profesjonalnego CV bez publikowania własnych danych osobowych. Żart może być widoczny w doborze postaci i doświadczenia, ale dokument nadal powinien mieć stanowisko docelowe, profil zawodowy, doświadczenie lub projekty, umiejętności oraz spójny kontakt do fikcyjnej osoby. Fakty z utworu warto odróżnić od twórczego dopowiedzenia.

Dobrym punktem startowym jest [AltaCV Template](https://www.overleaf.com/latex/templates/altacv-template/trgqjpwnmtgv): czytelny układ z boczną kolumną, oficjalna strona szablonu podaje autora i licencję LPPL 1.3c. Spokojniejszą alternatywą jest [ModernCV and Cover Letter Template](https://www.overleaf.com/latex/templates/moderncv-and-cover-letter-template/sttkgjcysttn). Przed wyborem obejrzyj PDF szablonu, sprawdź, czy polski tekst mieści się w kolumnach, oraz czy cały projekt — w tym pliki klasy — da się zapisać w repozytorium. Oceniamy także jakość **wyboru i dostosowania** szablonu, nie sam fakt jego użycia.

---

# Prezentacja w Beamerze

Klasa `beamer` tworzy PDF złożony ze slajdów. Każde środowisko `frame` to jeden slajd. Przykład można skompilować bez zewnętrznych grafik:

~~~latex
\documentclass[aspectratio=169]{beamer}
\usepackage[T1]{fontenc}
\usepackage[polish]{babel}
\usepackage{lmodern}

\title{Czy wykres może wprowadzać w błąd?}
\author{Jan Kowalski}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Pytanie}
    Co zmienia się, gdy oś wykresu nie zaczyna się od zera?
    \begin{itemize}
        \item wielkość różnicy w danych pozostaje taka sama,
        \item wizualne wrażenie może się zmienić.
    \end{itemize}
\end{frame}

\begin{frame}{Wniosek}
    Sprawdzaj skalę osi, jednostki i źródło danych.
\end{frame}

\end{document}
~~~

Przy większej prezentacji można użyć `\begin{columns}...\end{columns}`, bloków `block`, tabel, wzorów i grafik. Na slajdzie tekst powinien być widoczny z dalszej części sali. Jeden slajd zwykle niesie jedną główną myśl, a podpis wykresu powinien objaśniać, co pokazuje.

Jeżeli chcesz zmienić wygląd, obejrzyj [Metropolis Beamer Theme](https://www.overleaf.com/latex/templates/metropolis-beamer-theme/qzyvdhrntfmr). Sprawdź wymagane pakiety i kompilator przed przejęciem motywu. Prosty motyw, konsekwentne kolory i dobre wykresy często dają lepszy rezultat niż rozbudowane animacje.

---

# Krótki kompletny raport

Poniższy przykład składa się z **dwóch plików w tym samym folderze**. Nie wymaga zewnętrznej grafiki. Pokazuje tytuł, sekcje, wzór, tabelę, odwołania i cytowanie. Można go wkleić do pustego projektu Overleaf albo skompilować lokalnie podanymi wcześniej poleceniami.

`report.tex`:

~~~latex
\documentclass[a4paper,11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[polish]{babel}
\usepackage{lmodern}
\usepackage{amsmath}

\title{Krótka notatka o wahadle}
\author{Jan Kowalski}
\date{\today}

\begin{document}
\maketitle

\section{Cel}
Sprawdzamy, jak okres drgań zależy od długości wahadła.
Opis przygotowania dokumentu w LaTeX-u podaje\cite{lamport1994}.

\section{Model}
Dla małych wychyleń przyjmujemy model
\begin{equation}
    T=2\pi\sqrt{\frac{L}{g}},
    \label{eq:okres}
\end{equation}
gdzie $L$ jest długością w metrach, a $g$ przyspieszeniem
ziemskim w metrach na sekundę do kwadratu.

\section{Dane}
\begin{table}[htbp]
    \centering
    \begin{tabular}{r r}
        \hline
        $L$ (m) & $T$ (s) \\
        \hline
        0,20 & 0,90 \\
        0,40 & 1,27 \\
        0,60 & 1,55 \\
        \hline
    \end{tabular}
    \caption{Przykładowe okresy dla trzech długości.}
    \label{tab:okresy}
\end{table}

Z równania~\eqref{eq:okres} i tabeli~\ref{tab:okresy}
wynika, że dłuższe wahadło drga wolniej.

\bibliographystyle{plain}
\bibliography{references}
\end{document}
~~~

`references.bib`:

~~~bibtex
@book{lamport1994,
    author    = {Leslie Lamport},
    title     = {LaTeX: A Document Preparation System},
    publisher = {Addison-Wesley},
    year      = {1994},
    edition   = {2}
}
~~~

Ten raport jest przykładem składni, nie pełną analizą naukową. W rzeczywistym raporcie trzeba opisać pochodzenie danych, metodę ich zebrania, ograniczenia modelu i źródła merytoryczne. Sam fakt, że dokument wygląda profesjonalnie, nie dowodzi poprawności wyniku.

---

# Sprawdzenie przed oddaniem

- [ ] Źródła `.tex`, `.bib` i wszystkie użyte grafiki są w repozytorium.
- [ ] Dokument kompiluje się od początku w opisanym środowisku.
- [ ] PDF otwiera się i wszystkie strony są czytelne.
- [ ] Nie ma `??`, brakujących cytowań ani komunikatów o brakujących plikach.
- [ ] Rysunki i tabele mają podpisy, jednostki i odwołania z tekstu.
- [ ] `README.md` podaje sposób kompilacji, pochodzenie danych i szablonu.
- [ ] Projekt nie zawiera prywatnych danych ani przypadkowych plików pomocniczych.

[Zadania do tego wykładu](tasks/05_task_latex_dokumenty_naukowe.md) są zapisane osobno, podobnie jak w poprzednich blokach kursu.

## Dobre materiały

- [Krótkie wprowadzenie do LaTeX-a po polsku](https://tug.ctan.org/info/lshort/polish/lshort-pl.pdf)
- [Overleaf — Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
- [Overleaf — Mathematical expressions](https://www.overleaf.com/learn/latex/Mathematical_expressions)
- [Overleaf — Bibliography management with BibTeX](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex)
- [Overleaf — Inserting images](https://www.overleaf.com/learn/latex/Inserting_Images)
