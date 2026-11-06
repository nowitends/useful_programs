# Ten sam fragment w dwóch zapisach

| Element | Markdown | LaTeX |
| --- | --- | --- |
| Tytuł | `# Okres wahadła` | `\title{...}` i `\maketitle` |
| Sekcja | `## Model` | `\section{Model}` |
| Lista | wiersz zaczynający się od `-` | `\begin{itemize}`, `\item`, `\end{itemize}` |
| Tabela | wiersze rozdzielane `\|` | `tabular` i `&` między kolumnami |
| Wzór w tekście | `$L$` | `$L$` |
| Wzór w bloku | `$$...$$` | `\[...\]` |

W plikach `.md` tego kursu `$$...$$` jest rozpoznawane przez renderer matematyki GitHuba. W zwykłym dokumencie `.tex` używamy `\[...\]`, czyli standardowego polecenia LaTeX do nienumerowanego wzoru wyświetlanego. Oba zapisy mogą wyglądać podobnie po renderowaniu, ale przetwarzają je inne narzędzia. [Fragment Markdown](fragment.md), [źródło LaTeX](fragment.tex), [PDF](fragment.pdf).
