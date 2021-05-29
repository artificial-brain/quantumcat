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

from quantumcat.gates.custom_gates.cirq import UGate, U1Gate, U2Gate, U3Gate, RXXGate, RXGate, \
                                               RCCXGate, RC3XGate, RGate, CYGate, PGate, SXDGate, SDGGate, \
                                               SXGate, TDGate, RYGate, RYYGate, RZXGate, RZZGate, RZGate, \
                                               CUGate, CU1Gate, CU3Gate, DCXGate, CHGate, CPhaseGate, \
                                               CRXGate, CRYGate, CRZGate, CSXGate, C3XGate, C3SXGate, \
                                               C4XGate

from quantumcat.circuit.op_type import OpType
from quantumcat.utils import gates_map

def is_custom_class(obj):
    if isinstance(obj, UGate) or isinstance(obj, U1Gate) or isinstance(obj, U2Gate) or isinstance(obj, U3Gate) or \
            isinstance(obj, RXXGate) or isinstance(obj, SXDGate) or isinstance(obj, SDGGate) or \
            isinstance(obj, SXGate) or isinstance(obj, TDGate) or isinstance(obj, RXGate) or \
            isinstance(obj, RCCXGate) or isinstance(obj, RC3XGate) or isinstance(obj, RGate) or \
            isinstance(obj, CYGate) or isinstance(obj, PGate) or isinstance(obj, RYGate) or \
            isinstance(obj, RYYGate) or isinstance(obj, RZXGate) or isinstance(obj, RZZGate) or \
            isinstance(obj, RZGate) or isinstance(obj, CUGate) or isinstance(obj, CU1Gate) or \
            isinstance(obj, CU3Gate) or isinstance(obj, DCXGate) or isinstance(obj, CHGate) or \
            isinstance(obj, CPhaseGate) or isinstance(obj, CRXGate) or isinstance(obj, CRYGate) or \
            isinstance(obj, CRZGate) or isinstance(obj, CSXGate) or isinstance(obj, C3XGate) or \
            isinstance(obj, C3SXGate) or isinstance(obj, C4XGate):
        return True
    else:
        return False


def num_of_measurements(operations):
    return sum(1 for op in operations if gates_map.quantumcat_to_qiskit[next(iter(op.items()))[0]] == OpType.measure)

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


def bitstring(bits):
    return "".join(str(int(b)) for b in bits)


def measure_qubits_index(operations):
    qubits_index = []
    for op in operations:
        operation = next(iter(op.items()))
        qiskit_op = gates_map.quantumcat_to_qiskit[operation[0]]
        qargs = operation[1]

        if qiskit_op == OpType.measure:
            qubits_index.append('q' + str(qargs[0]))
    return qubits_index


def binary_to_decimal(binary_num):
    return int(binary_num, 2)


def cirq_measurment_in_reverse(results):
    result_dict = {}
    for result in results:
        result_dict[reverse_binary(result)] = results[result]
    return result_dict


def reverse_binary(num):
    return num[::-1]
