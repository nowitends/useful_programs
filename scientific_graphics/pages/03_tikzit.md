# TikZiT — rysunki naukowe w dokumentach LaTeX

Podczas pisania notatek i artykułów w LaTeX-u często potrzeba prostych diagramów: połączeń między elementami, schematów przepływu, stanów układu lub kierunków oddziaływania. **TikZiT** jest graficznym edytorem takich diagramów, zapisującym je w formacie zgodnym z **PGF/TikZ**.

**Zadanie:** [TikZiT](tasks/03_task_tikzit.md) · **Materiały:** [`files/tikzit/lecture_template/`](files/tikzit/lecture_template/)

## 1. Dlaczego rysunek jako źródło, a nie zrzut ekranu?

Rysunki osadzane w LaTeX-u mogą zawierać tę samą typografię co tekst, skalować się bez utraty ostrości i pozostawać edytowalne. Zamiast wklejać zrzut ekranu do PDF-a, przechowujemy **kod rysunku**.

TikZiT zapisuje diagramy w plikach `.tikz`. Są one tekstem opartym na środowisku `tikzpicture`.

```latex
\begin{tikzpicture}
  \node[draw, circle] (a) at (0,0) {$A$};
  \node[draw, circle] (b) at (2,0) {$B$};
  \draw[->] (a) -- (b);
\end{tikzpicture}
```

W TikZiT podobny diagram można zbudować metodą wskazywania i klikania, bez wpisywania współrzędnych ręcznie.

## 2. Elementy środowiska TikZiT

- **Node** — węzeł (stan, obiekt, wielkość lub etap procesu).
- **Edge** — krawędź lub strzałka łącząca węzły.
- **Style** — zestaw parametrów określających wygląd węzła lub połączenia.
- **Label** — etykieta, np. symbol matematyczny `$F$`, `$E$` lub `$\Delta t$`.

Rysunki naukowe powinny przedstawiać **konkretne zależności**, a nie jedynie ozdabiać stronę.

## 3. Workflow z dokumentem LaTeX

1. Otwórz dostarczony projekt w edytorze LaTeX-a.
2. Przeczytaj fragment notatek i ustal, gdzie schemat faktycznie pomaga zrozumieć zagadnienie.
3. W TikZiT stwórz diagram i zapisz go jako `figures/01_*.tikz`.
4. Przenieś lub skopiuj rysunek do folderu `figures/` wewnątrz projektu LaTeX.
5. Dołącz go w pliku `.tex` poleceniem `\input{figures/01_*.tikz}` wewnątrz środowiska `figure`.
6. Skompiluj dokument i sprawdź czytelność diagramu oraz poprawność etykiet.

W dostarczonym projekcie jest plik `styles.tikzstyles` z przykładowymi stylami. Otwórz go jako paletę stylów w TikZiT i używaj tych samych stylów we wszystkich rysunkach.

Przykładowe osadzenie:

```latex
\begin{figure}[ht]
\centering
\input{figures/01_model.tikz}
\caption{Schemat połączeń w rozważanym modelu.}
\label{fig:model}
\end{figure}
```

W preambule dokumentu wystarczy odpowiednio skonfigurować pakiet `tikz` i definicje stylów; nie trzeba używać zrzutów ekranu. Oficjalna strona TikZiT opisuje również wariant z makrami `\tikzfig` i pakietem `tikzit.sty`.

## 4. Dobra ilustracja naukowa

Dobry diagram charakteryzują:

- niewielka liczba jasno wyodrębnionych elementów,
- czytelne etykiety symboliczne,
- jednoznaczny kierunek strzałek,
- spójny styl linii i obiektów,
- poprawność merytoryczna,
- możliwość ponownej edycji źródła.

Przykład: przepływ energii między trzema elementami można opisać trzema węzłami i dwiema skierowanymi krawędziami. Jeśli źródło przepływu i odbiornik są oznaczone odwrotnie, diagram może być estetyczny, ale jest niepoprawny.

## 5. Wymagania plikowe

Do repozytorium należy dodać **cały edytowalny projekt**: `main.tex`, plik stylów, źródła `.tikz` i wygenerowany `main.pdf`. PDF jest artefaktem końcowym, ale nie zastępuje plików źródłowych.

## Dokumentacja

- [TikZiT — strona i Quickstart](https://tikzit.github.io/)
- [TikZiT na GitHubie](https://github.com/tikzit/tikzit)
- [PGF/TikZ Manual](https://tikz.dev/)
