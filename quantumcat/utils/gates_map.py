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
    # OpType.ecr_gate: standard_gates.ECRGate,
    OpType.s_gate: standard_gates.s.SGate,
    OpType.sdg_gate: standard_gates.s.SdgGate,
    OpType.swap_gate: standard_gates.swap.SwapGate,
    OpType.iswap_gate: standard_gates.iswap.iSwapGate,
    OpType.sx_gate: standard_gates.sx.SXGate,
    OpType.sxd_gate: standard_gates.sx.SXdgGate,
    OpType.t_gate: standard_gates.t.TGate,
    OpType.td_gate: standard_gates.t.TdgGate,
    OpType.u_gate: standard_gates.u.UGate,
    OpType.u1_gate: standard_gates.u1.U1Gate,
    OpType.u2_gate: standard_gates.u2.U2Gate,
    OpType.u3_gate: standard_gates.u3.U3Gate,
    OpType.cy_gate: standard_gates.y.CYGate,
    OpType.cz_gate: standard_gates.z.CZGate,
    OpType.i_gate: standard_gates.i.IGate,
    OpType.rxx_gate: standard_gates.rxx.RXXGate,
    OpType.rx_gate: standard_gates.rx.RXGate,
    OpType.rzz_gate: standard_gates.rzz.RZZGate,
    OpType.rzx_gate: standard_gates.rzx.RZXGate,
    OpType.r_gate: standard_gates.r.RGate,
    OpType.p_gate: standard_gates.p.PhaseGate,
    OpType.dcx_gate: standard_gates.dcx.DCXGate,
    OpType.c3x_gate: standard_gates.x.C3XGate,
    OpType.c3sx_gate: standard_gates.x.C3SXGate,
    OpType.c4x_gate: standard_gates.x.C4XGate,
    OpType.ch_gate: standard_gates.h.CHGate,
    OpType.csx_gate: standard_gates.sx.CSXGate,
    OpType.cswap_gate: standard_gates.swap.CSwapGate,
    OpType.cphase_gate: standard_gates.p.CPhaseGate,
    OpType.crx_gate: standard_gates.rx.CRXGate,
    OpType.cry_gate: standard_gates.ry.CRYGate,
    OpType.crz_gate: standard_gates.rz.CRZGate,
    OpType.cu_gate: standard_gates.u.CUGate,
    OpType.cu1_gate: standard_gates.u1.CU1Gate,
    OpType.cu3_gate: standard_gates.u3.CU3Gate,
    OpType.mct_gate: OpType.mct_gate,
    OpType.measure: OpType.measure,
}

quantumcat_to_cirq = {
    OpType.x_gate: ops.pauli_gates.X,
    OpType.y_gate: ops.pauli_gates.Y,
    OpType.z_gate: ops.pauli_gates.Z,
    OpType.cx_gate: ops.common_gates.CNOT,
    OpType.ccx_gate: ops.three_qubit_gates.CCNOT,
    OpType.h_gate: ops.common_gates.H,
    OpType.rzz_gate: custom_gates.cirq.RZZGate,
    OpType.rzx_gate: custom_gates.cirq.RZXGate,
    OpType.s_gate: ops.common_gates.S,
    OpType.sdg_gate: custom_gates.cirq.SDGGate,
    OpType.swap_gate: ops.swap_gates.SWAP,
    OpType.iswap_gate: ops.swap_gates.ISWAP,
    OpType.sxd_gate: custom_gates.cirq.SXDGate,
    OpType.t_gate: ops.common_gates.T,
    OpType.td_gate: custom_gates.cirq.TDGate,
    OpType.cz_gate: ops.common_gates.CZ,
    OpType.i_gate: ops.identity.I,
    OpType.cy_gate: custom_gates.cirq.CYGate,
    OpType.p_gate: custom_gates.cirq.PGate,
    OpType.sx_gate: custom_gates.cirq.SXGate,
    OpType.u_gate: custom_gates.cirq.UGate,
    OpType.u1_gate: custom_gates.cirq.U1Gate,
    OpType.u2_gate: custom_gates.cirq.U2Gate,
    OpType.u3_gate: custom_gates.cirq.U3Gate,
    OpType.rxx_gate: custom_gates.cirq.RXXGate,
    OpType.r_gate: custom_gates.cirq.RGate,
    OpType.rx_gate: custom_gates.cirq.RXGate,
    OpType.c3x_gate: custom_gates.cirq.C3XGate,
    OpType.c3sx_gate: custom_gates.cirq.C3SXGate,
    OpType.c4x_gate: custom_gates.cirq.C4XGate,
    OpType.dcx_gate: custom_gates.cirq.DCXGate,
    OpType.ch_gate: custom_gates.cirq.CHGate,
    OpType.crx_gate: custom_gates.cirq.CRXGate,
    OpType.cry_gate: custom_gates.cirq.CRYGate,
    OpType.crz_gate: custom_gates.cirq.CRZGate,
    OpType.csx_gate: custom_gates.cirq.CSXGate,
    OpType.cphase_gate: custom_gates.cirq.CPhaseGate,
    OpType.cu_gate: custom_gates.cirq.CUGate,
    OpType.cu1_gate: custom_gates.cirq.CU1Gate,
    OpType.cu3_gate: custom_gates.cirq.CU3Gate,
    OpType.cswap_gate: ops.three_qubit_gates.CSWAP,
    OpType.mct_gate: OpType.mct_gate,
    OpType.measure: OpType.measure,
}
