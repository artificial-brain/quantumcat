import cirq
from quantumcat import config
from qiskit import QuantumCircuit


class Circuit:

    def __init__(self, num_qubits=1, num_classic_bits=0, provider='IBM'):
        super(Circuit, self).__init__()
        self.provider = provider
        config.provider = provider
        self.num_qubits = num_qubits
        self.num_classic_bits = num_classic_bits
        self.quantum_circuit = None

    def create(self):
        if self.provider == 'IBM':
            quantum_circuit = QuantumCircuit(self.num_qubits, self.num_classic_bits)
        elif self.provider == 'Google':
            quantum_circuit = cirq.Circuit(cirq.LineQubit.range(self.num_qubits))
        self.quantum_circuit = quantum_circuit
        return quantum_circuit

    def draw(self):
        if self.provider == 'IBM':
            self.quantum_circuit.draw()
        elif self.provider == 'Google':
            print(self.quantum_circuit)





