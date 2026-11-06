# Wolfram Alpha jako druga kontrola

Poniższe odnośniki otwierają zapytania w Wolfram Alpha. Dostępny tutaj widok serwisu wymaga JavaScriptu, więc nie mogłem odczytać jego odpowiedzi. Trzecia kolumna podaje **oczekiwany wynik wyliczony niezależnie**, a nie wynik zaobserwowany w interfejsie. Faktoryzację, układ i całkę sprawdziłem skryptami [SymPy](sympy/symbolic.py) i [NumPy](uklad/solve_system.py); konwersja wynika z $72/3{,}6=20$.

| Problem | Zapytanie i link | Oczekiwany wynik do porównania |
| --- | --- | --- |
| Faktoryzacja | [`factor x^3 - 6x^2 + 11x - 6`](https://www.wolframalpha.com/input?i=factor+x%5E3-6x%5E2%2B11x-6) | $(x-1)(x-2)(x-3)$ |
| Układ liniowy | [`solve 2x+y=5, x+3y=5`](https://www.wolframalpha.com/input?i=solve+2x%2By%3D5%2C+x%2B3y%3D5) | $x=2$, $y=1$ |
| Całka | [`integrate x^2 from 0 to 1`](https://www.wolframalpha.com/input?i=integrate+x%5E2+from+0+to+1) | $1/3$ |
| Jednostki | [`72 km/h to m/s`](https://www.wolframalpha.com/input?i=72+km%2Fh+to+m%2Fs) | $20\,\mathrm{m/s}$ |

Trzeba sprawdzić, jak system zinterpretował znaki i zakres zmiennych. Na przykład niejednoznaczny zapis `2x+y=5, x+3y=5` można zastąpić dwiema jawnie oddzielonymi równościami. Niezależna kontrola matematyczna nie zastępuje sprawdzenia wejścia.
