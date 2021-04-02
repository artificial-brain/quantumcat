import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import config
import cirq


class XGate():
    """docstring for XGate."""

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
