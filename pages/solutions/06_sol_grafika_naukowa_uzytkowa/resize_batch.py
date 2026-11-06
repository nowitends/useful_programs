"""Skalowanie trzech przykładów do szerokości 800 px bez zmiany proporcji."""

from pathlib import Path
from PIL import Image

folder = Path(__file__).resolve().parent
source = folder.parents[1] / "examples" / "01_markdown" / "files" / "sprezyna"
target = folder / "batch"
target.mkdir(exist_ok=True)

rows = []
for name in ("energia", "schemat", "rezonans"):
    with Image.open(source / f"{name}.png") as image:
        original = image.size
        height = round(original[1] * 800 / original[0])
        resized = image.resize((800, height), Image.Resampling.LANCZOS)
        resized.save(target / f"{name}_800.png")
        rows.append((name, original, resized.size, 800 / original[0]))

table = [
    "# Zmiana rozmiaru rasterów",
    "",
    "Źródła: `pages/examples/01_markdown/files/sprezyna/`. Skrypt `resize_batch.py` używa Pillow i zachowuje proporcje.",
    "",
    "| Plik | Rozmiar przed | Rozmiar po | Skala szerokości |",
    "| --- | --- | --- | --- |",
]
for name, before, after, scale in rows:
    table.append(f"| {name}.png | {before[0]} × {before[1]} px | {after[0]} × {after[1]} px | {scale:.4f} |")
table.extend([
    "",
    "Zmiana samego rozszerzenia `.jpg` na `.png` nie dekoduje i nie zapisuje obrazu w nowym formacie. Powiększenie małego rastra interpoluje istniejące piksele, ale nie odzyskuje szczegółów, których w źródle nie ma.",
    "",
])
(folder / "raster_report.md").write_text("\n".join(table), encoding="utf-8")
print("Wygenerowano", len(rows), "obrazów PNG o szerokości 800 px")
