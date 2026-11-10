# Obliczenia naukowe

Komputer może pomagać w obliczeniach na kilka różnych sposobów. Czasem chcemy szybko sprawdzić wynik. Czasem potrzebujemy policzyć tysiące wartości. Innym razem zależy nam na **dokładnym wzorze**, a nie tylko liczbie.

W tym bloku poznamy kilka narzędzi i nauczymy się dobierać je do problemu.

Punktem wyjścia są znane już z Colaba i VS Code pliki Pythona oraz notebooki. Wynik obliczenia powinien dać się odtworzyć z zapisanych danych i kodu w forku GitHub, a nie tylko ze zrzutu ekranu.

| Narzędzie | Najlepiej nadaje się do |
| --- | --- |
| **Wolfram Alpha** | szybkiego sprawdzania obliczeń i własności obiektów matematycznych |
| **Wolfram Mathematica / Cloud** | pracy z Wolfram Language w notebooku |
| **Python** | uniwersalnych obliczeń, automatyzacji i analizy danych |
| **NumPy** | szybkich obliczeń numerycznych, obliczeń na wektorach i macierzach w Pythonie |
| **SymPy** | obliczeń symbolicznych w Pythonie |
| **Matplotlib** | tworzenia wykresów w Pythonie |
| **Octave** | obliczeń numerycznych w stylu MATLAB-a |
| **OEIS** | rozpoznawania ciągów liczbowych |
| **Gnuplot** | szybkiego rysowania danych i dopasowywania funkcji |

---

# Obliczenia numeryczne i symboliczne

## Dwa różne pytania

Rozważmy całkę:

$$
I=\int_0^1 x^2\,dx
$$

Możemy zapytać o **wartość numeryczną**:

$$
I \approx 0.3333333333
$$

albo o **wynik dokładny**:

$$
I=\frac{1}{3}
$$

To nie jest dokładnie ten sam rodzaj odpowiedzi.

### Obliczenia numeryczne

W obliczeniach numerycznych operujemy głównie na liczbach i przybliżeniach.

Przykład w Pythonie:

~~~python
print(1 / 3)
~~~

Efekt:

~~~text
0.3333333333333333
~~~

### Obliczenia symboliczne

W obliczeniach symbolicznych program operuje na wzorach.

Przykład w SymPy:

~~~python
from sympy import Rational

x = Rational(1, 3)
print(x)
~~~

Efekt:

~~~text
1/3
~~~

Oba podejścia są potrzebne.

Numeryka jest szczególnie przydatna dla dużych zbiorów danych, symulacji i problemów, dla których nie znamy prostego wzoru dokładnego.

Obliczenia symboliczne są wygodne przy algebraicznym przekształcaniu wzorów, pochodnych, całkach i równaniach.

---

# Wolfram Alpha

## Co to jest Wolfram Alpha?

**Wolfram Alpha** jest systemem obliczeniowym, do którego można wpisywać pytania i wyrażenia matematyczne w dość naturalnej formie.

Nie jest zwykłą wyszukiwarką. Zamiast szukać strony zawierającej odpowiedź, często **oblicza odpowiedź** na podstawie dostarczonego wyrażenia.

Przykładowe zapytanie:

~~~text
factor x^3 - 6x^2 + 11x - 6
~~~

otrzymuje rozkład:

$$
x^3-6x^2+11x-6=(x-1)(x-2)(x-3)
$$

Możemy więc od razu odczytać pierwiastki:

$$
x=1,\qquad x=2,\qquad x=3
$$

---

## Równania

Zapytanie:

~~~text
solve x^2 - 5x + 6 = 0
~~~

daje rozwiązania:

$$
x=2,\qquad x=3
$$

---

## Pochodne

Zapytanie:

~~~text
derivative x^3 - 6x^2 + 11x - 6
~~~

daje:

$$
3x^2-12x+11
$$

---

## Całki

Zapytanie:

~~~text
integrate x^2 from 0 to 1
~~~

prowadzi do:

$$
\int_0^1 x^2\,dx=\frac{1}{3}
$$

---

