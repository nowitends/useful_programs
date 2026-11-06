"""Dopasowanie prostej do jawnych danych przykładowych."""

from pathlib import Path
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
data = np.loadtxt(folder / "measurements.csv", delimiter=",", skiprows=1)
x, y = data[:, 0], data[:, 1]

model = np.polynomial.Polynomial.fit(x, y, deg=1)
b, a = model.convert().coef
residuals = y - model(x)
rmse = float(np.sqrt(np.mean(residuals**2)))

result = f"a={a:.5f}\nb={b:.5f}\nrmse={rmse:.5f}\n"
(folder / "fit_results.txt").write_text(result, encoding="utf-8")

fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.scatter(x, y, marker="o", color="#146c83", s=48, label="Dane przykładowe")
x_line = np.linspace(float(x.min()), float(x.max()), 200)
ax.plot(x_line, model(x_line), color="#b44b26", linewidth=2,
        label="Dopasowanie liniowe")
ax.set_xlabel("x (jednostki umowne)")
ax.set_ylabel("y (jednostki umowne)")
ax.legend()
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(folder / "fit.png", dpi=180)
fig.savefig(folder / "fit.pdf")
plt.close(fig)
print(result, end="")
