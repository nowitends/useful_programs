"""Rozwiązanie układu równań z kontrolą reszty."""

from pathlib import Path
import numpy as np

A = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([5.0, 5.0])
v = np.linalg.solve(A, b)
residual_norm = float(np.linalg.norm(A @ v - b))
assert np.allclose(A @ v, b)

result = f"x={v[0]:.6f}\ny={v[1]:.6f}\nresidual_norm={residual_norm:.6e}\n"
(Path(__file__).resolve().parent / "results.txt").write_text(result, encoding="utf-8")
print(result, end="")
