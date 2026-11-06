"""Dwa przykłady porównania liczb zmiennoprzecinkowych."""

import math
from pathlib import Path

first = 0.1 + 0.2
baseline = 100_000_000.0
reading = baseline + 0.1

result = (
    f"0.1+0.2={first:.17f}\n"
    f"exact_equality={first == 0.3}\n"
    f"isclose_default={math.isclose(first, 0.3)}\n"
    f"large_scale_default={math.isclose(reading, baseline)}\n"
    f"large_scale_1mm={math.isclose(reading, baseline, rel_tol=0.0, abs_tol=0.001)}\n"
)
(Path(__file__).resolve().parent / "precision_results.txt").write_text(result, encoding="utf-8")
print(result, end="")
