# Porównanie szablonów CV

Porównałem [ModernCV](https://ctan.org/pkg/moderncv) z [AltaCV](https://www.overleaf.com/latex/templates/altacv-template/trgqjpwnmtgv). Gotowy [CV Sherlocka Holmesa](cv/cv.pdf) powstał z ModernCV i został sprawdzony jako PDF. AltaCV oceniłem na podstawie [strony szablonu](https://www.overleaf.com/latex/templates/altacv-template/trgqjpwnmtgv) i dostępnego tam przykładu; nie składałem osobnego CV w AltaCV. To ocena dopasowania do tego krótkiego, polskiego CV, a nie ranking dla każdego kandydata.

| Kryterium | ModernCV `classic` | AltaCV |
| --- | --- | --- |
| Hierarchia informacji | Nazwisko, stanowisko i sekcje czyta się w jednej kolumnie od góry. | Dwie kolumny mocniej wyróżniają umiejętności, ale wymagają uważnego rozdziału treści. |
| Kontrast | Ciemny tekst i stonowany niebieski dobrze działają w naszym PDF. | Kolory są elastyczne; demonstracyjny wzór ma więcej akcentów. |
| Czytelność na A4 | Jedna kolumna i oszczędny nagłówek mieszczą się na jednej stronie. | Wąska kolumna może wymagać skracania polskich opisów. |
| Miejsce na osiągnięcia | Krótkie punkty doświadczenia są widoczne bez ozdobników. | Szablon oferuje osobne bloki i tagi na osiągnięcia. |
| Edycja polskiej treści | Wystarczy zwykły LaTeX, `babel` i korekta szerokości etykiet. | Przy dwóch kolumnach trzeba dodatkowo pilnować łamania długich słów. |
| Zależności | Klasa `moderncv` oraz jej pakiety z dystrybucji TeX. | `altacv.cls`, `paracol` i wybrane fonty/ikony; gotowy projekt trzeba pobrać z kompletem plików. |
| Licencja | [LPPL 1.3c](https://ctan.org/pkg/moderncv). | [LPPL 1.3c](https://www.overleaf.com/latex/templates/altacv-template/trgqjpwnmtgv). |

**Wybór:** ModernCV. W [naszym PDF](cv/cv.pdf) nazwa stanowiska, profil, dwa opisy spraw i umiejętności mają czytelną kolejność na jednej stronie. Dla tej ilości tekstu druga kolumna AltaCV dałaby więcej możliwości graficznych, lecz krótsze wiersze mogłyby utrudnić czytanie polskich opisów. Szablon AltaCV może być lepszy przy większej liczbie krótkich umiejętności lub projektów.