## Jednostki

Wolfram Alpha jest bardzo wygodny przy przeliczaniu jednostek.

Zapytanie:

~~~text
72 km/h to m/s
~~~

daje:

$$
72\,\mathrm{km/h}=20\,\mathrm{m/s}
$$

Przy obliczeniach fizycznych sprawdzanie jednostek jest często równie ważne jak sprawdzanie samej liczby.

---

## Wolfram Alpha jako narzędzie kontrolne

Wolfram Alpha jest szczególnie użyteczny do:

- szybkiego sprawdzenia rachunków,
- rozwiązania równania,
- sprawdzenia pochodnej lub całki,
- narysowania funkcji,
- konwersji jednostek,
- sprawdzenia własności funkcji.

Nie warto jednak traktować wyniku jako „magicznej prawdy”. Trzeba wiedzieć, **jakie pytanie zostało zadane** i czy program poprawnie je zinterpretował.

---

## Wolfram Cloud

**Wolfram Cloud** pozwala pracować z Wolfram Language w notebookach dostępnych przez przeglądarkę.

Przykład kodu:

~~~text
Factor[x^3 - 6 x^2 + 11 x - 6]
~~~

wynik:

~~~text
(-3 + x) (-2 + x) (-1 + x)
~~~

Ten sam problem możemy więc rozwiązać:

- wpisując zapytanie do Wolfram Alpha,
- pisząc kod w Wolfram Language,
- używając SymPy,
- rozwiązując go ręcznie.

To dobry przykład, że **narzędzia mogą być różne, ale problem matematyczny pozostaje ten sam**.

---

## Dobre materiały

- [Wolfram Alpha — przykłady](https://www.wolframalpha.com/examples/)
- [Wolfram Alpha — przykłady matematyczne](https://www.wolframalpha.com/examples/mathematics)
- [Wolfram Cloud](https://www.wolframcloud.com/)

---

# Python jako kalkulator naukowy

Python jest językiem programowania ogólnego przeznaczenia, ale bardzo dobrze nadaje się również do obliczeń.

## Zmienne

~~~python
a = 12
b = 5

c = a + b
print(c)
~~~

Efekt:

~~~text
17
~~~

Zmienna pozwala nadać nazwę wartości.

---

## Podstawowe operacje

~~~python
a = 7
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a**b)
~~~

Efekt:

~~~text
10
4
21
2.3333333333333335
343
~~~

Operator `**` oznacza potęgowanie.

---

## Typy liczb

~~~python
a = 5
b = 2.5
c = 3 + 4j

print(type(a))
print(type(b))
print(type(c))
~~~

Efekt:

~~~text
<class 'int'>
<class 'float'>
<class 'complex'>
~~~

Najczęściej spotkamy:

- `int` — liczby całkowite,
- `float` — liczby zmiennoprzecinkowe,
- `complex` — liczby zespolone.

---

## Funkcje matematyczne

Moduł `math` zawiera podstawowe funkcje matematyczne.

~~~python
import math

print(math.sqrt(2))
print(math.sin(math.pi / 2))
print(math.exp(1))
~~~

Przykładowy wynik:

~~~text
1.4142135623730951
1.0
2.718281828459045
~~~

---

## Własna funkcja

Zamiast wielokrotnie przepisywać ten sam wzór, możemy zdefiniować funkcję.

~~~python
def energia(m, v):
    return 0.5 * m * v**2

print(energia(2, 3))
~~~

Efekt:

~~~text
9.0
~~~

Funkcje są podstawowym sposobem organizowania kodu obliczeniowego.

---

# NumPy

## Dlaczego nie wystarczy zwykła lista?

Python ma listy:

~~~python
x = [1, 2, 3, 4]
~~~

ale w obliczeniach naukowych często chcemy wykonywać tę samą operację na tysiącach lub milionach elementów.

Do tego służy biblioteka **NumPy**.

~~~python
import numpy as np

x = np.array([1, 2, 3, 4])
print(x)
~~~

Efekt:

~~~text
[1 2 3 4]
~~~

---

## Operacje na całym wektorze

~~~python
import numpy as np

x = np.array([1, 2, 3, 4])

print(x**2)
~~~

Efekt:

~~~text
[ 1  4  9 16]
~~~

Nie musieliśmy pisać pętli po każdym elemencie.

---

## Generowanie siatki punktów

~~~python
import numpy as np

x = np.linspace(0, 1, 6)

print(x)
~~~

Efekt:

~~~text
[0.  0.2 0.4 0.6 0.8 1. ]
~~~

`linspace` tworzy równomiernie rozmieszczone punkty.

To bardzo wygodne przy wykresach i obliczeniach numerycznych.

---

## Podstawowe statystyki

~~~python
import numpy as np

data = np.array([2, 4, 6, 8, 10])

print(np.mean(data))
print(np.std(data))
print(np.min(data))
print(np.max(data))
~~~

Efekt:

~~~text
6.0
2.8284271247461903
2
10
~~~

Domyślnie `np.std(data)` liczy odchylenie standardowe całego zestawu (`ddof=0`). Jeżeli traktujesz dane jako próbę i potrzebujesz estymatora z mianownikiem $n-1$, użyj `np.std(data, ddof=1)`. W raporcie napisz, którą definicję zastosowano.

---

# Wektory i macierze

## Macierz w NumPy

~~~python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

print(A)
~~~

Efekt:

~~~text
[[2 1]
 [1 3]]
~~~

---

## Mnożenie macierzy

Operator `@` oznacza mnożenie macierzowe.

~~~python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

v = np.array([1, 2])

print(A @ v)
~~~

Efekt:

~~~text
[4 7]
~~~

---

## Rozwiązywanie układu liniowego

Rozważmy układ:

$$
\begin{cases}
2x+y=5, \\
x+3y=5.
\end{cases}
$$

W zapisie macierzowym:

$$
A v=b
$$

gdzie:

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
5 \\
5 \\
\end{pmatrix}
$$

NumPy:

~~~python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
], dtype=float)

