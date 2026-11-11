# IrfanView — praktyczna praca z obrazami

IrfanView jest lekką przeglądarką obrazów, ale ma także zestaw przydatnych narzędzi do **automatycznej obróbki wielu plików**. Dwie operacje szczególnie przydają się w codziennej pracy: przygotowanie dużej kolekcji zdjęć do publikacji i połączenie kilku części w jeden obraz.

**Zadania:** [IrfanView](tasks/01_task_irfanview.md) · **Pliki startowe:** [`files/irfanview/`](files/irfanview/)

## 1. Grafika rastrowa i jej rozdzielczość

Obraz rastrowy to siatka pikseli. Rozmiar `1200 × 800 px` oznacza szerokość 1200 pikseli i wysokość 800 pikseli. Zapis do `PNG` jest zwykle bezstratny, podczas gdy zapis do `JPEG` używa kompresji stratnej.

**Skalowanie do 50%** oznacza, że oba wymiary liniowe maleją o połowę; liczba pikseli staje się w przybliżeniu czterokrotnie mniejsza. Przykład:

| Etap | Szerokość | Wysokość |
| --- | ---: | ---: |
| Oryginał | 1200 | 800 |
| Skalowanie do 50% | 600 | 400 |
| Biała ramka 10 px z każdej strony | 620 | 420 |

Ramka jest dodawana **po skalowaniu**, dlatego powiększa wynikowy obraz o 20 pikseli w każdym wymiarze.

## 2. Odcienie szarości a obraz czarno-biały

- **Grayscale (odcienie szarości):** zachowuje wiele poziomów jasności. Dobre do zdjęć.
- **Black and white / 1-bit:** każdy piksel ma tylko dwie możliwe wartości, czarną albo białą. Przydaje się np. do niektórych skanów, ale może usunąć szczegóły zdjęcia.

W pierwszym ćwiczeniu używamy **grayscale**, czyli konwersji do odcieni szarości.

## 3. Batch Conversion — obróbka całego folderu

1. Otwórz IrfanView i wybierz **File → Batch Conversion/Rename**.
2. Jako źródło wskaż pliki z `files/irfanview/batch_input/` i dodaj je do listy (**Add All**).
3. Ustaw tryb **Batch conversion** oraz format wynikowy `PNG`.
4. Ustaw osobny **Output directory** — docelowy folder w swoim `pages/solutions/`.
5. Zaznacz **Use advanced options** i wejdź w **Advanced** / **Set advanced options**.
6. Włącz **Convert to greyscale** oraz **Resize** z wartością `50%` (z zachowaniem proporcji).
7. W części dotyczącej **Canvas size / Add border** ustaw białe marginesy po `10 px` z lewej, prawej, góry i dołu. Zadbaj o kolejność: najpierw resize, potem ramka.
8. Uruchom konwersję i porównaj obraz wejściowy z wynikowym.

Opcje nazywają się nieco inaczej w poszczególnych wydaniach programu. Jeśli domyślna kolejność operacji jest inna, skorzystaj z opcji własnej kolejności przetwarzania lub wykonaj dwa kolejne przebiegi wsadowe.

**Dlaczego nie nadpisujemy oryginałów?** Zmniejszenia rozdzielczości nie można później cofnąć bez utraty jakości. Zachowanie plików źródłowych ułatwia także sprawdzenie rezultatu.

## 4. Create Panorama — składanie fragmentów

Polecenie **Image → Create Panorama image** łączy obrazy pionowo albo poziomo. Nie jest to automatyczne dopasowywanie fotografii wykonanych z zakładką, lecz **zwykłe składanie obrazów obok siebie**.

W zadaniu mamy obraz rozcięty na cztery równe części:

```text
┌─────────────┬─────────────┐
│  top_left   │  top_right  │
├─────────────┼─────────────┤
│ bottom_left │ bottom_right│
└─────────────┴─────────────┘
```

Najpierw łączymy **pionowo** `top_left` z `bottom_left` (lewa kolumna). Potem **pionowo** `top_right` z `bottom_right` (prawa kolumna). Na końcu łączymy oba powstałe pliki **poziomo**.

Uwaga: gdy obrazy mają różne wymiary, IrfanView może je automatycznie przeskalować do wymiaru pierwszego obrazu w grupie. W tym zadaniu wymiary fragmentów zostały dobrane tak, aby tego uniknąć.

## 5. Co sprawdzamy?

- Czy student zna różnicę między pikselem, rozdzielczością a rozmiarem pliku?
- Czy umie użyć narzędzia **batch**, a nie obrabia obrazów pojedynczo?
- Czy rozumie różnicę między skalowaniem a dodawaniem płótna (ramki)?
- Czy zachowuje właściwą kolejność części podczas składania panoramy?

## Dokumentacja

- [IrfanView — Batch Conversion/Rename](https://www.irfanview.net/help/guida/hlp_batch_conversion.htm)
- [IrfanView — Create Panorama image](https://www.irfanview.net/help/guida/hlp_create_panorama.htm)
- [IrfanView — Canvas size / Add border](https://www.irfanview.net/help/guida/hlp_canvas_size.htm)
