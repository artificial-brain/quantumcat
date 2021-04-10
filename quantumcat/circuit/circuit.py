from quantumcat.circuit.op_type import OpType
from quantumcat.exceptions import CircuitError
from quantumcat.utils import ErrorMessages
from quantumcat.circuit import convert
from quantumcat.utils import providers


class QCircuit:
    """docstring for Circuit."""

    def __init__(self, qubits, cbits):
        super(QCircuit, self).__init__()
        self.qubits = qubits
        self.cbits = cbits
        self.operations = []
        self.converted_q_circuit = None
        self.provider = None

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
            raise CircuitError(ErrorMessages.qubit_out_of_bound)

    def draw_circuit(self, provider=providers.IBM_PROVIDER):
        if self.converted_q_circuit is None or self.provider != provider:
            self.provider = provider
            converted_q_circuit = self.convert_circuit()
            self.converted_q_circuit = converted_q_circuit

        if self.provider == providers.IBM_PROVIDER:
            print(self.converted_q_circuit.draw())
        elif self.provider == providers.GOOGLE_PROVIDER:
            pass
        elif self.provider == providers.MICROSOFT_PROVIDER:
            pass

    def convert_circuit(self):
        converted_q_circuit = None
        if self.provider == providers.IBM_PROVIDER:
            converted_q_circuit = convert.to_qiskit(self, self.qubits, self.cbits)
        elif self.provider == providers.GOOGLE_PROVIDER:
            converted_q_circuit = convert.to_cirq(self, self.qubits, self.cbits)
        if self.provider == providers.MICROSOFT_PROVIDER:
            converted_q_circuit = convert.to_q_sharp(self, self.qubits, self.cbits)
        return converted_q_circuit
