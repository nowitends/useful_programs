"""Kontrola równania y'=2 sqrt(y^2+C) dla Lambda=3 i C=1."""
from math import asinh, sinh, sqrt
from pathlib import Path

import matplotlib.pyplot as plt


def rhs(y: float, c: float = 1.0) -> float:
    return 2.0 * sqrt(y * y + c)


def rk4(step: float, end: float = 1.0) -> tuple[list[float], list[float]]:
    n = round(end / step)
    h = end / n
    times = [0.0]
    values = [1.0]
    for i in range(n):
        y = values[-1]
        k1 = rhs(y)
        k2 = rhs(y + h * k1 / 2)
        k3 = rhs(y + h * k2 / 2)
        k4 = rhs(y + h * k3)
        values.append(y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        times.append((i + 1) * h)
    return times, values


def exact(t: float) -> float:
    return sinh(2 * t + asinh(1))


if __name__ == "__main__":
    for step in (0.1, 0.05, 0.025):
        times, values = rk4(step)
        error = abs(values[-1] - exact(times[-1]))
        print(f"h={step:.3f}, blad koncowy={error:.8g}")

    times, values = rk4(0.05)
    reference = [exact(t) for t in times]
    errors = [abs(v - e) for v, e in zip(values, reference)]
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5), layout="constrained")
    axes[0].plot(times, reference, label="analitycznie")
    axes[0].plot(times, values, "o", markersize=3, label="RK4, h=0.05")
    axes[0].set(xlabel="t", ylabel="y=a²", title="Rozwiązanie")
    axes[0].legend()
    axes[1].semilogy(times[1:], errors[1:])
    axes[1].set(xlabel="t", ylabel="|błąd|", title="Błąd bezwzględny")
    for ax in axes:
        ax.grid(alpha=0.25)
    fig.savefig(Path(__file__).with_name("analiza_numeryczna.png"), dpi=180)
