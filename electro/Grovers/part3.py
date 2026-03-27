import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

N=19   #number of qubits
qc=QuantumCircuit(N)

def anti_controlled_x(qc: QuantumCircuit, control: int, target: int):
    qc.x(control)
    qc.cx(control, target)
    qc.x(control)

def _maybe_x(qubit: int, flag: bool):
        if flag: qc.x(qubit)

def _compute_or2(qc: QuantumCircuit, a: int, neg_a: bool, b: int, neg_b: bool, target: int):
    _maybe_x(a, neg_a)
    qc.cx(a, target)
    _maybe_x(a, neg_a)

    _maybe_x(b, neg_b)
    qc.cx(b, target)
    _maybe_x(b, neg_b)

    _maybe_x(a, neg_a)
    _maybe_x(b, neg_b)
    qc.ccx(a, b, target)
    _maybe_x(a, neg_a)
    _maybe_x(b, neg_b)


def oracle_gate(n_comp: int, n_anc: int):
    n_total = n_comp + n_anc
    qc_oracle = QuantumCircuit(n_total)
    comp = list(range(n_comp))
    anc  = list(range(n_comp, n_total))

    #forward
    # 1: A
    qc_oracle.cx(comp[0], anc[0])                    # anc0 = A

    # 2: (A or NOT F) can be computed as NOT((NOT A) AND F)
    qc_oracle.x(comp[0])                             # flip A for anti-control
    qc_oracle.ccx(comp[0], comp[5], anc[1])          # anc1 = (NOT A) AND F
    qc_oracle.x(comp[0])                             # restore A
    qc_oracle.x(anc[1])                              # anc1 = NOT( (NOT A) AND F )

    # 3: (E or A)
    _compute_or2(qc_oracle, comp[4], False, comp[0], False, anc[2])

    # 4: (E or NOT A)
    _compute_or2(qc_oracle, comp[4], False, comp[0], True, anc[3])

    # 5: (C or D)
    _compute_or2(qc_oracle, comp[2], False, comp[3], False, anc[4])

    # 6: (C or NOT D)
    _compute_or2(qc_oracle, comp[2], False, comp[3], True, anc[5])

    # 7: (NOT B or C)
    _compute_or2(qc_oracle, comp[1], True,  comp[2], False, anc[6])

    # 8: (NOT B or NOT C)
    _compute_or2(qc_oracle, comp[1], True,  comp[2], True,  anc[7])

    # 9: (NOT D or E)
    _compute_or2(qc_oracle, comp[3], True,  comp[4], False, anc[8])

    # 10: (NOT D or NOT E)
    _compute_or2(qc_oracle, comp[3], True,  comp[4], True,  anc[9])

    # 11: (NOT A or C or E)
    # compute (NOT A OR C) into anc[10], then OR with E
    _compute_or2(qc_oracle, comp[0], True, comp[2], False, anc[10])
    _compute_or2(qc_oracle, anc[10], False, comp[4], False, anc[10])

    # 12: (NOT D or A or E)
    _compute_or2(qc_oracle, comp[3], True, comp[0], False, anc[11])
    _compute_or2(qc_oracle, anc[11], False, comp[4], False, anc[11])

    #reverse

    # undo clause 12
    _compute_or2(qc_oracle, anc[11], False, comp[4], False, anc[11])
    _compute_or2(qc_oracle, comp[3], True, comp[0], False, anc[11])
    # undo clause 11
    _compute_or2(qc_oracle, anc[10], False, comp[4], False, anc[10])
    _compute_or2(qc_oracle, comp[0], True, comp[2], False, anc[10])
    # undo clauses 10‑1 in reverse order
    _compute_or2(qc_oracle, comp[3], True,  comp[4], True,  anc[9])
    _compute_or2(qc_oracle, comp[3], True,  comp[4], False, anc[8])
    _compute_or2(qc_oracle, comp[1], True,  comp[2], True,  anc[7])
    _compute_or2(qc_oracle, comp[1], True,  comp[2], False, anc[6])
    _compute_or2(qc_oracle, comp[2], False, comp[3], True,  anc[5])
    _compute_or2(qc_oracle, comp[2], False, comp[3], False, anc[4])
    _compute_or2(qc_oracle, comp[4], False, comp[0], True,  anc[3])
    _compute_or2(qc_oracle, comp[4], False, comp[0], False, anc[2])
    qc_oracle.x(anc[1])                              # undo negation from step 2
    qc_oracle.x(comp[0])                             # restore A for step 2
    qc_oracle.ccx(comp[0], comp[5], anc[1])          # undo CCX from step 2
    qc_oracle.x(comp[0])                             # restore A for step 2
    qc_oracle.cx(comp[0], anc[0])                    # undo clause 1

    return qc_oracle.to_gate(label="Oracle")

def diffuser_gate(n_comp: int):
    qc_diff = QuantumCircuit(n_comp)
    # ... build diffuser using only computational qubits



    return qc_diff.to_gate(label="Diffuser")

fig = qc.draw("mpl")
plt.show()