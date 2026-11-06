# Zadania: LaTeX i dokumenty naukowe

**Folder na rozwiązania:** [`pages/solutions/05_sol_latex_dokumenty_naukowe/`](../solutions/05_sol_latex_dokumenty_naukowe/) w swoim forku repozytorium.

To jest **bank propozycji** do późniejszego wyboru przez prowadzącego. Zadania 1–5 tworzą spójny zestaw: artykuł, CV, prezentację i zadanie literackie. Zadania 6–12 można dołączyć lub wybrać jako zamienniki. Każde kończy się plikami, które da się obejrzeć na GitHubie i sprawdzić. Nie publikuj własnego CV, danych kontaktowych ani dokumentów innych osób.

W każdym zadaniu polegającym na stworzeniu dokumentu LaTeX umieść **źródło `.tex` i końcowy `.pdf`** oraz pliki potrzebne do ponownej kompilacji: bibliografię, grafikę, dane lub pliki szablonu. Sam link do projektu w Overleaf nie wystarcza. Po Commit i Push sprawdź pliki w przeglądarce na stronie swojego forka.

## Zadanie 1. Przygotuj folder i indeks prac

Utwórz w podanym folderze `README.md`. Na początku wpisz tytuł bloku, krótką informację o użytym kompilatorze lub Overleaf oraz tabelę z linkami do wykonanych prac. Po każdym zadaniu uzupełnij tabelę o jego źródło i PDF, np. `[raport.tex](raport/raport.tex)` i `[raport.pdf](raport/raport.pdf)`. Dodaj jedną checklistę postępu i zdanie o pochodzeniu wykorzystanych szablonów oraz grafik.

**Sprawdzenie:** linki względne działają w forku na GitHubie, wskazane pliki istnieją, a opis kompilacji pozwala odtworzyć wyniki.

---

## Zadanie 2. Miniartykuł z wieloma elementami LaTeX-a

Utwórz podfolder `raport/` z plikami `raport.tex`, `references.bib`, `dane.csv`, `wykres.pdf` i `raport.pdf`. Dodaj również `generuj_wykres.py` albo `generuj_wykres.ipynb` oraz opisz w `README.md`, jak odtworzyć wykres. Dodatkowe grafiki także zapisz w tym folderze.

**Proponowany temat:** „Czy okres wahadła rośnie wraz z jego długością?”. Poniższe liczby są **danymi przykładowymi do ćwiczenia składu i analizy**, a nie udokumentowanymi wynikami eksperymentu:

~~~csv
dlugosc_m,okres_s
0.20,0.90
0.40,1.27
0.60,1.55
0.80,1.80
1.00,2.01
~~~

Możesz zamiast tego wybrać temat z wcześniejszych zajęć, na przykład ruch ciała na sprężynie lub rzut ukośny, jeśli masz dane i potrafisz podać ich pochodzenie. Wszystkie warianty muszą spełnić te same wymagania.

`raport.tex` ma utworzyć **2–4 strony A4** z:

1. tytułem, autorem, datą i krótkim streszczeniem,
2. co najmniej trzema sekcjami i jedną podsekcją,
3. zwykłymi akapitami, jednym uzasadnionym wyróżnieniem `\emph{...}`, listą `itemize` i listą `enumerate`,
4. co najmniej dwoma wzorami w tekście, jednym wzorem nienumerowanym oraz jednym numerowanym równaniem,
5. przynajmniej jednym działającym odwołaniem do sekcji, równania, tabeli i rysunku przez `\label` i `\ref` lub `\eqref`,
6. tabelą z nagłówkami i jednostkami oraz rysunkiem `wykres.pdf` z podpisem i opisanymi osiami,
7. dwoma cytowaniami rzeczywistych, sprawdzonych źródeł z pliku `references.bib`,
8. krótkim omówieniem ograniczeń danych lub modelu i własnym wnioskiem.

W `dane.csv` zapisz dokładnie dane użyte na wykresie. Jeśli stosujesz dane z ćwiczenia, nazwij je w raporcie przykładowymi. Skrypt lub notebook ma wczytywać `dane.csv` i zapisywać `wykres.pdf`; czytelnik powinien móc odtworzyć rysunek. Użyj ścieżek względnych, aby projekt działał po pobraniu z GitHuba.

