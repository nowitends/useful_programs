"""Dokładne rachunki algebraiczne i dwie kontrole wyniku."""

from pathlib import Path
from sympy import diff, expand, factor, integrate, solve, symbols

x = symbols("x")
p = x**3 - 6*x**2 + 11*x - 6
factored = factor(p)
roots = solve(p, x)
derivative = diff(p, x)
integral = integrate(x**2, (x, 0, 1))

factor_check = expand(factored - p) == 0
roots_check = all(p.subs(x, root) == 0 for root in roots)
assert factor_check and roots_check

result = (
    f"factor={factored}\n"
    f"roots={roots}\n"
    f"derivative={derivative}\n"
    f"integral={integral}\n"
    f"factor_check={factor_check}\n"
    f"roots_check={roots_check}\n"
)
(Path(__file__).resolve().parent / "symbolic_results.txt").write_text(result, encoding="utf-8")
print(result, end="")
