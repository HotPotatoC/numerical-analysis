import math
from numbers import Number
from typing import Callable


def riemann(f: Callable, a: Number, b: Number, n: Number) -> Number:
    """
    Riemann sum divides the area into rectangles of the function f into n equal parts.
    """
    dx = (b - a) / n
    area = 0

    x = a
    for _ in range(n):
        area += f(x) * dx
        x += dx

    return area


def trapezoid(f: Callable, a: Number, b: Number, n: Number) -> Number:
    """
    Trapezoid rule squeezes n trapezoids into the area of the function f.
    """
    dx = (b - a) / n
    area = 0

    x = a
    for _ in range(n):
        area += (f(x) + f(x + dx)) * dx / 2
        x += dx

    return area


def simpson(f: Callable, a: Number, b: Number, n: Number) -> Number:
    """
    Simpson's Rule is a numerical method that approximates the value of a definite integral by using quadratic functions
    """
    if n % 2 != 0:
        raise ValueError("n must be even")

    dx = (b - a) / n
    area = f(a) + f(b)

    x = a
    for i in range(1, n - 1):
        if i % 2 == 0:
            area += 2 * f(x + i * dx)
        else:
            area += 4 * f(x + i * dx)

    return area * dx / 3


if __name__ == "__main__":
    """
    Evaluate sin(x) from 0 to pi

    Exact value: 2
    """
    f = lambda x: math.sin(x)
    a = 0
    b = math.pi

    # Amount of grid panels to use (the more panels, the more accurate the result)
    n = 10

    I_riemann = riemann(f, a, b, n)
    I_trapezoid = trapezoid(f, a, b, n)
    I_simpson = simpson(f, a, b, n)

    print(f"Riemanns Integral: {I_riemann}")
    print(f"Trapezoid Rule: {I_trapezoid}")
    print(f"Simpson's Rule: {I_simpson}")

    print()

    print("Exact: 2")
    print(f"Absolute Error Riemanns Integral: {abs(2 - I_riemann)}")
    print(f"Absolute Error Trapezoid Rule: {abs(2 - I_trapezoid)}")
    print(f"Absolute Error Simpson's Rule: {abs(2 - I_simpson)}")
