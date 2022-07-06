from numbers import Number
from typing import Callable


def runge_kutta_2nd_order(x0: Number, y0: Number, x: Number, dy: Callable, n: Number):
    h = (x - x0) / n
    for _ in range(n):
        k1 = dy(x0, y0)
        k2 = dy(x0 + h, y0 + h * k1)

        y0 = y0 + h / 2 * (k1 + k2)
        x0 += h

    return y0


def runge_kutta_4th_order(x0: Number, y0: Number, x: Number, dy: Callable, n: Number):
    h = (x - x0) / n
    for _ in range(n):
        k1 = dy(x0, y0)
        k2 = dy(x0 + h / 2, y0 + h / 2 * k1)
        k3 = dy(x0 + h / 2, y0 + h / 2 * k2)
        k4 = dy(x0 + h, y0 + h * k3)

        y0 = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 += h

    return y0


if __name__ == "__main__":
    """
    Case:

    A ball at 1200K is allowed to cool in air at 300K. Assuming heat is lost only by radiation, the differential equation for the temperature of the ball is given by

        dθ/dt = -2.2067 * 10 ** (-12) * (θ**4 - 81 * 10**8)

    Where θ in K and t in seconds. Calculate the temperature at t=480 seconds using the Runge-Kutta method. Assuming a step size of h=48 seconds.
    """

    dθ = lambda t, θ: -2.2067 * 10 ** (-12) * (θ**4 - 81 * 10**8)

    n = 10
    initial_t = 0
    initial_θ = 1200

    R2 = lambda x: runge_kutta_2nd_order(initial_t, initial_θ, x, dθ, n)
    R4 = lambda x: runge_kutta_4th_order(initial_t, initial_θ, x, dθ, n)

    print(f"θ(480) 2nd Order: {R2(480)} K")
    print(f"θ(480) 4th Order: {R4(480)} K")