b = np.array([5, 5], dtype=float)

v = np.linalg.solve(A, b)

print(v)
~~~

Efekt:

~~~text
[2. 1.]
~~~

czyli:

$$
x=2,\qquad y=1
$$

Możemy sprawdzić wynik przez podstawienie: `np.allclose(A @ v, b)`. Jeśli macierz jest osobliwa albo dane pomiarowe tworzą układ nadokreślony, samo `solve` nie jest właściwym rozwiązaniem; wtedy trzeba zbadać problem i ewentualnie użyć metody najmniejszych kwadratów.

---

# SymPy

## Co robi SymPy?

**SymPy** jest biblioteką Pythona do obliczeń symbolicznych.

Zamiast tylko przybliżać wynik liczbowo, potrafi operować na symbolach takich jak $x$, $y$ czy $n$.

---

## Symbol

~~~python
from sympy import symbols

x = symbols("x")

print(x)
~~~

Efekt:

~~~text
x
~~~

Od tej chwili Python może traktować `x` jako symbol matematyczny.

---

## Rozwijanie i faktoryzacja

~~~python
from sympy import symbols, expand, factor

x = symbols("x")

expr = (x - 1) * (x - 2) * (x - 3)

print(expand(expr))
print(factor(x**3 - 6*x**2 + 11*x - 6))
~~~

Efekt:

~~~text
x**3 - 6*x**2 + 11*x - 6
(x - 3)*(x - 2)*(x - 1)
~~~

---

## Równania

~~~python
from sympy import symbols, solve

x = symbols("x")

solutions = solve(x**2 - 5*x + 6, x)

print(solutions)
~~~

Efekt:

~~~text
[2, 3]
~~~

---

## Pochodne

~~~python
from sympy import symbols, diff

x = symbols("x")

f = x**3 - 6*x**2 + 11*x - 6

print(diff(f, x))
~~~

Efekt:

~~~text
3*x**2 - 12*x + 11
~~~

---

## Całki

~~~python
from sympy import symbols, integrate

x = symbols("x")

print(integrate(x**2, (x, 0, 1)))
~~~

