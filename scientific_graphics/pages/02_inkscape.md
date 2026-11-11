# Inkscape — obiekty, SVG i krzywe Béziera

Inkscape służy do edycji **grafiki wektorowej**. Obraz nie jest tu wyłącznie tablicą pikseli: tworzą go obiekty geometryczne, ścieżki, kolory, obrysy i relacje między elementami. Dzięki temu diagram można powiększać, reorganizować i edytować bez utraty ostrości.

**Zadania:** [Inkscape](tasks/02_task_inkscape.md) · **Pliki:** [`files/inkscape/`](files/inkscape/)

## 1. SVG — plik, a nie zrzut ekranu

`SVG` (Scalable Vector Graphics) jest tekstowym formatem grafiki wektorowej opartym na XML. Przechowuje kształty, warstwy i parametry ich wyglądu. Zapisany plik SVG można ponownie otworzyć i edytować w Inkscape. Wyeksportowany PNG to już tylko wynik rastrowy.

Przykład fragmentu SVG:

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="160" height="80">
  <rect x="10" y="10" width="140" height="60"
        rx="12" fill="#3b82f6" stroke="#14213d" stroke-width="4"/>
</svg>
```

W Inkscape nie trzeba pisać tego kodu samodzielnie — edytor zapisuje go automatycznie.

## 2. Podstawowe obiekty i ich wygląd

Najczęściej używane narzędzia: **Rectangle**, **Ellipse**, **Star/Polygon**, **Bezier/Pen** oraz **Text**.

| Własność | Znaczenie |
| --- | --- |
| `Fill` | kolor lub sposób wypełnienia wnętrza |
| `Stroke paint` | kolor obrysu |
| `Stroke style` | szerokość, zakończenia i styl obrysu |
| `Opacity` | przezroczystość całego obiektu lub grupy |
| `X`, `Y`, `W`, `H` | pozycja, szerokość i wysokość |

Panel **Object → Fill and Stroke** pozwala zarządzać kolorami, przezroczystością i obrysem. Sam kolor obrysu nie wystarczy: gdy szerokość obrysu wynosi zero, nie będzie go widać.

**Ćwiczenie:** narysuj kilka części składowych diagramu, zmieniając niezależnie wypełnienie, krawędź i przezroczystość. Przesunięcie suwaka `Opacity` pokaże, jak elementy nachodzą na siebie.

## 3. Transformacje i środek obrotu

Obiekt można przesuwać, skalować, obracać i odbijać. Po wybraniu obiektu narzędziem Select kolejne kliknięcie przełącza uchwyty skalowania na uchwyty obrotu. Można także wprowadzać wartości liczbowe w panelu transformacji.

Obracanie odbywa się wokół określonego **środka obrotu**. Przesunięcie go pozwala np. rozmieszczać elementy wokół wspólnego punktu, a nie jedynie wokół ich własnych środków.

Ważne: skalowanie i obrót nie powinny przypadkowo deformować kształtu. Gdy zachowanie proporcji ma znaczenie, użyj blokady proporcji.

## 4. Kolejność nakładania, wyrównanie i grupowanie

Obiekty SVG mają kolejność rysowania (*z-order*): późniejszy obiekt zwykle zakrywa wcześniejszy. Używaj poleceń **Raise / Lower** oraz **Raise to Top / Lower to Bottom** do ustawiania właściwej kolejności.

Panel **Object → Align and Distribute** służy do wyrównywania oraz równomiernego rozmieszczania elementów. To coś innego niż ręczne przesuwanie „na oko”.

Grupowanie `Ctrl+G` pozwala operować na wielu elementach jako jednej całości. Rozgrupowywanie `Ctrl+Shift+G` przywraca dostęp do składowych. Zapisany SVG powinien pozostać **edytowalny**.

## 5. Warstwy i zablokowane tło

W ćwiczeniu odtwarzania kształtów nie należy rysować bezpośrednio na obrazie referencyjnym. Prawidłowy workflow wygląda następująco:

1. Otwórz dostarczony plik SVG przygotowany przez prowadzącego.
2. Znajdź warstwę `Wzór` (lub analogiczną) w panelu **Layers and Objects**.
3. Upewnij się, że warstwa wzorcowa jest **zablokowana** (symbol kłódki). Nie odblokowuj jej.
4. Utwórz nad nią osobną warstwę `Rysunek`.
5. Wszystkie własne linie i figury twórz **wyłącznie na nowej warstwie**.
6. Zapisz plik pod nową nazwą w swoim folderze `solutions`.

Jeżeli trzeba samodzielnie zbudować taki szablon: zaimportuj grafikę, umieść ją na warstwie `Wzór`, ewentualnie zmniejsz krycie, zablokuj warstwę i dopiero wtedy dodaj nową warstwę.

W pakiecie znajduje się [demonstracyjny plik warstw](examples/inkscape/locked_background_demo.svg). Dwa właściwe szablony egzaminacyjne/ćwiczeniowe doda prowadzący.

## 6. Krzywe Béziera — od punktów do gładkiego konturu

Ścieżka Béziera składa się z odcinków opisanych punktami i uchwytami sterującymi. Krzywa sześcienna ma postać:

$$
B(t)=(1-t)^3P_0+3(1-t)^2tP_1+3(1-t)t^2P_2+t^3P_3,\qquad 0\leq t\leq 1.
$$

Tutaj $P_0$ i $P_3$ są końcami odcinka, a $P_1$ i $P_2$ sterują stycznymi i kształtem krzywej.

W praktyce liczy się umiejętność:

- umieszczania **niewielkiej liczby dobrze dobranych węzłów**, a nie dziesiątek zbędnych,
- ustawiania uchwytów, aby krzywa nie miała załamań,
- rozróżniania węzłów narożnych i gładkich,
- zamykania ścieżki, gdy tworzony jest obiekt z wypełnieniem.

Po narysowaniu ścieżki użyj narzędzia **Edit paths by nodes**, aby dopracować kontur.

## 7. Raster → wektor: Trace Bitmap

Funkcja **Path → Trace Bitmap** tworzy ścieżki na podstawie obrazu pikselowego. Dobrze działa dla prostych logotypów, schematów i kontrastowych konturów, gorzej dla skomplikowanych fotografii.

Procedura:

1. Zaimportuj dostarczony plik PNG.
2. Zaznacz bitmapę i wybierz **Path → Trace Bitmap**.
3. Dla czarnego, kontrastowego motywu wykorzystaj skanowanie pojedyncze z progiem jasności.
4. Utworzony obiekt wektorowy odsuń, aby odróżnić go od pozostającej pod spodem bitmapy.
5. Usuń niepotrzebne fragmenty i popraw kontury. Nie pozostawiaj w pliku wynikowym wyłącznie rastrowej kopii.
6. Zapisz **SVG**, a dodatkowo wyeksportuj obraz **PNG**.

Samo zapisanie pliku `.png` z nowym rozszerzeniem `.svg` **nie jest wektoryzacją**.

## 8. Jak zapisywać i eksportować?

- `SVG` — zachowuje obiekty, grupy i możliwość edycji.
- `PNG` — podgląd gotowego rysunku w zadanej rozdzielczości.
- Eksportuj **rysunek** albo **stronę** świadomie; nie pozostawiaj ogromnych pustych marginesów.
- Przed commitowaniem otwórz zapisany SVG ponownie i sprawdź, czy zawiera wszystkie elementy.

## Dokumentacja

- [Inkscape — strona projektu](https://inkscape.org/)
- [Inkscape Learn](https://inkscape.org/learn/)
- [W3C: SVG](https://www.w3.org/TR/SVG2/)
