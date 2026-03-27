# Lab code by Eric Cai and Anant Krishna

import numpy as np
import matplotlib.pyplot as plt
import random

from qutip import expect, basis, sigmax, sigmay, sigmaz, sesolve, Bloch, Options

seed = 31
random.seed(seed)
np.random.seed(seed)


def getBlochVector(state):
    return np.array(
        [expect(sigmax(), state), expect(sigmay(), state), expect(sigmaz(), state)]
    )


def trace_distance(a, b):
    return 0.5 * np.sqrt(np.sum((a - b) ** 2))


# ============================================================
# 1. Parameters
#    Work numerically with ħ = 1; H has units of rad/s.
# ============================================================

Omega0 = 2 * np.pi * 10e3  # 2π × 10 kHz ~ 6.283e4 rad/s
sigma = 10.0 * 1e-6  # microseconds

Omega0_jitter = Omega0 * 0.001
sigma_jitter = sigma * 0.005

# ============================================================
# 2. Time grid: positive-only times 0 → 10σ, pulse centered at 5σ
# ============================================================

t0 = 5 * sigma  # center the Gaussian at 5σ (in seconds)
t_start = 0.0
t_end = 10 * sigma  # window [0, 10σ] in seconds

tlist = np.linspace(t_start, t_end, 20)  # seconds
tlist_us = tlist * 1e6  # microseconds for plotting

gen_args_nominal = lambda: {"Omega0": Omega0, "sigma": sigma, "t0": t0}
gen_args_jitter = lambda: {
    "Omega0": np.random.normal(Omega0, Omega0_jitter),
    "sigma": np.random.normal(sigma, sigma_jitter),
    "t0": t0,
}


# ============================================================
# 3. Time-dependent Hamiltonian H(t) = Omega_z(t) * Sz
# ============================================================


def Omega(t, args):
    """Z-rotation rate Omega_z(t) in rad/s (Gaussian pulse)."""
    Omega0 = args["Omega0"]
    sigma = args["sigma"]
    t0 = args["t0"]
    return Omega0 * np.exp(-((t - t0) ** 2) / (2 * sigma**2))


# Spin operators
Sx = 0.5 * sigmax()
Sy = 0.5 * sigmay()
Sz = 0.5 * sigmaz()

# ============================================================
# 4. Initial state and time evolution
#    Start in |+x> = (|0> + |1>)/sqrt(2).
# ============================================================

psi0 = (basis(2, 0) + basis(2, 1)).unit()

# Track expectations of sigma_x, sigma_y, sigma_z
e_ops = [2 * Sx, 2 * Sy, 2 * Sz]  # gives <σx>, <σy>, <σz>

# Force QuTiP to store the states as well as expectations
opts = Options(store_states=True)

NumPulse = 50

# initialize arrays  *** BE CAREFULE WITH DATATYPES IN QuTip
# array[0] = ideal, array[1] = noisy
pulseNum = []  # list to store the index of pulses
times_all = [None, None]  # 1D numpy array
states_all = [[], []]  # list of Qobj (specal QuTip datatype)
expect_all = [None, None]  # list of many numpy arrays
blochvec_all = [[], []]
trace_dist = []

psi0 = (basis(2, 0) + basis(2, 1)).unit()
psi_all = [psi0.copy(), psi0.copy()]


# Concatinates time, state, and expectation value lists after each pulse
def concat_data(result, times_all, states_all, expect_all):
    times_k = np.array(result.times)  # convert result.times to numpy array for t_offset

    # check for first pulse empty data
    if times_all is None:
        # first pulse: take everything as-is
        times_all = times_k
        states_all = list(result.states)
        expect_all = [np.array(e) for e in result.expect]

    # for all pulses after first pulse
    else:
        # shift times of this pulse so it follows previous pulse
        t_offset = times_all[-1]
        new_times = times_k[1:] + t_offset  # skip first to avoid duplicate

        # concatenate times
        times_all = np.concatenate([times_all, new_times])

        # concatenate states (skip first to avoid duplicate)
        states_all.extend(result.states[1:])

        # concatenate expectation values (each expect[j] is already an array)
        for j in range(len(expect_all)):
            expect_all[j] = np.concatenate(
                [expect_all[j], np.array(result.expect[j][1:])]
            )
    return times_all, states_all, expect_all


def gen_random_axis():
    return random.choice([Sx, Sy, Sz])


def gen_random_axis_all():
    theta = random.random() * 2 * np.pi
    phi = random.random() * np.pi
    coeffs = [np.sin(phi) * np.cos(theta), np.sin(phi) * np.sin(theta), np.cos(phi)]
    return np.dot(coeffs, [Sx, Sy, Sz])


for k in range(NumPulse):
    pulseNum.append(k + 1)  # get index of loop

    H_axis = gen_random_axis()
    H = [[H_axis, Omega]]  # build Hamiltonian - not evaluated until sesolve()

    for i in range(2):
        args = gen_args_nominal() if i == 0 else gen_args_jitter()

        # Solve Schrodinger Equation for current (k) pulse
        result = sesolve(H, psi_all[i], tlist, e_ops=e_ops, args=args, options=opts)

        # Set final state of sesolve() to be intial state for next loop
        psi_all[i] = result.states[-1]

        # Concatenation of data from each pulse into big lists
        times_all[i], states_all[i], expect_all[i] = concat_data(
            result, times_all[i], states_all[i], expect_all[i]
        )
        blochvec_all[i].append(getBlochVector(psi_all[i]))
    trace_dist.append(trace_distance(blochvec_all[0][-1], blochvec_all[1][-1]))


# Optional: plot expectation values vs time in microseconds
plt.figure()
plt.plot(times_all[0] * 1e6, expect_all[0][2], "-", label=r"Nominal")
plt.plot(times_all[1] * 1e6, expect_all[1][2], "--", label=r"Noisy")
plt.xlabel("time (µs)")
plt.ylabel("expectation value in z")
plt.legend()
plt.xticks([i * 200 for i in range(NumPulse // 2 + 1)])
plt.grid(True)
plt.tight_layout()

plt.figure()
plt.plot(pulseNum, trace_dist)
plt.xlabel("Pulse Number")
plt.ylabel("Trace Distance")
plt.legend()
plt.xticks([i * 2 for i in range(NumPulse // 2 + 1)])
plt.grid(True)

# ============================================================
# 5. Bloch sphere trajectory
# ============================================================

# b = Bloch()
# b.add_states(states_all[0])
# b.show()

plt.show()
