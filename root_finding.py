import math
from numbers import Number
from typing import Callable


def sign(x: Number):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def bisection(f: Callable, a: Number, b: Number, epsilon=0.01) -> Number:
    """
    The bisection method is an approximation method to find the roots of
    the given equation by repeatedly dividing the interval. This method will
    divide the interval until the resulting interval is found, which is extremely small.
    """
    if sign(f(a)) == sign(f(b)):
        raise ValueError("a and b must have different signs")

    mid = (a + b) / 2

    if abs(f(mid)) < epsilon:
        return mid
    elif sign(f(mid)) == sign(f(a)):
        return bisection(f, mid, b, epsilon)
    elif sign(f(mid)) == sign(f(b)):
        return bisection(f, a, mid, epsilon)


def newton_raphson(f: Callable, df: Callable, a: Number, epsilon=0.01) -> Number:
    """
    Newton-Raphson method is an approximation method to find the roots of
    the given equation. This method produces successively better approximations
    to the roots of real-valued equations.
    """
    xn = a - f(a) / df(a)
    if abs(f(xn)) < epsilon:
        return xn
    else:
        return newton_raphson(f, df, xn, epsilon)


if __name__ == "__main__":
    """
    Evaluate sqrt(2)
    """
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x
    a = 0
    b = 2

    print(f"Bisection method: {bisection(f, a, b)}")
    print(f"Newton raphson method: {newton_raphson(f, df, b)}")

    print()

    print(f"Exact: {math.sqrt(2)}")
    print(f"Absolute Error Bisection method: {abs(2 - bisection(f, a, b))}")
    print(f"Absolute Error Newton raphson method: {abs(2 - newton_raphson(f, df, b))}")
