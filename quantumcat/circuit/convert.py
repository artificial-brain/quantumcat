from qiskit import QuantumCircuit
from quantumcat.utils import gates_map


def to_qiskit(q_circuit, qubits, cbits):
    operations = q_circuit.operations
    qiskit_qc = QuantumCircuit(qubits, cbits)
    for index in operations:
        operation = next(iter(index.items()))
        qiskit_op = gates_map.quantumcat_to_qiskit[operation[1]]
        qargs = operation[0]
        qiskit_qc.append(qiskit_op(), [qargs])
    return qiskit_qc


def to_cirq(q_circuit, qubits, cbits):
    pass


def to_q_sharp(q_circuit, qubits, cbits):
    pass




