import numpy as np
import matplotlib.pyplot as plt


def make_sequence(f, x0, n):
    x = np.zeros(n)
    x[0] = x0

    for i in range(1, n):
        x[i] = f(x[i-1])

    return x


def log_map(x, r):
    return r*x*(1-x)


def main():
    # nbr iterations per r-value and initial condition x0
    n = 1000

    # range of r
    r_range = np.arange(1, 4, 0.01)

    # range of initial conditions per r
    x0_range = np.arange(0.1, 1, 0.02)

    # nbr of points in the end of the sequence to plot
    m = 10

    fig, ax = plt.subplots()
    ax.set_xlabel("$r$")
    ax.set_ylabel("$\lim_{n\\to\infty}x_n$")

    for r in r_range:
        for x0 in x0_range:
            y = make_sequence(lambda x: log_map(x, r), x0, n)
            ax.plot(r*np.ones(m), y[-m-1:-1], "k.", markersize=0.1)

    plt.show()


if __name__ == "__main__":
    main()