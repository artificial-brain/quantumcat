import cirq
import config

class XGate():

    def __init__(self, quantum_circuit, qubit):
        super(XGate, self).__init__()
        self.provider = config.provider
        self.quantum_circuit = quantum_circuit
        self.qubit = qubit

    def apply(self):
        if self.provider == 'IBM':
             self.quantum_circuit.x(self.qubit)
             return self.quantum_circuit
        elif self.provider == 'Google':
             self.quantum_circuit.append(cirq.X(self.qubit))
             return self.quantum_circuit
