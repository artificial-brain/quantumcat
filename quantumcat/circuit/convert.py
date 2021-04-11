from qiskit import QuantumCircuit
from quantumcat.utils import gates_map
from quantumcat.circuit.op_type import OpType


def to_qiskit(q_circuit, qubits, cbits):
    operations = q_circuit.operations
    qiskit_qc = QuantumCircuit(qubits, cbits)
    for index in operations:
        operation = next(iter(index.items()))
        qiskit_op = gates_map.quantumcat_to_qiskit[operation[1]]
        qargs = operation[0]
        if qiskit_op == OpType.measure:
            qiskit_qc.measure([qargs], [index['cbit']])
        else:
            qiskit_qc.append(qiskit_op(), [qargs])
    return qiskit_qc


def to_cirq(q_circuit, qubits, cbits):
    pass


def to_q_sharp(q_circuit, qubits, cbits):
    pass




