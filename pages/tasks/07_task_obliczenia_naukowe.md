# Zadania: obliczenia naukowe

**Folder na rozwiązania:** [`pages/solutions/07_sol_obliczenia_naukowe/`](../solutions/07_sol_obliczenia_naukowe/) w swoim forku.

To zestaw propozycji do wyboru przez prowadzącego. Zadania 1–5 tworzą powtarzalny projekt obliczeniowy; zadania 6–9 rozwijają kontrolę wyników i porównanie narzędzi. Zapisuj **dane wejściowe, kod, wyniki i krótki opis**, aby można było sprawdzić pracę po pobraniu forka. Nie wystarczy zrzut ekranu z wynikiem.

## Zadanie 1. README projektu

Utwórz `README.md` z tabelą wykonanych zadań i względnymi linkami do plików źródłowych oraz wyników. Napisz, czy programy uruchamiasz lokalnie, w Colabie czy w Codespaces, oraz jakie biblioteki są potrzebne. Po każdej pracy dodaj w README jedno zdanie z najważniejszym wynikiem i jego jednostką, jeśli dotyczy wielkości fizycznej.

**Sprawdzenie:** linki działają na GitHubie, opis uruchomienia jest wystarczający, a wskazane wyniki zgadzają się z plikami.

---

## Zadanie 2. Python jako kalkulator fizyczny

Utwórz `spadek/python_calc.py` i wygenerowany przez niego `spadek/python_results.txt`. Dla wysokości $h=20{,}0\,\mathrm{m}$ i przyspieszenia $g=9{,}81\,\mathrm{m/s^2}$ policz czas spadku bez oporu powietrza $t=\sqrt{2h/g}$ oraz prędkość końcową $v=gt$.

Program ma używać funkcji `math.sqrt`, zapisać dane wejściowe i wyniki z **czterema miejscami po przecinku** oraz właściwymi jednostkami. W `spadek/README.md` zapisz użyte wzory, założenie o braku oporu i kontrolne przybliżenia: $t\approx2{,}0193\,\mathrm{s}$ oraz $v\approx19{,}8091\,\mathrm{m/s}$. Nie przepisuj wyniku ręcznie do pliku `.txt`: program ma go utworzyć.

**Sprawdzenie:** uruchomienie skryptu odtwarza wynik, jednostki są poprawne, a wartości mieszczą się w rozsądnej tolerancji zaokrąglenia.

---

## Zadanie 3. Wynik dokładny w SymPy

Utwórz `sympy/symbolic.py` i generowany `sympy/symbolic_results.txt`. Dla $p(x)=x^3-6x^2+11x-6$ policz rozkład na czynniki, pierwiastki i pochodną. Osobno oblicz dokładną całkę $\int_0^1 x^2\,dx$. Zapisz również **dwie kontrole**: czy po rozwinięciu rozkładu otrzymujemy $p(x)$ oraz czy podstawienie znalezionych pierwiastków daje zero.

Wynik całki ma pozostać ułamkiem `1/3`, nie tylko przybliżeniem dziesiętnym. W `sympy/README.md` wyjaśnij w 3–5 zdaniach różnicę między wynikiem dokładnym a jego przybliżeniem.

**Sprawdzenie:** skrypt działa od początku, kontrole przechodzą, a zapisane wyniki są matematycznie równoważne oczekiwanym; kolejność czynników i pierwiastków nie ma znaczenia.

---

## Zadanie 4. CSV, dopasowanie prostej i reszty

Utwórz `dopasowanie/measurements.csv` z dokładnie poniższą zawartością. Są to **dane przykładowe**, nie wyniki rzeczywistego pomiaru.

~~~csv
x,y
0,1.1
1,2.9
2,5.2
3,7.1
4,8.9
5,11.2
~~~

Napisz `dopasowanie/analyze_data.py`, który wczytuje CSV, dopasowuje model $y=ax+b$ przez `numpy.polynomial.Polynomial.fit`, oblicza reszty $y_i-(ax_i+b)$ oraz RMSE i zapisuje `dopasowanie/fit_results.txt`. W pliku mają być osobne wiersze `a=...`, `b=...` i `rmse=...`, zaokrąglone do pięciu miejsc po przecinku. Oczekiwane przybliżenia: `a=2.01143`, `b=1.03810`, `rmse=0.12319`.

Z tego samego skryptu zapisz `dopasowanie/fit.png` i `dopasowanie/fit.pdf`: punkty danych oraz prostą modelu z podpisanymi osiami i legendą. W `dopasowanie/README.md` wyjaśnij, dlaczego mały RMSE sam w sobie nie dowodzi poprawności fizycznej modelu. Zapisz, że dane są przykładowe.

