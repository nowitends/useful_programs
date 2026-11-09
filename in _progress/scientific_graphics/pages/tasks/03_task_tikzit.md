# Zadanie: TikZiT i LaTeX

**Folder na rozwiązania:** [`pages/solutions/03_sol_tikzit/`](../solutions/03_sol_tikzit/).

## Zadanie 1. Uzupełnienie notatek wykładowych o rysunki

Otwórz [projekt startowy LaTeX](../files/tikzit/lecture_template/) i zapoznaj się z treścią `main.tex`. Dokument zawiera trzy miejsca, w których brakuje ilustracji.

Korzystając z **TikZiT**, wykonaj **trzy osobne diagramy naukowe** zgodne z tematem notatek, a następnie umieść je we właściwych miejscach w dokumencie.

Wymagania:

1. Diagramy zbuduj w TikZiT z węzłów, krawędzi i etykiet.
2. Każdy diagram zapisz w **oddzielnym pliku `.tikz`** wewnątrz folderu `figures/`.
3. Użyj spójnej palety stylów (`styles.tikzstyles`).
4. Umieść rysunki w `main.tex` jako odwołania do plików `.tikz`, **nie jako wklejone obrazy rastrowe**.
5. Zachowaj podpisy i odwołania do rysunków w tekście. Wygeneruj wynikowy `main.pdf`.
6. Sprawdź, czy diagramy są poprawne merytorycznie, a tekst i symbole nie nakładają się na siebie.

Do folderu `pages/solutions/03_sol_tikzit/` dodaj cały projekt:

```text
03_sol_tikzit/
├── main.tex
├── main.pdf
├── styles.tikzstyles
└── figures/
    ├── 01_energy_flow.tikz
    ├── 02_stable_equilibrium.tikz
    └── 03_measurement_chain.tikz
```

Wynikowy PDF powinien zawierać trzy czytelne schematy i dać się otworzyć bez dodatkowych plików. Równocześnie wszystkie źródła muszą pozostać w repozytorium.

**Uwaga dla prowadzącego:** startowy dokument jest przykładem możliwym do zastąpienia docelowymi notatkami. Jeśli zostanie podmieniony, należy dostosować tematykę i nazwy ilustracji w tym zadaniu.
