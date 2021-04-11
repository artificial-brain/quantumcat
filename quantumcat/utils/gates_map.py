from quantumcat.circuit.op_type import OpType
from qiskit.circuit.library.standard_gates.x import XGate
from qiskit.circuit.library.standard_gates.y import YGate
from qiskit.circuit.library.standard_gates.z import ZGate
from cirq import ops

quantumcat_to_qiskit = {
    OpType.x_gate: XGate,
    OpType.y_gate: YGate,
    OpType.z_gate: ZGate,
    OpType.measure: OpType.measure,
}

quantumcat_to_cirq = {
    OpType.x_gate: ops.pauli_gates.X,
    OpType.y_gate: ops.pauli_gates.Y,
    OpType.z_gate: ops.pauli_gates.Z,
    OpType.measure: OpType.measure,
}
