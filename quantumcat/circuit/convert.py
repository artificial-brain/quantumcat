from qiskit import QuantumCircuit
from quantumcat.utils import gates_map
from quantumcat.circuit.op_type import OpType
import cirq


def to_qiskit(q_circuit, qubits, cbits):
    operations = q_circuit.operations
    qiskit_qc = QuantumCircuit(qubits, cbits)
    for op in operations:
        operation = next(iter(op.items()))
        qiskit_op = gates_map.quantumcat_to_qiskit[operation[1]]
        qargs = operation[0]
        if qiskit_op == OpType.measure:
            qiskit_qc.measure([qargs], [op['cbit']])
        else:
            qiskit_qc.append(qiskit_op(), [qargs])
    return qiskit_qc


def to_cirq(q_circuit, qubits, cbits):
    operations = q_circuit.operations
    cirq_qc = cirq.Circuit()
    lined_qubits = cirq.LineQubit.range(qubits)
    for op in operations:
        operation = next(iter(op.items()))
        qiskit_op = gates_map.quantumcat_to_cirq[operation[1]]
        qargs = operation[0]
        if qiskit_op == OpType.measure:
            cirq_qc.append(cirq.ops.measure(lined_qubits[qargs]))
        else:
            cirq_qc.append([qiskit_op(lined_qubits[qargs])])
    return cirq_qc


def to_q_sharp(q_circuit, qubits, cbits):
    pass




