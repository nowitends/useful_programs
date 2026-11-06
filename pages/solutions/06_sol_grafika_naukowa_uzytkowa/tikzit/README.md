# Graf w formacie TikZiT

[graf.tikz](graf.tikz) zawiera cztery węzły i cztery połączenia; [graf.tikzstyles](graf.tikzstyles) definiuje wygląd pól i strzałek. [graf.tex](graf.tex) składa diagram do [graf.pdf](graf.pdf) poleceniem `pdflatex graf.tex`. Plik `.tikz` ma układ warstw i poleceń opisany w [dokumentacji TikZiT](https://tikzit.github.io/).

**Zakres wykonania:** ten przykład przygotowałem w edytorze tekstowym i skompilowałem w LaTeX-u. Program TikZiT nie jest zainstalowany w użytym środowisku, dlatego nie potwierdziłem otwarcia ani przesuwania węzłów w jego interfejsie. Pozostaje to częścią zadania do sprawdzenia ręcznie.

TikZ rysuje graf na podstawie kodu, a TikZiT jest wizualnym edytorem niektórych diagramów TikZ. Mysz pozwoliłaby szybko przesunąć „Analizę A” względem „Analizy B”; w kodzie wygodniej zmienić wspólny styl wszystkich strzałek. Źródła i wynik PDF są zapisane razem, więc etap kompilacji można sprawdzić niezależnie od GUI.
