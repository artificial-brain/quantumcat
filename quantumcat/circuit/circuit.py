from quantumcat.circuit.op_type import OpType
from quantumcat.exceptions import CircuitError


class QCircuit:
    """docstring for Circuit."""

    def __init__(self, qubits, cbits):
        super(QCircuit, self).__init__()
        self.qubits = qubits
        self.cbits = cbits
        self.operations = []

    def x_gate(self, qubit):
        self.check_raise_error(qubit)
        self.operations.append({qubit: OpType.x_gate})

    def y_gate(self, qubit):
        self.check_raise_error(qubit)
        self.operations.append({qubit: OpType.y_gate})

    def z_gate(self, qubit):
        self.check_raise_error(qubit)
        self.operations.append({qubit: OpType.z_gate})

    def get_operations(self):
        return self.operations

    def check_raise_error(self, qubit):
        if qubit > (self.qubits - 1):
            raise CircuitError('Qubit is out of bound')