**Sprawdzenie:** źródło się kompiluje, w PDF nie ma `??`, rysunek odpowiada danym w CSV, podpisy i jednostki są czytelne, a klucze `\cite{...}` istnieją w `.bib`. Prowadzący może otworzyć PDF i osobno przejrzeć składnię `.tex`.

---

## Zadanie 3. Profesjonalne CV postaci literackiej

Utwórz `cv/cv.tex`, `cv/cv.pdf` oraz wszystkie użyte przez szablon pliki, np. `.cls`, `.sty` i grafiki. W `cv/README.md` podaj **postać, utwór, stanowisko, autora szablonu, link do strony szablonu, licencję i wybrany kompilator**. CV powinno zmieścić się na **jednej stronie A4**.

Postać ma pochodzić z literatury, a nie być Tobą lub osobą z Twojego otoczenia. Przykładowe pary:

| Postać | Fikcyjne stanowisko |
| --- | --- |
| Sherlock Holmes | analityk śledczy |
| Alicja z *Alicji w Krainie Czarów* | specjalistka od testowania nietypowych interfejsów |
| Robinson Crusoe | koordynator logistyki terenowej |
| Don Kichot | inspektor zagrożeń wyobrażonych |

Żartobliwa może być sama sytuacja, ale **forma ma pozostać profesjonalna**. W CV wymagane są: imię i nazwisko postaci, stanowisko, krótki profil dopasowany do stanowiska, co najmniej dwie pozycje doświadczenia lub projektów opisane konkretnymi działaniami, umiejętności, wykształcenie albo przygotowanie do roli oraz fikcyjny kontakt. Nie wpisuj prawdziwego adresu, telefonu, daty urodzenia ani zdjęcia realnej osoby. Dla fikcyjnego e-maila możesz użyć domeny `example.org`.

W `cv/README.md` wypisz w dwóch krótkich listach, które elementy biografii wynikają z utworu, a które są Twoim twórczym dopowiedzeniem. Nie przedstawiaj dopisanych osiągnięć jako dosłownych faktów literackich.