Efekt:

~~~text
1/3
~~~

Tu dobrze widać różnicę między obliczeniem symbolicznym a numerycznym: SymPy zwrócił dokładnie `1/3`.

---

## Zamiana wyniku dokładnego na przybliżenie

~~~python
from sympy import Rational

x = Rational(1, 3)

print(x)
print(x.evalf())
~~~

Efekt:

~~~text
1/3
0.333333333333333
~~~

---

## Dobre materiały

- [Python — oficjalny tutorial](https://docs.python.org/3/tutorial/)
- [Python — moduł math](https://docs.python.org/3/library/math.html)
- [NumPy — quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [SymPy — tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html)

---

# CSV — prosty format danych

## Co to jest CSV?

**CSV** oznacza *Comma-Separated Values*.

To prosty tekstowy format tabelaryczny.

Przykład:

~~~csv
x,y
0,1.1
1,2.9
2,5.2
3,7.1
4,8.9
5,11.2
~~~

Pierwsza linia zawiera nazwy kolumn.

Każda następna linia zawiera jeden rekord.

CSV jest bardzo popularny, ponieważ można go otworzyć w:

- Excelu,
- LibreOffice,
- Pythonie,
- Octave,
- R,
- Gnuplocie,
- wielu narzędziach laboratoryjnych.

W przykładach tego kursu separatorem pól jest **przecinek**, a separatorem części dziesiętnej **kropka**. Plik eksportowany przez polski arkusz kalkulacyjny może używać średnika i przecinka dziesiętnego. Przed wczytaniem sprawdź pierwsze linie pliku; dobierz `delimiter` do rzeczywistej zawartości, zamiast zakładać jeden format dla wszystkich CSV.

---

## Wczytanie CSV w NumPy

Dla pliku `measurements.csv`:

~~~csv
x,y
0,1.1
1,2.9
2,5.2
3,7.1
4,8.9
5,11.2
~~~

możemy użyć:

~~~python
import numpy as np

data = np.loadtxt(
    "measurements.csv",
    delimiter=",",
    skiprows=1
)

print(data)
~~~

Efekt:

~~~text
[[ 0.   1.1]
 [ 1.   2.9]
 [ 2.   5.2]
 [ 3.   7.1]
 [ 4.   8.9]
 [ 5.  11.2]]
~~~

Kolumny wybieramy:

~~~python
x = data[:, 0]
y = data[:, 1]
~~~

Ścieżka `measurements.csv` jest liczona względem bieżącego katalogu pracy programu. Jeśli uruchamiasz skrypt z innego folderu, podaj właściwą ścieżkę albo zbuduj ją względem lokalizacji pliku `.py`.

---

# Dopasowanie prostej

Kontynuujemy przykład z `measurements.csv`: tablice `x` i `y` zostały utworzone w poprzedniej sekcji. Chcemy dopasować model:

$$
y=ax+b
$$

W nowym kodzie NumPy zaleca interfejs `numpy.polynomial`. Dopasowanie prostej metodą najmniejszych kwadratów:

~~~python
model = np.polynomial.Polynomial.fit(x, y, deg=1)
b, a = model.convert().coef

print(a)
print(b)
~~~

Otrzymamy w przybliżeniu:

~~~text
2.01143
1.03810
~~~

czyli:

$$
y \approx 2.01143x+1.03810
$$

`Polynomial.fit` zwraca wielomian w przeskalowanej dziedzinie. Po `.convert()` współczynniki odpowiadają zwykłemu zapisowi $b+ax$, w tej właśnie kolejności. Starsze przykłady często używają `np.polyfit(x, y, 1)`; wtedy wyniki zwracane są w kolejności `a, b`.

To przykład obliczenia numerycznego: parametry minimalizują sumę kwadratów różnic między modelem a podanymi wartościami $y$. Samo dopasowanie nie dowodzi, że zależność fizyczna naprawdę jest liniowa. Obejrzyj wykres i reszty $y_i-(ax_i+b)$.

Reszty i średni błąd kwadratowy można policzyć bez dodatkowego pakietu:

~~~python
reszty = y - model(x)
rmse = np.sqrt(np.mean(reszty**2))
print(round(float(rmse), 4))
~~~

W tych przykładowych danych otrzymamy około `0.1232` jednostki osi $y$. Liczba ta opisuje rozrzut względem prostej, ale nie zastępuje informacji o niepewności pomiarowej.

---

# Wykres w Matplotlib

Ten fragment korzysta z `x`, `y`, `a`, `b` i `np` z poprzednich sekcji. W osobnym pliku `.py` trzeba dołączyć również wczytanie CSV i dopasowanie prostej.

~~~python
import matplotlib.pyplot as plt

plt.scatter(x, y, label="dane")

x_fit = np.linspace(0, 5, 100)
y_fit = a * x_fit + b

plt.plot(x_fit, y_fit, label="dopasowanie")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.savefig("fit.png", dpi=150, bbox_inches="tight")
plt.show()
~~~

Powstanie plik:

~~~text
fit.png
~~~

W raporcie Markdown można go osadzić:

~~~markdown
![Dane i dopasowana prosta](fit.png)
~~~

Dobre źródło:

- [Matplotlib — tutoriale](https://matplotlib.org/stable/tutorials/index.html)

---

# Octave

## Co to jest Octave?

**GNU Octave** jest środowiskiem do obliczeń numerycznych, szczególnie wygodnym dla pracy z wektorami i macierzami.

Składnia jest w dużej mierze zgodna z podejściem używanym w MATLAB-ie.

To oznacza, że wiele podstawowych skryptów można przenosić między tymi środowiskami z niewielkimi zmianami.

---

## Wektor

~~~octave
v = [1; 2; 3]
~~~

Efekt:

~~~text
v =

   1
   2
   3
~~~

---

## Macierz

~~~octave
A = [2 1; 1 3]
~~~

Efekt:

~~~text
A =

   2   1
   1   3
~~~

---

## Układ równań

Dla:

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
5 \\
5 \\
\end{pmatrix}
$$

w Octave możemy napisać:

~~~octave
A = [2 1; 1 3];
b = [5; 5];

v = A \ b;

disp(v)
~~~

Efekt:

~~~text
   2
   1
~~~

Operator odwrotnego ukośnika jest jednym z najbardziej charakterystycznych sposobów rozwiązywania układów liniowych w MATLAB-ie i Octave.

---

## Skrypt Octave

Kod możemy zapisać w pliku:

~~~text
solve_system.m
~~~

i uruchomić:

~~~bash
octave solve_system.m
~~~

Dobre źródło:

- [GNU Octave — dokumentacja](https://docs.octave.org/latest/)

---

# OEIS

## Co to jest OEIS?

**OEIS — Online Encyclopedia of Integer Sequences** to baza ciągów liczb całkowitych.

Jeżeli w obliczeniach otrzymamy ciąg:

~~~text
1, 1, 2, 3, 5, 8, 13, 21
~~~

możemy go wyszukać w OEIS.

To oczywiście ciąg Fibonacciego.

OEIS może podać:

- identyfikator ciągu,
- kolejne wyrazy,
- wzory,
- rekurencje,
- odniesienia do literatury,
- powiązane ciągi.

---

## Inny przykład

Ciąg:

~~~text
1, 2, 6, 24, 120, 720
~~~

to wartości:

$$
n!
$$

dla kolejnych $n$.

W OEIS jest to ciąg **A000142**.

Kolejne wyrazy:

~~~text
5040
40320
362880
~~~

OEIS jest szczególnie przydatny w badaniach eksperymentalnych i matematyce dyskretnej, gdy z obliczeń wyłania się ciąg, którego jeszcze nie rozpoznajemy.

Źródło:

- [OEIS](https://oeis.org/)

---

# Gnuplot

## Po co jeszcze jedno narzędzie do wykresów?

Gnuplot jest lekkim programem nastawionym na szybkie rysowanie danych i funkcji.

Może działać bez notebooka i bez rozbudowanego programu w Pythonie.

Przykład pliku `plot.gp`:

~~~gnuplot
set datafile separator ","
set datafile columnheaders
set key left top
set grid
set xlabel "x"
set ylabel "y"
set terminal pngcairo size 1200,800
set output "fit_gnuplot.png"

plot "measurements.csv" using 1:2 with points title "dane"
~~~

Gnuplot może również dopasowywać funkcje.

Przykład:

~~~gnuplot
set datafile separator ","
set datafile columnheaders
set terminal pngcairo size 1200,800
set output "fit_gnuplot.png"

f(x) = a*x + b
a = 1
b = 0

fit f(x) "measurements.csv" using 1:2 via a,b

plot "measurements.csv" using 1:2 with points title "dane", \
     f(x) with lines title "fit"
~~~

Dla naszych danych parametry powinny być bliskie:

~~~text
a = 2.01143
b = 1.03810
~~~

Gnuplot jest dobrym przykładem narzędzia, które robi jedną rzecz i robi ją bardzo sprawnie.

Źródło:

- [Gnuplot — dokumentacja](http://www.gnuplot.info/documentation.html)

---

# Kontrola wyniku i odtwarzalność

Obliczenie jest bardziej wiarygodne, gdy można je sprawdzić **drugą metodą**. Rozwiązanie układu równań podstaw do równań wejściowych. Pochodną symboliczną porównaj z prostym rachunkiem ręcznym. Dopasowaną prostą obejrzyj razem z punktami i resztami. Przy konwersji jednostek sprawdź wymiar fizyczny wyniku.

Liczby zmiennoprzecinkowe są przybliżeniami. Dlatego nie porównuj dwóch wyników obliczeń naukowych wyłącznie przez dokładną równość bitów. Przykład:

~~~python
import math

print(0.1 + 0.2 == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))
~~~

Pierwszy wynik to `False`, drugi `True`. Tolerancję porównania dobiera się do skali problemu i oczekiwanej dokładności; nie służy do ukrywania dużych błędów.

W projekcie GitHub zachowaj:

~~~text
dane wejściowe + kod + opis uruchomienia + wynik
~~~

Podaj jednostki i źródło danych, nie zaokrąglaj ich nadmiernie przed obliczeniem, a wynik zaokrąglij dopiero przy prezentacji. Jeśli używasz liczb losowych, ustaw i zapisz ziarno generatora. Przed oddaniem uruchom skrypt od początku w czystym folderze lub notebook po restarcie środowiska.

---

# Jak dobrać narzędzie?

Nie istnieje jedno narzędzie najlepsze do wszystkiego.

| Problem | Sensowny pierwszy wybór |
| --- | --- |
| szybkie sprawdzenie całki | Wolfram Alpha |
| dokładna pochodna w kodzie Python | SymPy |
| milion wartości funkcji | NumPy |
| macierze i obliczenia w stylu MATLAB | Octave |
| analiza danych z CSV | Python + NumPy |
| wykres w raporcie | Matplotlib |
| szybki wykres z terminala | Gnuplot |
| rozpoznanie ciągu całkowitego | OEIS |

Dobry użytkownik narzędzi obliczeniowych nie pyta tylko:

> Jakiego programu mam użyć?

ale najpierw:

> Czy potrzebuję wyniku dokładnego, przybliżenia numerycznego, wykresu, analizy danych czy rozpoznania struktury?

---

# Sprawdzenie przed oddaniem obliczeń

- [ ] Dane wejściowe i ich jednostki są jawne.
- [ ] Kod działa od początku w opisanym środowisku.
- [ ] Wyniki liczbowe zostały sprawdzone przez podstawienie, oszacowanie lub drugie narzędzie.
- [ ] Wynik dokładny i przybliżony są wyraźnie rozróżnione.
- [ ] Wykres odpowiada danym i ma podpisane osie.
- [ ] Pliki wynikowe można odtworzyć ze źródeł zapisanych w forku GitHub.

[Zadania do tego wykładu](tasks/07_task_obliczenia_naukowe.md) znajdują się w osobnym pliku.

---
