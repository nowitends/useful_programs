# Zadania: grafika z wykorzystaniem AI

**Folder na rozwiązania:** [`pages/solutions/04_sol_ai/`](../solutions/04_sol_ai/).

Każde zadanie wykorzystujące AI wymaga pliku `prompts.md`: podaj nazwę narzędzia, początkowy prompt, istotną poprawkę oraz krótki opis kontroli jakości. **Wynik musi być zweryfikowany.** Nie publikuj w repozytorium prywatnych danych ani cudzych zdjęć bez zgody.

## Zadanie 1. Zdjęcie → styl rysunkowy

Wybierz zdjęcie, do którego masz prawo i które możesz udostępnić (może to być własna fotografia lub obraz na odpowiedniej licencji). Przy użyciu AI przygotuj jego wersję **rysunkową**: np. szkic tuszem, komiks lub ilustrację ołówkową.

Zachowaj kompozycję i wszystkie istotne elementy zdjęcia, zmieniając przede wszystkim **styl**, a nie treść. Porównaj obie wersje.

Do folderu [`01_style_transfer/`](../solutions/04_sol_ai/01_style_transfer/) dodaj `original.png` (lub `.jpg`), `drawing.png` i `prompts.md`.

## Zadanie 2. AI urządza pomieszczenie

Wykorzystaj zdjęcie wnętrza i poproś AI, aby uzupełniło je o wyposażenie zgodne z Twoimi zainteresowaniami — **na podstawie tego, co rzeczywiście o Tobie wiadomo z rozmowy**, albo na podstawie dostarczonego, fikcyjnego profilu mieszkańca.

Zachowaj geometrię pomieszczenia, perspektywę, położenie okien i drzwi. Nie zmieniaj elementów konstrukcyjnych. Sprawdź, czy meble mają realistyczne proporcje i sensownie się mieszczą.

Do [`02_room/`](../solutions/04_sol_ai/02_room/) dodaj `room_before.png`, `room_after.png` i `prompts.md`. W raporcie zapisz założenia dotyczące użytkownika pokoju, **bez danych wrażliwych**.

## Zadanie 3. Plecak postaci historycznej

Wybierz rozpoznawalną **postać historyczną** (np. Newton, Kopernik lub Maria Skłodowska-Curie). Przygotuj ilustrację przedstawiającą wyobrażoną zawartość jej plecaka lub torby — jako spójnie zaprojektowany zestaw przedmiotów.

Zadbaj o zgodność z epoką. W krótkim komentarzu odróżnij elementy historycznie uzasadnione od kreatywnej interpretacji. Nie podpisuj ilustracji jako autentycznej fotografii.

Do [`03_historical_backpack/`](../solutions/04_sol_ai/03_historical_backpack/) dodaj `backpack.png`, `description.md` i `prompts.md`.

## Zadanie 4. Nowy budynek Wydziału Fizyki i Astronomii

Otwórz **zdjęcie bazowe DSF** dostarczone przez prowadzącego w [`files/ai/building/`](../files/ai/building/) i poproś AI o zaprojektowanie w jego miejscu nowego budynku Wydziału Fizyki i Astronomii UWr.

Nowy budynek powinien mieć charakter akademicki, a projekt musi respektować miejsce, perspektywę zdjęcia, sąsiednią zabudowę i oświetlenie. Zachowaj otoczenie poza obszarem objętym zmianą. Wykonaj przynajmniej jedną **ukierunkowaną poprawkę** bryły lub elewacji.

Do [`04_building/`](../solutions/04_sol_ai/04_building/) dodaj `new_faculty.png` i `prompts.md` (opcjonalnie także wariant pośredni). Obraz oznacz jako **koncepcję wygenerowaną przez AI**, a nie oficjalny projekt inwestycyjny.

**Zdjęcie DSF zostanie uzupełnione przez prowadzącego.**

## Zadanie 5. Od infografiki referencyjnej do wykładu z 5 infografik

To zadanie jest **jednym, wieloetapowym workflow**.

