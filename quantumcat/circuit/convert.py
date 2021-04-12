from qiskit import QuantumCircuit
from quantumcat.utils import gates_map
from quantumcat.circuit.op_type import OpType
import cirq


def to_qiskit(q_circuit, qubits, cbits):
    operations = q_circuit.operations
    qiskit_qc = QuantumCircuit(qubits, cbits)
    for op in operations:
        operation = next(iter(op.items()))
        qiskit_op = gates_map.quantumcat_to_qiskit[operation[0]]
        qargs = operation[1]
        print(qiskit_op, qargs)
        if qiskit_op == OpType.measure:
            qiskit_qc.measure(qargs[0], qargs[1])
        else:
            qiskit_qc.append(qiskit_op(), qargs)
    return qiskit_qc


def to_cirq(q_circuit, qubits, cbits):
    operations = q_circuit.operations
    cirq_qc = cirq.Circuit()
    named_qubits = cirq.NamedQubit.range(qubits, prefix='q')
    # print(operations)
    for op in operations:
        operation = next(iter(op.items()))
        cirq_op = gates_map.quantumcat_to_cirq[operation[0]]
        qargs = operation[1]
        if cirq_op == OpType.measure:
            qubit = named_qubits[qargs[0][0]]
            cirq_qc.append(cirq.ops.measure(qubit))
        else:
            pass
            # Need to complete below to support multi gates
            # print(named_qubits[qargs[i]] for i in range(qubits))
            # qubit = named_qubits[qargs[0]]
            # cirq_qc.append([cirq_op(j)])
    return cirq_qc


def to_q_sharp(q_circuit, qubits, cbits):
    pass




