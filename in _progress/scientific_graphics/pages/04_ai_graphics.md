# AI w grafice użytkowej i naukowej

W przypadku AI nie chodzi jedynie o wygenerowanie estetycznego obrazka. Ważniejsze jest, czy potrafimy **kontrolować zmianę**, utrzymywać spójność kilku ilustracji, poprawnie przekazywać informację i sprawdzać wynik.

**Zadania:** [AI Graphics](tasks/04_task_ai_graphics.md) · **Materiały:** [`files/ai/`](files/ai/)

## 1. Edycja obrazu i generowanie od podstaw

Rozróżniamy dwa procesy:

- **Generowanie od zera:** tworzenie nowego obrazu na podstawie opisu.
- **Edycja obrazu referencyjnego:** modyfikacja istniejącego obrazu przy jednoczesnym zachowaniu wybranych jego cech.

W edycji szczególnie istotne są *inwarianty* — elementy, które mają pozostać bez zmian: perspektywa, proporcje, układ pomieszczenia, tło, rozpoznawalna postać, zawartość nieedytowanego fragmentu.

Dobry prompt na edycję zawiera trzy części:

1. **Co zachować?**
2. **Co dokładnie zmienić?**
3. **Czego nie wolno zmieniać?**

Przykład:

> Przekształć załączone zdjęcie w czytelny rysunek w stylu ilustracji prasowej. Zachowaj geometrię pomieszczenia, ustawienie okien i punkt widzenia. Nie dodawaj nowych drzwi i nie zmieniaj liczby osób.

## 2. Style transfer — ta sama scena, inna estetyka

Zmiana stylu to nie to samo co stworzenie zupełnie nowej sceny. Dobrą próbą jest porównanie przed i po: czy wszystkie istotne obiekty nadal znajdują się we właściwych miejscach? Czy zmieniła się jedynie estetyka, czy także treść?

Przykładowe style: rysunek tuszem, akwarela, szkic ołówkowy, komiks, ilustracja podręcznikowa.

**Praktyka:** często lepiej poprosić AI o zmianę jednego aspektu naraz, a dopiero potem korygować kolorystykę lub detale.

## 3. Aranżacja wnętrza i kontrola geometrii

W obrazie pomieszczenia AI powinno respektować ściany, drzwi, okna, kierunek światła i skalę przedmiotów. Można poprosić model, aby dopasował wystrój do opisu użytkownika, ale nie należy zakładać, że zna jego rzeczywiste preferencje.

Możesz użyć **fikcyjnego profilu mieszkańca** zamiast publikować prywatne zdjęcia i szczegóły z własnego domu. Oceń, czy nowe elementy są sensownie rozmieszczone i nie przecinają istniejących ścian.

## 4. Rekonstrukcja historyczna a kreatywna interpretacja

Zadanie z plecakiem postaci historycznej jest **interpretacją artystyczną**, nie fotografią dokumentalną. Wygląd przedmiotów powinien być spójny z epoką, ale nie można przedstawiać fikcyjnego zestawu jako autentycznie należącego do danej osoby.

Warto odróżnić:

- elementy potwierdzone źródłowo,
- prawdopodobne przedmioty typowe dla epoki,
- elementy całkowicie fikcyjne.

## 5. Edycja architektury na istniejącym zdjęciu

Przy fotomontażu nowego budynku na zdjęciu referencyjnym kluczowe są:

- zachowanie punktu widzenia i linii perspektywy,
- poprawne umiejscowienie bryły względem otoczenia,
- dopasowanie skali i wysokości do sąsiednich budynków,
- spójność oświetlenia i cieni,
- zachowanie elementów tła, których nie obejmuje projekt.

W tym kursie zadaniem jest **koncepcja nowego budynku Wydziału Fizyki i Astronomii w miejscu DSF**, a nie realistyczna wizualizacja zatwierdzonej inwestycji. Wynik należy jednoznacznie oznaczyć jako koncepcję AI.

## 6. Infografiki: tekst, treść, styl

Infografika łączy **strukturę informacji** z projektem graficznym. Nie wystarczy, że zawiera obrazki i kilka haseł — czytelnik musi rozumieć, co z nich wynika.

Najważniejsze cechy dobrej infografiki:

