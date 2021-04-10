from qiskit import QuantumCircuit
from quantumcat.circuit.op_type import OpType


def to_qiskit(q_circuit, qubits, cbits):
    operations = q_circuit.operations
    qiskit_qc = QuantumCircuit(qubits, cbits)
    for index in operations:
        operation = next(iter(index.items()))
        if operation[1] == OpType.x_gate:
            qiskit_qc.x(operation[0])
    return qiskit_qc


def to_cirq(q_circuit, qubits, cbits):
    pass


def to_q_sharp(q_circuit, qubits, cbits):
    pass




