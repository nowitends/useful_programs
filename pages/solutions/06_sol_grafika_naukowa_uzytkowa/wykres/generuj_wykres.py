"""Wykres syntetycznych danych wahadła z jawną niepewnością."""

from pathlib import Path
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
data = np.loadtxt(folder / "wahadlo.csv", delimiter=",", skiprows=1)
length, period, uncertainty = data.T
grid = np.linspace(0.18, 1.02, 300)
model = 2 * np.pi * np.sqrt(grid / 9.81)

fig, ax = plt.subplots(figsize=(6.4, 4.1))
ax.errorbar(length, period, yerr=uncertainty, fmt="o", capsize=4,
            markersize=6, color="#147d86", label="Dane syntetyczne")
ax.plot(grid, model, "--", linewidth=2, color="#b44b26",
        label="Model małych wychyleń")
ax.set_xlabel("Długość L (m)")
ax.set_ylabel("Okres T (s)")
ax.grid(alpha=0.25)
ax.legend(loc="upper left")
fig.tight_layout()
fig.savefig(folder / "wahadlo.pdf")
fig.savefig(folder / "wahadlo.png", dpi=200)
plt.close(fig)
