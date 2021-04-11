from quantumcat.circuit.op_type import OpType
from qiskit.circuit.library.standard_gates.x import XGate
from qiskit.circuit.library.standard_gates.y import YGate
from qiskit.circuit.library.standard_gates.z import ZGate

quantumcat_to_qiskit = {
    OpType.x_gate: XGate,
    OpType.y_gate: YGate,
    OpType.z_gate: ZGate,
    OpType.measure: OpType.measure,
}
