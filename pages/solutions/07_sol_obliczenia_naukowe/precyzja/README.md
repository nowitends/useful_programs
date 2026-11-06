# Porównywanie liczb `float`

W zapisie binarnym większość ułamków dziesiętnych, w tym `0.1` i `0.2`, nie ma skończonej reprezentacji. Dlatego `0.1 + 0.2 == 0.3` daje `False`, choć wartości są bliskie. [Skrypt](precision.py) pokazuje też, że domyślna tolerancja względna może uznać różnicę `0.1` przy wartości około `100 000 000` za małą. Jeśli w danym pomiarze dopuszczalna różnica wynosi `0.001`, jawna tolerancja bezwzględna daje inny wynik.

Tolerancję ustala się według rozdzielczości pomiaru i celu obliczenia. Nie zwiększa się jej tylko po to, aby test zwrócił `True`. Uruchom `python precision.py` i porównaj [wyniki](precision_results.txt).