- jeden wyraźny temat,
- hierarchia informacji,
- niewielka liczba dobrze dobranych elementów,
- czytelne podpisy,
- spójne kolory i typografia,
- poprawność językowa i merytoryczna.

### Workflow: jedna obca infografika → pięć infografik wykładowych

1. Otwórz dostarczoną **infografikę referencyjną** w języku angielskim.
2. Poproś AI o **tłumaczenie na polski bez zmiany układu i stylu**.
3. Oceń, które elementy decydują o stylu: paleta kolorów, grubości linii, fonty, kształty kart, proporcje.
4. Niezależnie przygotuj w Markdown **plan pięcioczęściowego wykładu** na wybrany temat naukowy.
5. Dla każdej części planu wygeneruj oddzielną infografikę. Wszystkie pięć powinno wyglądać jak **jedna spójna seria**, nawiązująca stylem do materiału referencyjnego.
6. Popraw błędy, w szczególności zniekształcone napisy, równania, jednostki i etykiety.
7. Połącz pięć plansz w jeden PDF we właściwej kolejności.

**Ważne:** infografika referencyjna jest niezwiązana tematycznie z wykładem. Przenosimy **styl graficzny**, a nie jej merytoryczną treść.

## 7. AI sprawdzające rozwiązania — czerwone poprawki

Rozpoznanie błędów merytorycznych i **naniesienie poprawek na obraz** to dwa odrębne kroki. Wygodniejszy workflow:

1. Wyodrębnij widoczne równania i rozwiązania (transkrypcja).
2. Przeanalizuj je niezależnie i sporządź listę błędów.
3. Dopiero potem nanieś krótkie adnotacje **czerwonym kolorem**, zachowując oryginalne zapiski.
4. Sprawdź, czy AI nie „naprawiło” potajemnie oryginalnego zapisu ucznia.

Adnotacja ma wyglądać jak uwaga nauczyciela, ale wynik należy oznaczyć jako **symulację sprawdzania stworzoną przez AI**.

## 8. PDF → symulowane odręczne notatki

Można przekształcić cyfrowe rozwiązanie w ilustrację przypominającą odręcznie zapisane kartki. Muszą pozostać:

- wszystkie istotne równania i przekształcenia,
- tekstowe komentarze,
- rysunki i szkice,
- poprawność symboli oraz indeksów.

Nie zakładaj, że generator obrazu poprawnie skopiuje dłuższy wzór matematyczny. Porównaj notatki z oryginalnym PDF-em **linia po linii**. Jeżeli to konieczne, popraw błędne symbole ręcznie.

Nie wolno przedstawiać tak uzyskanego dokumentu jako autentycznego rękopisu innej osoby.

## 9. Jak dokumentować pracę z AI?

Dla każdego zadania przygotuj plik `prompts.md` zawierający przynajmniej: nazwę użytego narzędzia, pierwszy prompt, ważne poprawki i krótką ocenę wyniku. Nie trzeba dołączać całej rozmowy; wystarczą fragmenty pokazujące sensowny workflow.

W odróżnieniu od przypadkowego eksperymentowania ważne jest, aby umieć wskazać **konkretną zmianę**, którą wniosła każda iteracja.

### Szablon raportu

```markdown
# Workflow AI

## Narzędzie

Nazwa usługi / modelu (jeśli znany).

## Cel i materiał wejściowy

Co miało zostać zmienione, a co zachowane?

## Prompt początkowy

...

## Najważniejsza poprawka

...

## Kontrola jakości

Co sprawdzono? Jakie błędy poprawiono?
```

## 10. Odpowiedzialne wykorzystanie obrazów

- Nie publikuj bez zgody prywatnych zdjęć osób i pomieszczeń.
- Zdjęcia, skany i materiały referencyjne muszą być używane zgodnie z ich prawami i przeznaczeniem.
- Oznaczaj realistycznie wyglądające **fikcyjne wizualizacje** jako wygenerowane przez AI.
- Poprawność graficzna nie zastępuje sprawdzenia poprawności naukowej.
- Nie przesyłaj do zewnętrznych usług danych osobowych prawdziwych studentów; prace do ćwiczeń powinny być fikcyjne lub odpowiednio przygotowane przez prowadzącego.
