# Scientific Graphics — Programy użytkowe

**Grafika naukowa i użytkowa: IrfanView, Inkscape, TikZiT i AI**

Praktyczny zestaw materiałów i zadań dotyczących obróbki zdjęć, tworzenia grafiki SVG, rysunków do LaTeX-a oraz edycji i generowania obrazów przy użyciu AI.

Repozytorium jest pomyślane jako kolejny moduł kursu [Programy użytkowe](https://github.com/RemigiuszDurka/useful_programs). Student wykonuje **fork**, pracuje w swoim repozytorium i umieszcza rezultaty w przygotowanych folderach `pages/solutions/`.

## Materiały i zadania

| Temat | Materiał wykładowy | Zadania | Rozwiązania |
| --- | --- | --- | --- |
| 1. IrfanView — grafika rastrowa | [01_irfanview.md](pages/01_irfanview.md) | [01_task_irfanview.md](pages/tasks/01_task_irfanview.md) | [01_sol_irfanview](pages/solutions/01_sol_irfanview/) |
| 2. Inkscape — grafika SVG | [02_inkscape.md](pages/02_inkscape.md) | [02_task_inkscape.md](pages/tasks/02_task_inkscape.md) | [02_sol_inkscape](pages/solutions/02_sol_inkscape/) |
| 3. TikZiT — grafika w LaTeX-u | [03_tikzit.md](pages/03_tikzit.md) | [03_task_tikzit.md](pages/tasks/03_task_tikzit.md) | [03_sol_tikzit](pages/solutions/03_sol_tikzit/) |
| 4. AI — grafika generatywna i edycja | [04_ai_graphics.md](pages/04_ai_graphics.md) | [04_task_ai_graphics.md](pages/tasks/04_task_ai_graphics.md) | [04_sol_ai](pages/solutions/04_sol_ai/) |

## Jak pracować

1. Wykonaj **Fork** repozytorium na swoim koncie GitHub. Nie zapisuj rozwiązań w repozytorium prowadzącego.
2. Zapoznaj się z materiałem `pages/XX_*.md`, a następnie wykonaj odpowiadające mu zadania w `pages/tasks/`.
3. Do każdego zadania użyj **wskazanego folderu** w `pages/solutions/`. Nie zmieniaj nazw folderów ani wymaganych plików.
4. Wyniki zapisuj w repozytorium przez **Commit & Push**. Sprawdź w widoku GitHub, czy pliki są obecne i dają się otworzyć.
5. Jeżeli otrzymasz uwagi przez GitHub Issues, popraw rozwiązanie i zatwierdź nową wersję.

**Zasada:** nie wystarczy efektowny obraz. Obraz musi spełniać wymagania zadania, a w przypadku grafiki naukowej również być poprawny merytorycznie.

## Struktura

```text
scientific_graphics/
├── README.md
├── INSTRUCTOR_TODO.md
├── pages/
│   ├── 01_irfanview.md
│   ├── 02_inkscape.md
│   ├── 03_tikzit.md
│   ├── 04_ai_graphics.md
│   ├── tasks/           # zadania dla studentów
│   ├── files/           # pliki startowe dostarczane przez prowadzącego
│   ├── examples/        # demonstracje, nie rozwiązania
│   └── solutions/       # foldery na wyniki w forkach studentów
└── tools/               # lokalny pomocniczy sprawdzacz struktury
```

W folderach `solutions/` pliki `.gitkeep` są jedynie technicznymi znacznikami utrzymującymi pusty folder w Git. Można je pozostawić.

## Pliki startowe i materiały, które będą dołączone później

Przykładowe dane do zadań IrfanView oraz do porządkowania i wektoryzacji w Inkscape są dołączone. Prowadzący doda **dwa własne szablony Béziera z zablokowanym tłem**, zdjęcie budynku DSF oraz materiały do ćwiczeń AI dotyczących sprawdzania prac i odręcznych notatek. Lista brakujących materiałów znajduje się w [INSTRUCTOR_TODO.md](INSTRUCTOR_TODO.md).

## Narzędzia

- [IrfanView](https://www.irfanview.com/) — operacje wsadowe, skalowanie i składanie obrazów.
- [Inkscape](https://inkscape.org/) — edytor grafiki wektorowej SVG.
- [TikZiT](https://tikzit.github.io/) — diagramy w formacie TikZ dla LaTeX-a.
- Dowolne narzędzie AI obsługujące **generowanie i edycję obrazu**, z zastrzeżeniem jego limitów oraz zasad prywatności.

Nie jest wymagane programowanie ani tworzenie animacji. Ćwiczenia koncentrują się na obsłudze narzędzi, pracy na plikach i jakości rezultatu.
