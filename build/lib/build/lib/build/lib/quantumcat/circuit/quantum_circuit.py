import qiskit
import cirq
from quantumcat import config


class QuantumCircuit:

    def __init__(self, num_qubits=1, num_classic_bits=0, provider='IBM'):
        super(QuantumCircuit, self).__init__()
        self.provider = provider
        config.provider = provider
        self.num_qubits = num_qubits
        self.num_classic_bits = num_classic_bits

    def create(self):
        if self.provider == 'IBM':
            quantum_circuit = QuantumCircuit(self.num_qubits, self.num_classic_bits)
        elif self.provider == 'Google':
            quantum_circuit = cirq.Circuit(cirq.LineQubit.range(self.num_qubits))
        return quantum_circuit


