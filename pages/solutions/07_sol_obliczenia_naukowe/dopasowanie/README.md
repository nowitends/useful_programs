# Dopasowanie liniowe

[Dane](measurements.csv) są **przykładowe**, więc osie mają jednostki umowne. Uruchom `python analyze_data.py` po instalacji NumPy i Matplotlib. Skrypt zapisuje [parametry i RMSE](fit_results.txt), [PNG](fit.png) oraz [PDF](fit.pdf). Współczynniki modelu $y=ax+b$ wynoszą około $a=2{,}01143$ i $b=1{,}03810$.

RMSE opisuje rozrzut punktów względem dopasowanej prostej. Mała wartość RMSE nie dowodzi, że proces fizyczny jest liniowy: model trzeba uzasadnić dziedzinowo i sprawdzić również rozkład reszt. W tym ćwiczeniu nie znamy niepewności pomiarowych, więc nie przypisuję wykresowi słupków błędów.
