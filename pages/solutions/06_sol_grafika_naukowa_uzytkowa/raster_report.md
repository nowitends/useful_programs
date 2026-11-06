# Zmiana rozmiaru rasterów

Źródła: `pages/examples/01_markdown/files/sprezyna/`. Skrypt `resize_batch.py` używa Pillow i zachowuje proporcje.

| Plik | Rozmiar przed | Rozmiar po | Skala szerokości |
| --- | --- | --- | --- |
| energia.png | 1800 × 756 px | 800 × 336 px | 0.4444 |
| schemat.png | 1800 × 612 px | 800 × 272 px | 0.4444 |
| rezonans.png | 1980 × 810 px | 800 × 327 px | 0.4040 |

Zmiana samego rozszerzenia `.jpg` na `.png` nie dekoduje i nie zapisuje obrazu w nowym formacie. Powiększenie małego rastra interpoluje istniejące piksele, ale nie odzyskuje szczegółów, których w źródle nie ma.
