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
import inspect


def to_qiskit(q_circuit, qubits, cbits):
    """This function converts quantumcat circuit into qiskit circuit.
    :param q_circuit: quantumcat circuit object that needs to be converted to qiskit circuit object
    :param qubits: number of qubits to create qiskit circuit
    :param cbits: number of classical bits for measurement
    :return: qiskit quantumcircuit object
    """
    operations = q_circuit.operations
    qiskit_qc = QuantumCircuit(qubits, cbits)
    for op in operations:
        params = []
        operation = next(iter(op.items()))
        qiskit_op = gates_map.quantumcat_to_qiskit[operation[0]]
        qargs = operation[1]
        if constants.PARAMS in op:
            params = (op[constants.PARAMS])

        if qiskit_op == OpType.measure:
            qiskit_qc.measure(qargs[0], qargs[1])
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
            qubit = named_qubits[qargs[0][0]]
            cirq_qc.append(cirq.ops.measure(qubit))
        elif cirq_op == OpType.mct_gate:
            mct_named_qubits = named_qubits_for_multi_controlled_op(named_qubits, qargs)
            cirq_qc.append([cirq.ops.X(mct_named_qubits[1]).controlled_by(*mct_named_qubits[0])])
          # Find a better way to replace the following if
        elif len(params) > 0 or (inspect.isclass(cirq_op) and helper.is_custom_class(cirq_op())):
            cirq_qc.append([cirq_op(*params).on(*named_qubits_for_ops(named_qubits, qargs))])
        else:
            cirq_qc.append([cirq_op(*named_qubits_for_ops(named_qubits, qargs))])

    return cirq_qc


def to_q_sharp(q_circuit, qubits, cbits):
    pass


def named_qubits_for_ops(named_qubits, qargs):
    """This function creates NamedQubit array for cirq operations based on the number of qubits required for
    that particular operation. Ex: x_gate -> 1 NamedQubit, cx_gate -> 2 NamedQubit
    :param named_qubits: NamedQubit for the entire circuit
    :param qargs: qubits of a operation
    :return: NamedQubit array based on the qargs
    """
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

def named_qubits_for_multi_controlled_op(named_qubits, qargs):
    mct_named_qubits = []
    for j in range(len(named_qubits)):
        if named_qubits[j].name == 'q' + str(qargs[1][0]):
            target_qubit = named_qubits[j]

    control_qubits = []
    for i in range(len(qargs[0])):
        for j in range(len(named_qubits)):
            if named_qubits[j].name == 'q' + str(qargs[0][i]):
                control_qubits.append(named_qubits[j])

    mct_named_qubits.append(control_qubits)
    mct_named_qubits.append(target_qubit)

    return mct_named_qubits

