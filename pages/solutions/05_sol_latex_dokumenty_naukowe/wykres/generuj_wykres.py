"""Wykres przykładowych danych wahadła i modelu małych wychyleń."""

from pathlib import Path
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
data = np.loadtxt(folder / "dane.csv", delimiter=",", skiprows=1)
length, period = data[:, 0], data[:, 1]
g = 9.81
grid = np.linspace(0.15, 1.05, 300)
model = lambda L: 2 * np.pi * np.sqrt(L / g)

fig, ax = plt.subplots(figsize=(6.3, 3.8))
ax.plot(grid, model(grid), linewidth=2, color="#264a69", label="Model małych wychyleń")
ax.scatter(length, period, marker="o", s=48, color="#c35a37",
           label="Dane przykładowe", zorder=3)
ax.set_xlabel("Długość wahadła L (m)")
ax.set_ylabel("Okres T (s)")
ax.grid(alpha=0.25)
ax.legend(loc="upper left")
fig.tight_layout()
fig.savefig(folder / "wykres.pdf")
fig.savefig(folder / "wykres.png", dpi=200)
plt.close(fig)

residual = period - model(length)
print(f"max_abs_residual={np.max(np.abs(residual)):.5f} s")
