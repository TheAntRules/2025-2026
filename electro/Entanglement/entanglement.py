import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

from qutip import basis, tensor, qeye, ket2dm, ptrace, entropy_vn

zero = basis(2, 0)
one = basis(2, 1)


def zero_state(N):
    return tensor([zero] * N)


def ghz_N(N):
    return (tensor(*([zero] * N)) + tensor(*([one] * N))).unit()


def w_N(N):
    return (sum(tensor(*[one if i == j else zero for j in range(N)]) for i in range(N))).unit()


def vn_entropy_subset(rho, keep):
    return entropy_vn(ptrace(rho, keep), base=2)


def entropy_map_2body(rho, N):
    M = np.zeros((N, N))
    for i in range(N):
        # Calculate the diagonal elements of M
        M[i, i] = round(vn_entropy_subset(rho, [i]), 12)

    for i in range(N):
        # Calculate the off-diagonal elements of M
        for j in range(N):
            if i == j:
                continue
            M[i, j] = round(vn_entropy_subset(rho, [i, j]), 12)
    return M


def plot_entropy_heatmap(M, title, save=""):
    plt.figure(figsize=(5, 5))
    im = plt.imshow(M, interpolation="nearest")
    plt.colorbar(im, label="Entropy (bits)")
    plt.xticks(range(M.shape[0]))
    plt.yticks(range(M.shape[0]))
    plt.title(title)
    plt.tight_layout()
    if save:
        plt.savefig(save, dpi=300)
    plt.close()


def plot_heatmap(psi):
    rho = ket2dm(psi)
    M = entropy_map_2body(rho, 4)
    plot_entropy_heatmap(M, "sigma sigma boyyy")


def avg_entropy_for_k(rho, N, k):
    entropies = []
    for keep in combinations(range(N), k):
        entropies.append(vn_entropy_subset(rho, list(keep)))
    return np.mean(entropies)


def plot_entropy_k(N, save=""):
    ks = range(1, N)
    rho_w, rho_ghz = ket2dm(w_N(N)), ket2dm(ghz_N(N))

    avg_entropy_w = [avg_entropy_for_k(rho_w, N, k) for k in ks]
    avg_entropy_ghz = [avg_entropy_for_k(rho_ghz, N, k) for k in ks]

    plt.figure(figsize=(6, 4))
    plt.plot(ks, avg_entropy_ghz, "o-", label="GHZ")
    plt.plot(ks, avg_entropy_w, "s-", label="W")
    plt.xlabel("Subsystem size k")
    plt.ylabel("Average entropy (bits)")
    plt.title(f"Average Subsystem Entropy vs k (N = {N})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    if save:
        plt.savefig(save, dpi=300)
    plt.close()


def remove_one_qubit(rho, N):
    return ptrace(rho, list(range(1, N)))


def main():
    np.set_printoptions(precision=4, suppress=True)
    plot_entropy_k(8, "average_entropy_vs_k_8")

    for N in range(3, 9):
        states = [(f"Zero_{N}", tensor([zero] * N)), (f"GHZ_{N}", ghz_N(N)), (f"W_{N}", w_N(N))]
        for name, psi in states:
            rho = ket2dm(psi)
            M = entropy_map_2body(rho, N)
            plot_entropy_heatmap(M, "Heatmap: " + name, f"heatmap_{name}_normal.png")

            rho_removed = remove_one_qubit(rho, N)
            M = entropy_map_2body(rho_removed, N - 1)
            plot_entropy_heatmap(M, f"Heatmap: Reduced Density Matrix of {name}", f"heatmap_{name}_reduced.png")
    plt.close("all")


if __name__ == "__main__":
    main()
