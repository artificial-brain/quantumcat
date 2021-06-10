# (C) Copyright Artificial Brain 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from qiskit import QuantumCircuit
from quantumcat.utils import gates_map
from quantumcat.circuit.op_type import OpType
from quantumcat.utils import constants, helper
import cirq
from braket.circuits import Circuit, Instruction
from braket.circuits.result_type import ResultType
import inspect


def to_qiskit(q_circuit, qubits):
    """This function converts quantumcat circuit into qiskit circuit.
    :param q_circuit: quantumcat circuit object that needs to be converted to qiskit circuit object
    :param qubits: number of qubits to create qiskit circuit
    :param cbits: number of classical bits for measurement
    :return: qiskit quantumcircuit object
    """
    operations = q_circuit.operations
    num_of_measurements = helper.num_of_measurements(operations)
    qiskit_qc = QuantumCircuit(qubits, qubits) if num_of_measurements > 0 else QuantumCircuit(qubits)
    for op in operations:
        params = []
        operation = next(iter(op.items()))
        qiskit_op = gates_map.quantumcat_to_qiskit[operation[0]]
        qargs = operation[1]
        if constants.PARAMS in op:
            params = (op[constants.PARAMS])

        if qiskit_op == OpType.measure:
            qiskit_qc.measure(qargs, qargs[0])
        elif qiskit_op == OpType.measure_all:
            qiskit_qc.measure_all()
        elif qiskit_op == OpType.mct_gate:
            qiskit_qc.mcx(control_qubits=qargs[0], target_qubit=qargs[1],
                          ancilla_qubits=qargs[2], mode=qargs[3])
        else:
            qiskit_qc.append(qiskit_op(*params), qargs)

    return qiskit_qc


def to_cirq(q_circuit, qubits):
    """This function converts quantumcat circuit into qiskit circuit.
    :param q_circuit: quantumcat circuit object that needs to be converted to qiskit circuit object
    :param qubits: number of qubits to create qiskit circuit
    :return: qiskit quantumcircuit object
    """
    operations = q_circuit.operations
    cirq_qc = cirq.Circuit()
    named_qubits = cirq.NamedQubit.range(qubits, prefix='q')
    for op in operations:
        params = []
        operation = next(iter(op.items()))
        cirq_op = gates_map.quantumcat_to_cirq[operation[0]]
        qargs = operation[1]
        if constants.PARAMS in op:
            params = (op[constants.PARAMS])

        if cirq_op == OpType.measure:
            qubit = named_qubits[qargs[0]]
            cirq_qc.append(cirq.ops.measure(qubit))
        elif cirq_op == OpType.measure_all:
            cirq_qc.append(cirq.ops.measure(*named_qubits, key='result'))
        elif cirq_op == OpType.mct_gate:
            mct_named_qubits = helper.named_qubits_for_multi_controlled_op(named_qubits, qargs)
            cirq_qc.append([cirq.ops.X(mct_named_qubits[1]).controlled_by(*mct_named_qubits[0])])
        # Find a better way to replace the following if
        elif len(params) > 0 or (inspect.isclass(cirq_op) and helper.is_custom_class(cirq_op())):
            cirq_qc.append([cirq_op(*params).on(*helper.named_qubits_for_ops(named_qubits, qargs))])
        else:
            cirq_qc.append([cirq_op(*helper.named_qubits_for_ops(named_qubits, qargs))])

    return cirq_qc


def to_q_sharp(q_circuit, qubits, cbits):
    pass


def to_braket(q_circuit, qubits):
    operations = q_circuit.operations
    braket_qc = Circuit()
    for op in operations:
        params = []
        instructor = []
        operation = next(iter(op.items()))
        braket_op = gates_map.quantumcat_to_braket[operation[0]]
        qargs = operation[1]
        if constants.PARAMS in op:
            params = (op[constants.PARAMS])

        if braket_op == OpType.measure:
            braket_qc.add(ResultType.Probability(target=[qargs[0]]))
        elif braket_op == OpType.measure_all:
            braket_qc.add(ResultType.Probability)
        else:
            braket_qc.add([Instruction(braket_op(*params), qargs)])

    return braket_qc
