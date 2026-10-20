import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

N=3   #number of qubits
qc=QuantumCircuit(N)

#*********************
# You add in N Hardamards, try using a for loop
#*********************
for i in range(N):
    qc.h(i)
qc.barrier()      #this just puts a vertical line in the circuit to separate the code

#*********************
# You add in the ccz gate based phase oracle
#*********************

def select111():
    qc.ccz(0, 1, 2)   # controls = 0,1  target = 2

def select100():
    qc.x(0)
    qc.x(1)
    qc.ccz(0,1,2)
    qc.x(0)
    qc.x(1)

def select101():
    qc.x(1)
    qc.ccz(0,1,2)
    qc.x(1)

def select110():
    qc.x(0)
    qc.ccz(0,1,2)
    qc.x(0)

def select3rd():
    select110()
    select101()
    qc.x(2)
    qc.ccz(0,1,2)
    qc.x(2)

select3rd()




qc.barrier()
#*********************
# You add in the Diffuser here
#*********************
for i in range(N):
    qc.h(i)
    qc.x(i)

qc.ccz(0, 1, 2)   # controls = 0,1  target = 2

for i in range(N):
    qc.x(i)
    qc.h(i)

qc.barrier()
#********************
# Perform Shot-based Measurements
#*******************
qc.measure_all()                                  #add in measurements for all qubits

backend = Aer.get_backend("aer_simulator")
result = backend.run(qc, shots=4000).result()
counts = result.get_counts()

plot_histogram(counts)
plt.show()

#********************
# Draw Circuit
#*******************
fig = qc.draw("mpl")
plt.show()
