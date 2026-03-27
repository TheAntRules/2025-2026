from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# qc = QuantumCircuit(2, 2)

# qc.h(0)
# qc.x(1)
# qc.z(0)

# qc.draw("mpl")

# qc = QuantumCircuit(2)   #make a new circuit and overwrite the last example

# qc.h(0)        # put qubit 0 in superposition
# qc.cx(0, 1)    # CNOT Gate with control = 0, target = 1

# fig = qc.draw("mpl")
# plt.show()

# qc = QuantumCircuit(2)   #make a new circuit and overwrite the last example

# qc.h(0)        
# qc.h(1)
# qc.cz(0,1)  #Control Z with control = 0, target = 1

# fig = qc.draw("mpl")
# plt.show()

# qc = QuantumCircuit(3)

# qc.ccx(0, 1, 2)   # controls = 0,1  target = 2

# fig = qc.draw("mpl")
# plt.show()

# qc = QuantumCircuit(4)

# controls = [0, 1, 2]              # Set control qubits
# target = 3                        # Set target qubit
# qc.mcx(controls, target)          # Perform a multi-controled X

# from qiskit.circuit.library import ZGate     #import ZGate details

# ccz =ZGate().control(2)           #make a custom Z Gate with two controls
# qc.append(ccz,[0,1,2])            #add our new ccz gate to circut
#                                   #gate has controls = [0,1], target = 2
# fig = qc.draw("mpl")
# plt.show()

# qc = QuantumCircuit(3)

# qc.x(0)
# qc.ccx(0, 1, 2)   # controls = 0,1  target = 2
# qc.x(0)

# fig = qc.draw("mpl")
# plt.show()

# qc=QuantumCircuit(2)

# qc.h(0)        #make a Bell State
# qc.cx(0,1)

# from qiskit_aer import Aer                    #import necessary Statevector methods
# from qiskit.quantum_info import Statevector

# sv = Statevector.from_instruction(qc)
# print(sv)

from qiskit_aer import Aer

qc=QuantumCircuit(2)

qc.h(0)        #make a Bell State
qc.cx(0,1)
qc.measure_all()

backend = Aer.get_backend("aer_simulator")
result = backend.run(qc, shots=2000).result()
counts = result.get_counts()
print(counts)      #These counts should change slightly each time you execute the code

from qiskit.visualization import plot_histogram
plot_histogram(counts)
plt.show()