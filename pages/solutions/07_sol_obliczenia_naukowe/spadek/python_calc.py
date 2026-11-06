"""Czas i prędkość swobodnego spadku bez oporu powietrza."""

from math import sqrt
from pathlib import Path

g = 9.81  # m/s^2
h = 20.0  # m
t = sqrt(2 * h / g)
v = g * t

result = f"g={g:.2f} m/s^2\nh={h:.1f} m\nt={t:.4f} s\nv={v:.4f} m/s\n"
(Path(__file__).resolve().parent / "python_results.txt").write_text(result, encoding="utf-8")
print(result, end="")
