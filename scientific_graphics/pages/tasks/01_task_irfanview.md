# Zadania: IrfanView

**Folder na rozwiązania:** [`pages/solutions/01_sol_irfanview/`](../solutions/01_sol_irfanview/).

## Zadanie 1. Batch Conversion: obróbka całego folderu

W folderze [`pages/files/irfanview/batch_input/`](../files/irfanview/batch_input/) znajduje się zestaw obrazów. Wykorzystując **IrfanView → File → Batch Conversion/Rename**, przetwórz **wszystkie** pliki jednocześnie:

1. zamień na **odcienie szarości** (`grayscale`),
2. zmniejsz szerokość i wysokość do **50%** rozmiaru oryginału,
3. dodaj **białą ramkę 10 px z każdej strony**, po przeskalowaniu,
4. zapisz wynik w formacie PNG.

**Nie wolno** otwierać, edytować i zapisywać każdego pliku osobno. Nie modyfikuj obrazów źródłowych.

Wyniki umieść w folderze [`01_batch/`](../solutions/01_sol_irfanview/01_batch/). Zachowaj nazwy plików z folderu wejściowego i dodaj `batch_settings.png` (zrzut ekranu z ustawieniami zaawansowanymi IrfanView).

Sprawdź przykładowo, czy obraz o wymiarach `900 × 600 px` po obróbce ma rozmiar `470 × 320 px` (połowa wymiarów oraz po 10 px ramki z obu stron).

## Zadanie 2. Create Panorama — obraz z czterech fragmentów

W folderze [`pages/files/irfanview/panorama_tiles/`](../files/irfanview/panorama_tiles/) znajdują się cztery części jednego obrazu. Używaj polecenia **Image → Create Panorama image**.

1. Połącz `top_left.png` i `bottom_left.png` **pionowo**. Wynik zapisz jako `left.png`.
2. Połącz `top_right.png` i `bottom_right.png` **pionowo**. Wynik zapisz jako `right.png`.
3. Połącz `left.png` i `right.png` **poziomo**, tak aby powstał oryginalny obraz. Zapisz go jako `panorama.png`.

Wyniki umieść w folderze [`02_panorama/`](../solutions/01_sol_irfanview/02_panorama/).

**Wymagane trzy pliki:** `left.png`, `right.png`, `panorama.png`. Końcowy obraz powinien mieć właściwą kolejność i nie może zawierać pustych szczelin między fragmentami.

## Przed oddaniem

Sprawdź na GitHubie, czy oba foldery `01_batch/` i `02_panorama/` zawierają wszystkie wymagane pliki, a `panorama.png` da się wyświetlić w przeglądarce.
