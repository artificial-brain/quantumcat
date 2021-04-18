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
from quantumcat.gates import custom_gates

quantumcat_to_qiskit = {
    OpType.x_gate: standard_gates.x.XGate,
    OpType.y_gate: standard_gates.y.YGate,
    OpType.z_gate: standard_gates.z.ZGate,
    OpType.cx_gate: standard_gates.x.CXGate,
    OpType.ccx_gate: standard_gates.x.CCXGate,
    OpType.h_gate: standard_gates.h.HGate,
    OpType.rzz_gate: standard_gates.rzz.RZZGate,
    OpType.rzx_gate: standard_gates.rzx.RZXGate,
    # OpType.ecr_gate: standard_gates.ECRGate,
    OpType.s_gate: standard_gates.s.SGate,
    OpType.swap_gate: standard_gates.swap.SwapGate,
    OpType.iswap_gate: standard_gates.iswap.iSwapGate,
    OpType.sx_gate: standard_gates.sx.SXGate,
    OpType.sxd_gate: standard_gates.SXdgGate,
    OpType.t_gate: standard_gates.t.TGate,
    OpType.td_gate: standard_gates.TdgGate,
    OpType.u_gate: standard_gates.u.UGate,
    OpType.u1_gate: standard_gates.u1.U1Gate,
    OpType.u2_gate: standard_gates.u2.U2Gate,
    OpType.u3_gate: standard_gates.u3.U3Gate,
    OpType.measure: OpType.measure,
}

quantumcat_to_cirq = {
    OpType.x_gate: ops.pauli_gates.X,
    OpType.y_gate: ops.pauli_gates.Y,
    OpType.z_gate: ops.pauli_gates.Z,
    OpType.cx_gate: ops.common_gates.CNOT,
    OpType.ccx_gate: ops.three_qubit_gates.CCNOT,
    OpType.h_gate: ops.common_gates.H,
    OpType.u_gate: custom_gates.cirq.UGate,
    OpType.measure: OpType.measure,
}