**Krok A — tłumaczenie.** Pobierz niezwiązaną z tematem przyszłego wykładu [infografikę referencyjną](../files/ai/infographic_reference/) w języku angielskim. Poproś AI o przygotowanie wersji polskiej. Zmień **język**, ale zachowaj styl, kompozycję, kolory i hierarchię informacji. Sprawdź wszystkie napisy.

**Krok B — konspekt.** Wybierz temat naukowy lub techniczny i równolegle przygotuj w Markdown **plan pięcioczęściowego wystąpienia**. Każda część powinna mieć tytuł, główną myśl oraz 2–4 najważniejsze informacje, które faktycznie mają znaleźć się na planszy.

**Krok C — przeniesienie stylu.** Wygeneruj **5 nowych infografik** o temacie wykładu, nawiązujących do wizualnego stylu materiału referencyjnego. Materiał referencyjny **nie może być źródłem treści** pięciu nowych plansz. Wszystkie powinny być czytelne i spójne stylistycznie.

**Krok D — kontrola i złożenie.** Zweryfikuj teksty, wzory, daty, skale i jednostki. Połącz pięć plansz w **jeden, pięciostronicowy PDF**. Nie generuj szóstej planszy tytułowej — wykład ma składać się dokładnie z **5 infografik**.

Do [`05_lecture_infographics/`](../solutions/04_sol_ai/05_lecture_infographics/) dodaj:

```text
05_lecture_infographics/
├── reference_pl.png       # przetłumaczona infografika bazowa
├── lecture_plan.md        # konspekt pięciu części
├── 01.png
├── 02.png
├── 03.png
├── 04.png
├── 05.png
├── lecture.pdf            # dokładnie pięć stron
└── prompts.md
```

**Ważne:** podstawowa infografika referencyjna służy nauce tłumaczenia i przenoszenia stylu. Pięć nowych plansz musi przedstawiać **inny temat**.

## Zadanie 6. Sprawdzanie pracy — czerwone adnotacje

Otwórz skan przykładowej pracy z [`files/ai/corrections/`](../files/ai/corrections/) i użyj AI, aby zidentyfikować rzeczywiste błędy. Następnie poproś o naniesienie **czerwonych, odręcznie wyglądających uwag nauczyciela** bez nadpisywania oryginalnych zapisów ucznia.

Nie oceniaj wyłącznie wyglądu adnotacji: każda poprawka powinna być zgodna z treścią zadania. Nie wolno zmieniać oryginalnej pracy tak, jakby uczeń napisał inne rozwiązanie.

Do [`06_red_corrections/`](../solutions/04_sol_ai/06_red_corrections/) dodaj `checked.png`, `mistakes.md` (lista znalezionych błędów z uzasadnieniem) i `prompts.md`.

Oznacz wynik jako **symulację sprawdzania przez AI**. Materiał źródłowy zostanie dostarczony przez prowadzącego.

## Zadanie 7. PDF → odręczne notatki z rysunkami

Na podstawie rozwiązania w PDF z [`files/ai/handwritten/`](../files/ai/handwritten/) przygotuj obraz lub serię obrazów przedstawiających **symulowane odręczne notatki studenta**. Zachowaj treść, wszystkie istotne wzory i ich kolejność oraz niezbędne szkice i rysunki.

Notatki powinny wyglądać naturalnie, ale **muszą być poprawne**. Porównaj tekst i symbole z materiałem źródłowym i popraw nieścisłości. Wynik jednoznacznie oznacz jako symulację wygenerowaną przez AI.

Do [`07_handwritten_notes/`](../solutions/04_sol_ai/07_handwritten_notes/) dodaj `notes_01.png` (oraz kolejne strony, jeśli potrzebne), `verification.md` i `prompts.md`.

**Plik PDF do tego ćwiczenia zostanie dostarczony przez prowadzącego.**

## Ostateczna kontrola

Przed wykonaniem Commit & Push upewnij się, że wszystkie wymagane obrazy są czytelne, nazwy plików są poprawne, a w przypadku pracy naukowej nie pojawiają się **zmyślone lub błędne informacje**. Do wyników nie dołączaj przypadkowych zrzutów całych rozmów — plik `prompts.md` powinien dokumentować istotne decyzje i poprawki.