**Sprawdzenie:** skrypt uruchomiony w folderze projektu odtwarza wszystkie wyniki; parametry i RMSE mieszczą się w tolerancji zaokrąglenia; wykres zgadza się z CSV i zapisanym modelem.

---

## Zadanie 5. Układ liniowy i kontrola podstawieniem

Utwórz `uklad/solve_system.py`, który rozwiązuje układ $2x+y=5$, $x+3y=5$ przy użyciu `numpy.linalg.solve`. Wynik zapisz do `uklad/results.txt` jako `x=...`, `y=...` i `residual_norm=...`. Norma reszty $\lVert Av-b\rVert$ ma być bliska zeru. W `uklad/README.md` pokaż zapis macierzowy i podstaw wynik do obu równań.

**Sprawdzenie:** skrypt odtwarza $x=2$ i $y=1$, a kontrola `A @ v` odpowiada wektorowi $b$ z tolerancją błędów zmiennoprzecinkowych.

---

## Zadanie 6. Druga metoda: Wolfram Alpha

W `wolfram.md` zapisz **dokładne zapytania**, otrzymane odpowiedzi i linki do wyników dla: faktoryzacji wielomianu z zadania 3, rozwiązania układu z zadania 5, całki $\int_0^1 x^2\,dx$ oraz konwersji `72 km/h to m/s`. Przy każdej odpowiedzi napisz, z którym własnym wynikiem ją porównujesz. Na końcu wskaż jedną sytuację, w której automatyczna interpretacja zapytania mogłaby wymagać sprawdzenia.

**Sprawdzenie:** zapytania i odpowiedzi są spójne, linki prowadzą do użytej usługi, a komentarz pokazuje faktyczne porównanie, nie tylko przepisanie ekranu.

## Zadanie 7. Rozpoznanie ciągu w OEIS

Wyszukaj `1, 2, 6, 24, 120, 720` w OEIS i zapisz `oeis.md` z linkiem do znalezionego wpisu, jego numerem, interpretacją ciągu oraz trzema kolejnymi wyrazami. Napisz `oeis.py`, który generuje te sześć wyrazów i trzy następne przez `math.factorial` i zapisuje je do `oeis_results.txt`. W jednym zdaniu wyjaśnij, dlaczego samo dopasowanie kilku początkowych wyrazów nie jest dowodem jedynego wzoru.

**Sprawdzenie:** numer to `A000142`, następne wyrazy to `5040`, `40320`, `362880`, a skrypt odtwarza listę.

## Zadanie 8. Pułapka dokładnej równości liczb `float`

Utwórz `precyzja/precision.py` i `precyzja/README.md`. Pokaż wynik `0.1 + 0.2 == 0.3`, a potem porównanie przez `math.isclose`. Dodaj drugi przykład z większą skalą wartości i jawnie ustawioną tolerancją. Wyjaśnij, skąd bierze się różnica i dlaczego tolerancja musi wynikać z problemu, a nie z chęci uzyskania `True`.

**Sprawdzenie:** kod wypisuje wartości obu porównań, a opis prawidłowo odróżnia zaokrąglenie zapisu liczby od błędu modelu lub danych.

## Zadanie 9. Octave lub Gnuplot — propozycja dodatkowa

Wybierz **jedno** z dwóch narzędzi:

- **Octave:** zapisz `alternatywa/solve_system.m` i `alternatywa/octave_results.txt` dla układu z zadania 5. Użyj operatora `A \ b`, zapisz wynik do pliku i porównaj go z `uklad/results.txt`.
- **Gnuplot:** zapisz `alternatywa/fit.gp` i `alternatywa/gnuplot_fit.png` dla danych z zadania 4. Skrypt ma wczytać CSV, narysować punkty i dopasowaną prostą oraz zapisać obraz. Porównaj parametry z `dopasowanie/fit_results.txt`.

W `alternatywa/README.md` podaj wersję lub nazwę użytego środowiska, sposób uruchomienia i jedną różnicę względem pracy w Pythonie.

**Sprawdzenie:** istnieją źródło i wynik; opis pozwala uruchomić narzędzie ponownie; liczby odpowiadają tym samym danym wejściowym.

---

# Checklista przed wysłaniem

- [ ] README zawiera działające linki do wykonanych prac.
- [ ] Skrypty działają od początku i tworzą pliki wynikowe.
- [ ] Dane wejściowe, jednostki i przyjęte założenia są zapisane.
- [ ] Wyniki dokładne nie zostały zastąpione samymi przybliżeniami.
- [ ] Wynik układu i dopasowania został sprawdzony niezależnie od samego wydruku liczby.
- [ ] Wykres ma podpisane osie, a dane przykładowe są tak nazwane.
- [ ] Po Commit i Push końcowe pliki są widoczne w forku na GitHubie.
