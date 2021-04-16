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

from quantumcat.circuit.op_type import OpType
from qiskit.circuit.library import standard_gates
from cirq import ops

quantumcat_to_qiskit = {
    OpType.x_gate: standard_gates.x.XGate,
    OpType.y_gate: standard_gates.y.YGate,
    OpType.z_gate: standard_gates.z.ZGate,
    OpType.cx_gate: standard_gates.x.CXGate,
    OpType.h_gate: standard_gates.h.HGate,
    OpType.cz_gate: standard_gates.z.CZGate,
    OpType.mct_gate: OpType.mct_gate,
    OpType.measure: OpType.measure,
}

quantumcat_to_cirq = {
    OpType.x_gate: ops.pauli_gates.X,
    OpType.y_gate: ops.pauli_gates.Y,
    OpType.z_gate: ops.pauli_gates.Z,
    OpType.cx_gate: ops.common_gates.CNOT,
    OpType.h_gate: ops.common_gates.H,
    OpType.cz_gate: ops.common_gates.CZ,
    OpType.mct_gate: OpType.mct_gate,
    OpType.measure: OpType.measure,
}