**Rekomendowany szablon:** [AltaCV Template](https://www.overleaf.com/latex/templates/altacv-template/trgqjpwnmtgv). Ma wyraźną hierarchię i miejsce na zwięzły profil oraz umiejętności. Alternatywa: [ModernCV and Cover Letter Template](https://www.overleaf.com/latex/templates/moderncv-and-cover-letter-template/sttkgjcysttn). Możesz wybrać inny szablon z jasno wskazanym autorem i warunkami użycia. Obejrzyj jego PDF przed decyzją, a potem dostosuj kolory, odstępy i ilość tekstu do polskiej treści.

**Sprawdzenie:** projekt kompiluje się z plików w repozytorium, PDF ma jedną czytelną stronę, treść pasuje do stanowiska, kontakt jest fikcyjny, a źródło i licencja szablonu są opisane. **Jakość szablonu i jego dopasowanie** są częścią oceny: przejrzystość, typografia i spójność mają znaczenie, sam efektowny kolor nie wystarcza.

---

## Zadanie 4. Prezentacja Beamer: dane, wykres i wniosek

Utwórz `prezentacja/prezentacja.tex`, `prezentacja/prezentacja.pdf` i wszystkie użyte grafiki. **Proponowany temat:** „Jak wykres może wprowadzić w błąd?”. Przygotuj dwa sposoby pokazania tych samych danych, np. z pełną i obciętą osią pionową. Wskaż, które wrażenie wizualne powstaje w każdym przypadku, i wyjaśnij, co pozostaje niezmienne w samych liczbach. Inne dopuszczalne tematy: „Czy wahadło jest dobrym zegarem?” albo „Jak rozpoznać wiarygodne źródło danych?”.

Prezentacja ma mieć **co najmniej siedem slajdów**: tytuł, pytanie, dane i źródło, metodę, wynik w postaci wykresu, ograniczenie lub kontrprzykład oraz końcowy wniosek. Dodaj też slajd ze źródłami, jeśli nie mieszczą się czytelnie na poprzednich slajdach.

Pokaż znajomość składni Beamera: `frame` z tytułami, lista `itemize` lub `enumerate`, blok `block`, układ `columns`, przynajmniej jedna mała tabela, jeden wzór i jedna grafika z opisanymi osiami lub czytelną legendą. Wybrany motyw powinien mieć spójne kolory i kontrast. Możesz użyć prostego motywu wbudowanego albo [Metropolis Beamer Theme](https://www.overleaf.com/latex/templates/metropolis-beamer-theme/qzyvdhrntfmr), jeżeli potrafisz dołączyć potrzebne pliki i skompilować go po pobraniu repozytorium.

**Sprawdzenie:** `prezentacja.pdf` ma wymaganą liczbę slajdów; w źródle występują wskazane środowiska; grafika, tabela i wzór są czytelne; źródło danych jest podane; widz może zrozumieć jeden główny wniosek z całej prezentacji.

---

## Zadanie 5. Jednostronicowe opowiadanie w innym stylu

Poniższy tekst jest **oryginalnym materiałem do ćwiczenia**. Przepisz wydarzenia do nowego `stylizacja/stylizacja.tex` i przygotuj `stylizacja/stylizacja.pdf` jako **jedną stronę A4**. Wybierz rozpoznawalny, historyczny styl jednego z autorów, np. Bolesława Prusa, Jane Austen, Charlesa Dickensa albo Edgara Allana Poego. Stylizacja może być karykaturalna, ale powinna pozostać własnym tekstem, bez kopiowania zdań z dzieł autora.

### Tekst wyjściowy: „Paczka o siódmej”

> O siódmej rano Lena znalazła pod drzwiami małą paczkę. Na kartonie nie było nazwiska nadawcy, tylko napis: „Otworzyć przed ósmą”. Lena najpierw pomyślała, że ktoś pomylił mieszkania. Na klatce schodowej panowała cisza, a przez okno widać było mokre od deszczu podwórze. Postawiła paczkę na stole i przez chwilę patrzyła na zegar.
>
> W środku leżał stary klucz, kartka z numerem 12 i złożona mapa osiedla. Czerwonym ołówkiem zaznaczono na niej ławkę przy nieczynnej fontannie. Lena znała to miejsce; codziennie mijała je w drodze na przystanek. Nie wiedziała jednak, dlaczego ktoś miałby zostawić jej klucz i mapę. Zadzwoniła do sąsiada z naprzeciwka, ale nie odebrał. Zrobiła zdjęcie paczki, włożyła kartkę do kieszeni i wyszła.
>
> Deszcz już ustał. Przy fontannie siedział mężczyzna w szarym płaszczu i czytał gazetę. Lena przeszła obok niego dwa razy, szukając wskazówki. Dopiero wtedy zauważyła metalową skrzynkę pod ławką. Miała mały zamek. Klucz pasował, choć przekręcił się z trudem. W środku był notes, ołówek i krótka wiadomość: „Jeżeli tu dotarłaś, zanieś notes do biblioteki. Dziś o ósmej zamykają archiwum na remont”.
>
> Lena spojrzała na telefon. Była siódma trzydzieści osiem. Biblioteka znajdowała się po drugiej stronie osiedla. Ruszyła szybkim krokiem, ale po kilku minutach zatrzymała się pod daszkiem sklepu. Notes nie wyglądał na ważny: miał miękką niebieską okładkę i kilka zagiętych rogów. Otworzyła go jednak i zobaczyła rysunki starych drzew, nazwy ulic oraz daty. Ktoś przez lata zapisywał, jak zmieniało się osiedle.
>
> Do biblioteki dotarła przed ósmą. Bibliotekarka obejrzała notes i rozpoznała pismo dawnego mieszkańca. Od miesięcy szukano jego zapisków do wystawy o historii dzielnicy. Lena oddała notes, poprosiła o potwierdzenie przyjęcia i wróciła do domu. Na stole nadal stał pusty karton. Tym razem na odwrocie klapy dostrzegła podpis: „Dziękuję za pomoc — sąsiad spod dwunastki”.

Zachowaj pięć faktów: paczka pojawia się o siódmej; jest klucz i mapa; przy fontannie znajduje się notes; trzeba dotrzeć do biblioteki przed ósmą; na końcu okazuje się, że nadawcą jest sąsiad spod dwunastki. **Zmień wyraźnie** narratora lub sposób opowiadania, składnię zdań, dobór obrazów i ton. Nie wystarczy zamienić kilku przymiotników. W `stylizacja/README.md` podaj wybranego autora i w 5–7 zdaniach wskaż co najmniej trzy cechy stylu, które celowo wyolbrzymiono, oraz dwa konkretne przykłady zmian względem tekstu wyjściowego.

**Sprawdzenie:** PDF ma jedną stronę, fabuła zachowuje wymagane punkty, przekształcenie jest widoczne w całym tekście, a komentarz w README pozwala porównać zamysł z efektem. Skład strony — tytuł, akapity, marginesy i czytelność — także podlega ocenie.

---

## Zadanie 6. Ten sam fragment w Markdown i LaTeX-u

Przygotuj `porownanie/fragment.md`, `porownanie/fragment.tex`, `porownanie/fragment.pdf` i `porownanie/uwagi.md`. Ten sam krótki opis zjawiska ma w obu wersjach zawierać tytuł, dwie sekcje, listę, tabelę i wzór. W `uwagi.md` pokaż w tabeli co najmniej pięć odpowiedników składni, np. nagłówek Markdown i `\section{...}`. Wyjaśnij osobno, dlaczego blok wzoru w pliku `.md` tego kursu zapisujemy jako `$$...$$`, a w `.tex` jako `\[...\]`.

**Sprawdzenie:** oba źródła i PDF istnieją; fragment Markdown poprawnie renderuje się na GitHubie; treść odpowiada wersji LaTeX; porównanie nie myli obu składni.

## Zadanie 7. Naprawa błędnego dokumentu

Skopiuj poniższy celowo błędny fragment do `naprawa/przed.tex`, a następnie zapisz poprawioną, kompletną wersję jako `naprawa/po.tex` i `naprawa/po.pdf`. W `naprawa/diagnoza.md` opisz przynajmniej cztery różne błędy i sposób ich naprawy.

~~~latex
\documentclass{article}
\begin{document}
\section{Wyniki
Plik nazywa się dane_wynikowe.csv.
\begin{itemize}
\item Pomiar 1
\item Pomiar 2
Wynik wzrósł o 5% w drugim pomiarze.
\end{document}
~~~

**Sprawdzenie:** `przed.tex` pozostaje jako materiał porównawczy, `po.tex` kompiluje się, a diagnoza wskazuje przyczyny, nie tylko przepisuje komunikaty kompilatora.

## Zadanie 8. Własny wykres od danych do publikacji

W `wykres/` umieść `dane.csv`, `generuj_wykres.py` lub notebook `.ipynb`, `wykres.pdf`, `wykres.png`, `nota.tex` i `nota.pdf`. Użyj własnych, jawnie opisanych danych lub danych przykładowych z zadania 2. Ten sam wykres zapisz jako PNG i PDF, a w jednostronicowej nocie wstaw wersję PDF i opisz, co widać po powiększeniu obu formatów. Oś każdego wykresu ma mieć nazwę i jednostkę.

**Sprawdzenie:** skrypt lub notebook odtwarza obie grafiki z `dane.csv`; PDF noty zawiera właściwy wykres; porównanie rastrowego PNG i PDF jest rzeczowe.

## Zadanie 9. Sprawdzenie bibliografii

Utwórz `bibliografia/bibliografia.tex`, `bibliografia/references.bib`, `bibliografia/bibliografia.pdf` i `bibliografia/kontrola.md`. Wybierz **trzy rzeczywiste źródła różnego rodzaju**, np. publikację, książkę i oficjalną dokumentację. W `kontrola.md` zapisz dla każdego: adres strony lub DOI, autora, tytuł, rok oraz informację, gdzie te dane sprawdzono. Zacytuj wszystkie trzy pozycje w jednym krótkim tekście.

**Sprawdzenie:** cytowania prowadzą do wpisów `.bib`, bibliografia pojawia się w PDF, metadane odpowiadają wskazanym stronom, a źródła rzeczywiście istnieją.

## Zadanie 10. Dwustronicowy poradnik z podziałem na pliki

Utwórz `poradnik/main.tex`, `poradnik/sections/wstep.tex`, `poradnik/sections/procedura.tex`, `poradnik/poradnik.pdf` i `poradnik/README.md`. Temat: „Jak przygotować projekt LaTeX do archiwum GitHub”. Użyj `\input{...}`, spisu treści, listy kroków i co najmniej jednego odwołania do sekcji. Dokument ma mieć około dwóch stron; w README wskaż plik główny i polecenie kompilacji.

**Sprawdzenie:** `main.tex` wczytuje oba pliki, ścieżki działają po sklonowaniu repozytorium, spis treści i odwołania mają poprawne numery.

## Zadanie 11. Recenzja czytelności szablonów CV

W `ocena_cv.md` porównaj **dwa różne szablony LaTeX CV**, w tym co najmniej jeden z zadania 3. Dodaj linki do oficjalnych stron szablonów oraz tabelę z kryteriami: hierarchia informacji, kontrast, czytelność przy wydruku A4, miejsce na osiągnięcia, łatwość edycji polskiej treści, zależności pakietowe i licencja. Wybierz lepszy do CV fikcyjnej postaci i uzasadnij decyzję na przykładach z własnego PDF. Nie oceniaj tylko miniaturki z galerii — obejrzyj gotowy dokument.

**Sprawdzenie:** oba linki działają, kryteria są zastosowane do obu szablonów, a wybór odpowiada efektowi w `cv/cv.pdf`.

## Zadanie 12. Paczka źródłowa do przekazania innemu autorowi

Utwórz `kontrola_zrodel.md` z checklistą wszystkich plików potrzebnych do odtworzenia jednego wybranego dokumentu z powyższych zadań. Wpisz: plik główny, bibliografię, grafiki, pliki klasy lub stylu, kompilator i polecenie uruchomienia. Zrób próbę kompilacji po pobraniu projektu do nowego folderu albo po imporcie kompletu źródeł do nowego projektu Overleaf. Zapisz wynik próby i ewentualny brakujący element.

**Sprawdzenie:** lista odpowiada rzeczywistym plikom w forku, nie zawiera prywatnych danych ani plików tymczasowych, a opis pozwala innej osobie odtworzyć PDF. Nie wysyłaj ćwiczenia do arXiv ani do czasopisma.

---

# Propozycja kryteriów dla czterech głównych prac

To punkt wyjścia do wyboru zadań i sposobu oceniania, nie gotowa decyzja o liczbie punktów w kursie.

| Praca | Najważniejsze kryteria |
| --- | --- |
| Miniartykuł | kompletna struktura i poprawna składnia; prawidłowe dane, jednostki, odwołania, źródła; czytelny PDF |
| CV | treść dopasowana do stanowiska; profesjonalne sekcje; świadomy wybór i dopasowanie estetycznego szablonu; fikcyjne dane |
| Prezentacja | jasna opowieść od pytania do wniosku; różnorodne elementy Beamera; czytelne slajdy i źródła |
| Stylizacja | wyraźna, konsekwentna zmiana stylu; zachowanie fabuły; jedna starannie złożona strona |

## Checklista przed wysłaniem zmian

- [ ] W `README.md` są działające linki do wykonanych źródeł i PDF-ów.
- [ ] Każdy PDF został otwarty i sprawdzony po ostatniej kompilacji.
- [ ] Projekt daje się odtworzyć z plików zapisanych w forku.
- [ ] Cytowania, etykiety, podpisy i ścieżki nie pokazują błędów.
- [ ] W repozytorium nie ma prawdziwych danych osobowych ani plików pomocniczych kompilacji.
- [ ] Zmiany zostały zatwierdzone i wysłane na GitHub; w przeglądarce widać ich końcową wersję.
