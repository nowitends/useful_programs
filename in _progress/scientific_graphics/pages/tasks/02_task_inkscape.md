# Zadania: Inkscape — SVG

**Folder na rozwiązania:** [`pages/solutions/02_sol_inkscape/`](../solutions/02_sol_inkscape/).

W każdym zadaniu zachowaj edytowalny plik **SVG**. Sam obraz PNG ani zrzut ekranu **nie zastępuje** pliku SVG.

## Zadanie 1. Obiekty, style i transformacje

Otwórz Inkscape i stwórz własną kompozycję graficzną, np. abstrakcyjny schemat naukowy, wykorzystując co najmniej:

- 3 prostokąty (w tym jeden z zaokrąglonymi rogami),
- 3 elipsy lub okręgi,
- 1 wielokąt lub gwiazdę,
- 1 obiekt z wypełnieniem innym niż obrys,
- 1 obiekt częściowo przezroczysty,
- 1 obiekt obrócony o konkretny kąt (np. `30°` lub `45°`),
- 1 parę obiektów będących swoimi kopiami lub odbiciami.

Zastosuj co najmniej **3 różne kolory wypełnienia** i **2 różne grubości obrysu**. Zadbaj o czytelne rozmieszczenie obiektów.

Zapisz `objects.svg` oraz wyeksportuj `objects.png` do [`01_objects/`](../solutions/02_sol_inkscape/01_objects/).

## Zadanie 2. Sortowanie, Align & Distribute, grupowanie

Otwórz dostarczony plik [`arrange_start.svg`](../files/inkscape/arrange_start.svg). Zawiera 12 obiektów opisanych literami `A`, `B` i `C` oraz numerami `1–4`.

1. Ułóż elementy `A1–A4` w jednym poziomym rzędzie, `B1–B4` w drugim, a `C1–C4` w trzecim.
2. Wyrównaj każdy rząd **narzędziem Align** i rozłóż elementy w równych odstępach przez **Distribute** (nie tylko „na oko”).
3. Utwórz trzy grupy: po jednej dla każdego rzędu; nazwij je `A`, `B` i `C`.
4. Ustaw kolejność nakładania tak, aby podpisy były czytelne, a obiekty nie zasłaniały się przypadkowo.
5. Dodaj pod wszystkimi rzędami jasny prostokąt pełniący funkcję tła i przenieś go na sam dół (z-order).

Zapisz `arranged.svg` i `arranged.png` do [`02_arrange/`](../solutions/02_sol_inkscape/02_arrange/).

## Zadanie 3. Krzywe Béziera — szablon pierwszy

Otwórz **pierwszy plik SVG prowadzącego**, który zostanie umieszczony w [`files/inkscape/bezier_01/`](../files/inkscape/bezier_01/).

Plik zawiera gotowy wzór na **zablokowanej warstwie tła**. Nie odblokowuj jej i nie przesuwaj. Na osobnej warstwie `Rysunek` dorysuj wskazane kontury z wykorzystaniem **krzywych Béziera**. Zastosuj odpowiednie węzły i uchwyty, unikając zbędnej liczby węzłów.

Zapisz `bezier_01.svg` i jego eksport `bezier_01.png` do [`03_bezier_01/`](../solutions/02_sol_inkscape/03_bezier_01/).

**Uwaga:** właściwy plik szablonu zostanie dodany przez prowadzącego; nie zastępuj go przypadkowym obrazem.

## Zadanie 4. Krzywe Béziera — szablon drugi

Powtórz procedurę dla **drugiego pliku prowadzącego** z folderu [`files/inkscape/bezier_02/`](../files/inkscape/bezier_02/).

Odtwórz wymagane kształty na własnej warstwie, zachowując nienaruszone tło. Wykorzystaj tam, gdzie to potrzebne, domknięte ścieżki, wypełnienia i edycję uchwytów węzłów.

Zapisz `bezier_02.svg` i `bezier_02.png` do [`04_bezier_02/`](../solutions/02_sol_inkscape/04_bezier_02/).

## Zadanie 5. Bitmapa → ścieżka

Otwórz dostarczony [`trace_source.png`](../files/inkscape/trace_source.png), a następnie użyj **Path → Trace Bitmap**, aby otrzymać grafikę wektorową.

- Wybierz odpowiedni tryb śledzenia konturów.
- Usuń z wynikowego dokumentu źródłową bitmapę, pozostawiając rzeczywiste **ścieżki**.
- Popraw ewentualne błędy konturów i niepotrzebne węzły.
- Sprawdź, czy kształt wygląda poprawnie po znacznym powiększeniu.

Zapisz `traced.svg` oraz `traced.png` do [`05_trace_bitmap/`](../solutions/02_sol_inkscape/05_trace_bitmap/).

## Kontrola

Upewnij się, że można otworzyć wszystkie SVG w Inkscape, a szczególnie w zadaniach 3 i 4 **wzorzec pozostaje na osobnej zablokowanej warstwie**. Nie przesyłaj tylko wyeksportowanych PNG.
