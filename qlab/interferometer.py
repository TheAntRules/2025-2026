import math
from scipy.optimize import newton
import numpy as np


def DOPL(n, T, theta_i, theta_f, Nf, lam):
    def f(th):
        temp = (1 - (math.sin(th)) ** 2 / (n * n)) ** 0.5
        return 2 * T / temp * (n - math.cos(th - math.acos(temp)))

    return f(theta_f) - f(theta_i) - Nf * lam


# ONLY CHANGE THESE VALUES
t0 = 30  # theta_0
tf = 50  # theta_f
nf = 313  # number of fringes
n0 = 1.49  # initial guess

# Monte Carlo Stuff
tags = ["T", "theta_i", "theta_f", "Nf", "lam"]
means = [0.001, t0, tf, nf, 632.8 * (10**-9)]
stdev = [0.00005, 5, 1, 15, 5 * (10**-9)]


def DOPL_fixed_n(n):
    return DOPL(n, 0.001, t0 / 180 * math.pi, tf / 180 * math.pi, nf, 632.8 * (10**-9))


n_solution = newton(DOPL_fixed_n, x0=n0, tol=1e-10, maxiter=50)

print(f"Refractive index ({t0}-{tf}, {nf} fringes):", n_solution)


def gen_data(n, exclude_index=-1):
    return [
        [
            np.random.uniform(a - b, a + b) if i != exclude_index else a
            for i, a, b in zip(range(len(means)), means, stdev)
        ]
        for _ in range(n)
    ]


def DOPL_i(n, a):
    return DOPL(n, a[0], a[1] / 180 * math.pi, a[2] / 180 * math.pi, a[3], a[4])


def monte_carlo(data):
    return [newton(lambda n: DOPL_i(n, a), x0=n0, tol=1e-10, maxiter=50) for a in data]


num_trials = 10000

# Cumulative
data = gen_data(num_trials)
results = monte_carlo(data)
mean = sum(results) / len(results)
sterror = np.std(results, ddof=1)


# Cumulative
mns, sterrors, contributions = [], [], []
for i in range(len(means)):
    data_i = [[d[j] if j != i else means[j] for j in range(len(d))] for d in data]
    results_i = monte_carlo(data_i)
    mns.append(sum(results_i) / len(results_i))
    sterrors.append(np.std(results_i, ddof=1))
    contributions.append(math.sqrt(sterror**2 - sterrors[-1] ** 2))

print(f"Population Standard Deviation: {sterror}")
print(f"Means: {[q for q in zip(tags, means)]}")
print(f"Estimated Errors: {[q for q in zip(tags, stdev)]}")
print(f"Isolated Contributions: {[q for q in zip(tags, contributions)]}")
