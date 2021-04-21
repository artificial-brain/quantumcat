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
    rxx_gate=13
    rx_gate=14
    r_gate=15
    p_gate=16
    rzz_gate = 42
    rzx_gate = 43
    ecr_gate = 44
    s_gate = 45
    sdg_gate = 46
    swap_gate = 47
    iswap_gate = 48
    sx_gate = 49
    sxd_gate = 50
    t_gate = 51
    td_gate = 52
    u_gate = 53
    u1_gate = 54
    u2_gate = 55
    u3_gate = 56
    rxx_gate=13
    rx_gate=14
    r_gate=15
    p_gate=16
    measure = 100
