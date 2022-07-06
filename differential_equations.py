from numbers import Number
from typing import Callable


def runge_kutta_2nd_order(
    x: Number, initial_x: Number, y: Number, dy: Callable, h: Number
):
    while initial_x != x:
        k1 = dy(x, y)
        k2 = dy(x + h, y + h * k1)

        solution = y + h / 2 * (k1 + k2)
        initial_x += h
        y = solution

    return solution


def runge_kutta_4th_order(
    x: Number, initial_x: Number, y: Number, dy: Callable, h: Number
):
    while initial_x != x:
        k1 = dy(x, y)
        k2 = dy(x + h / 2, y + h / 2 * k1)
        k3 = dy(x + h / 2, y + h / 2 * k2)
        k4 = dy(x + h, y + h * k3)

        solution = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        initial_x += h
        y = solution

    return solution


if __name__ == "__main__":
    """
    Case:

    A ball at 1200K is allowed to cool in air at 300K. Assuming heat is lost only by radiation, the differential equation for the temperature of the ball is given by

        dθ/dt = -2.2067 * 10 ** (-12) * (θ**4 - 81 * 10**8)

    Where θ in K and t in seconds. Calculate the temperature at t=480 seconds using the Runge-Kutta method. Assuming a step size of h=48 seconds.
    """

    dθ = lambda t, θ: -2.2067 * 10 ** (-12) * (θ**4 - 81 * 10**8)

    h = 48
    initial_t = 0
    initial_θ = 1200

    R2 = lambda x: runge_kutta_2nd_order(x, initial_t, initial_θ, dθ, h)
    R4 = lambda x: runge_kutta_4th_order(x, initial_t, initial_θ, dθ, h)

    print(f"θ(480) 2nd Order: {R2(480)} K")
    print(f"θ(480) 4th Order: {R4(480)} K")
