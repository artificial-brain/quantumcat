import cirq
from quantumcat import config
from qiskit import QuantumCircuit


class Circuit:

    def __init__(self, num_qubits=1, num_classic_bits=0):
        super(Circuit, self).__init__()
        self.num_qubits = num_qubits
        self.num_classic_bits = num_classic_bits
        self.quantum_circuit = None

    def create(self):
        print(config.provider)
        if config.provider == 'IBMa':
            quantum_circuit = QuantumCircuit(self.num_qubits, self.num_classic_bits)
        elif config.provider == 'IBM':
            quantum_circuit = cirq.Circuit(cirq.LineQubit.range(self.num_qubits))
        self.quantum_circuit = quantum_circuit
        return quantum_circuit

    def ddraw(self):
        if self.provider == 'IBM':
            return self.quantum_circuit.draw()
        elif self.provider == 'Google':
            return print(self.quantum_circuit)





