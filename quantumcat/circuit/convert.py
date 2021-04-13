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
        if qiskit_op == OpType.measure:
            qiskit_qc.measure(qargs[0], qargs[1])
        else:
            qiskit_qc.append(qiskit_op(), qargs)

    return qiskit_qc


def to_cirq(q_circuit, qubits):
    operations = q_circuit.operations
    cirq_qc = cirq.Circuit()
    named_qubits = cirq.NamedQubit.range(qubits, prefix='q')
    for op in operations:
        operation = next(iter(op.items()))
        cirq_op = gates_map.quantumcat_to_cirq[operation[0]]
        qargs = operation[1]
        if cirq_op == OpType.measure:
            qubit = named_qubits[qargs[0][0]]
            cirq_qc.append(cirq.ops.measure(qubit))
        else:
            cirq_qc.append([cirq_op(*named_qubits_for_ops(named_qubits, qargs))])

    return cirq_qc


def to_q_sharp(q_circuit, qubits, cbits):
    pass


def named_qubits_for_ops(named_qubits, qargs):
    op_named_qubits = []
    if len(qargs) > 1:
        for i in range(len(qargs)):
            for j in range(len(named_qubits)):
                if named_qubits[j].name == 'q' + str(qargs[i][0]):
                    op_named_qubits.append(named_qubits[j])
    else:
        for j in range(len(named_qubits)):
            if named_qubits[j].name == 'q' + str(qargs[0]):
                op_named_qubits.append(named_qubits[j])

    return op_named_qubits





