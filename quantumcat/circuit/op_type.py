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

from enum import Enum


class OpType(Enum):
    """docstring for OpType."""

    x_gate = 1
    y_gate = 2
    z_gate = 3
    cx_gate = 4
    ccx_gate = 5
    mct_gate = 6
    h_gate = 7
    cy_gate = 8
    cz_gate = 9
    i_gate = 10
    rccx_gate = 11
    rc3x_gate = 12
    rxx_gate = 13
    rx_gate = 14
    r_gate = 15
    p_gate = 16
    mcp_gate = 17
    mcx_gate = 18
    mcxgc_gate = 19
    mcxrec_gate = 20
    mcxvchain_gate = 21
    dcx_gate = 22
    ch_gate = 23
    csx_gate = 24
    cswap_gate = 25
    cphase_gate = 26
    crx_gate = 27
    cry_gate = 28
    crz_gate = 29
    cu_gate = 30
    cu1_gate = 31
    cu3_gate = 32
    c3x_gate = 33
    c3sx_gate = 34
    c4x_gate = 35
    ry_gate = 36
    ryy_gate = 37
    rz_gate = 38
    rzz_gate = 39
    rzx_gate = 40
    ecr_gate = 41
    s_gate = 42
    sdg_gate = 43
    swap_gate = 44
    iswap_gate = 45
    sx_gate = 46
    sxd_gate = 47
    t_gate = 48
    td_gate = 49
    u_gate = 50
    u1_gate = 51
    u2_gate = 52
    u3_gate = 53
    measure = 100
    measure_all = 101
