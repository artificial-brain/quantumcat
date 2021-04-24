from quantumcat.gate import XGate
from quantumcat import config
import cirq
from quantumcat.circuit.circuit import QuantumCircuit

if __name__ == '__main__':
    quantum_circuit = QuantumCircuit(2,2)
    print(quantum_circuit)
