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

import pytest
from quantumcat.circuit.circuit import QCircuit
from quantumcat.utils import providers, constants
import numpy as np


def measurementresult(circ):
    return circ.execute(provider=providers.IBM_PROVIDER, repetitions=10, simulator_name=constants.STATEVECTOR_SIMULATOR)


@pytest.fixture()
def circdef():
    circ = QCircuit(5)
    return circ


def test_x_gate(circdef):
    circdef.x_gate(0)
    circdef.x_gate(1)
    circdef.x_gate(2)
    circdef.x_gate(3)
    circdef.x_gate(4)
    assert measurementresult(circdef).tolist() == [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j]


def test_y_gate(circdef):
    circdef.y_gate(0)
    circdef.y_gate(1)
    circdef.y_gate(2)
    circdef.y_gate(3)
    circdef.y_gate(4)
    assert measurementresult(circdef).tolist() == [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+1j]


def test_z_gate(circdef):
    circdef.z_gate(0)
    circdef.z_gate(1)
    circdef.z_gate(2)
    circdef.z_gate(3)
    circdef.z_gate(4)
    assert measurementresult(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_h_gate(circdef):
    circdef.h_gate(0)
    circdef.h_gate(1)
    circdef.h_gate(2)
    circdef.h_gate(3)
    circdef.h_gate(4)
    assert np.round(measurementresult(circdef), 3).tolist() == [0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j]


def test_cx_gate(circdef):
    circdef.cx_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_cz_gate(circdef):
    circdef.cz_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_ccx_gate(circdef):
    circdef.ccx_gate(0, 1, 2)
    circdef.measure(0,)
    circdef.measure(1)
    circdef.measure(2)
    assert True


def test_ry_gate(circdef):
    circdef.ry_gate(30, 0)
    circdef.measure(0)
    assert True


def test_ryy_gate(circdef):
    circdef.ryy_gate(45, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_rzz_gate(circdef):
    circdef.rzz_gate(60, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_rzx_gate(circdef):
    circdef.rzx_gate(60, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_rz_gate(circdef):
    circdef.rz_gate(60, 0)
    circdef.measure(0)
    assert True


def test_s_gate(circdef):
    circdef.s_gate(0)
    circdef.measure(0)
    assert True


def test_sdg_gate(circdef):
    circdef.sdg_gate(0)
    circdef.measure(0)
    assert True


def test_swap_gate(circdef):
    circdef.swap_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_iswap_gate(circdef):
    circdef.iswap_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_sx_gate(circdef):
    circdef.sx_gate(0)
    circdef.measure(0)
    assert True


def test_sxd_gate(circdef):
    circdef.sxd_gate(0)
    circdef.measure(0)
    assert True


def test_t_gate(circdef):
    circdef.t_gate(0)
    circdef.measure(0)
    assert True


def test_td_gate(circdef):
    circdef.td_gate(0)
    circdef.measure(0)
    assert True


def test_u_gate(circdef):
    circdef.u_gate(30, 45, 60, 0)
    circdef.measure(0)
    assert True


def test_u1_gate(circdef):
    circdef.u1_gate(45, 0)
    circdef.measure(0)
    assert True


def test_u2_gate(circdef):
    circdef.u2_gate(60, 30, 0)
    circdef.measure(0)
    assert True


def test_u3_gate(circdef):
    circdef.u3_gate(30, 45, 60, 0)
    circdef.measure(0)
    assert True


def test_cy_gate(circdef):
    circdef.cy_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_i_gate(circdef):
    circdef.i_gate(0)
    circdef.measure(0)
    assert True


def test_rccx_gate(circdef):
    circdef.rccx_gate(0, 1, 2)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    assert True
    
    
def test_rc3x_gate(circdef):
    circdef.rc3x_gate(0, 1, 2, 3)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    circdef.measure(3)
    assert True


def test_rxx_gate(circdef):
    circdef.rxx_gate(60, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_rx_gate(circdef):
    circdef.rx_gate(30, 0)
    circdef.measure(0)
    assert True


def test_r_gate(circdef):
    circdef.r_gate(30, 60, 0)
    circdef.measure(0)
    assert True


def test_p_gate(circdef):
    circdef.p_gate(30, 0)
    circdef.measure(0)
    assert True


def test_c3x_gate(circdef):
    circdef.c3x_gate(0, 1, 2, 3)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    circdef.measure(3)
    assert True


def test_c3sx_gate(circdef):
    circdef.c3sx_gate(0, 1, 2, 3)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    circdef.measure(3)
    assert True


def test_c4x_gate(circdef):
    circdef.c4x_gate(0, 1, 2, 3, 4)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    circdef.measure(3)
    circdef.measure(4)
    assert True


def test_dcx_gate(circdef):
    circdef.dcx_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_ch_gate(circdef):
    circdef.ch_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_csx_gate(circdef):
    circdef.csx_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_cswap_gate(circdef):
    circdef.cswap_gate(0, 1, 2)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    assert True


def test_cphase_gate(circdef):
    circdef.cphase_gate(30, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_crx_gate(circdef):
    circdef.crx_gate(30, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_cry_gate(circdef):
    circdef.cry_gate(30, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_crz_gate(circdef):
    circdef.crz_gate(30, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_cu_gate(circdef):
    circdef.cu_gate(30, 45, 60, 10, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_cu1_gate(circdef):
    circdef.cu1_gate(30, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_cu3_gate(circdef):
    circdef.cu3_gate(30, 45, 60, 0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_mcx_gate(circdef):
    circdef.mcx_gate([0, 1], 2, [3, 4])
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    assert True


def test_mcxgc_gate(circdef):
    circdef.mcxgc_gate([0, 1], 2)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    assert True


def test_mcxvchain_gate(circdef):
    circdef.mcxvchain_gate([0, 1], 2, [3, 4])
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    assert True


def test_mcxrec_gate(circdef):
    circdef.mcxrec_gate([0, 1], 2)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    assert True


def test_mcp_gate(circdef):
    circdef.mcp_gate(30, [0, 1], 2)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    assert True


def test_mct_gate(circdef):
    circdef.mct_gate([0, 1], 2, [3, 4])
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    assert True
