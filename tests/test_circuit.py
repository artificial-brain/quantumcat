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


def statevector(circ):
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
    assert statevector(circdef).tolist() == [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j]


def test_y_gate(circdef):
    circdef.y_gate(0)
    circdef.y_gate(1)
    circdef.y_gate(2)
    circdef.y_gate(3)
    circdef.y_gate(4)
    assert statevector(circdef).tolist() == [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+1j]


def test_z_gate(circdef):
    circdef.z_gate(0)
    circdef.z_gate(1)
    circdef.z_gate(2)
    circdef.z_gate(3)
    circdef.z_gate(4)
    assert statevector(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_h_gate(circdef):
    circdef.h_gate(0)
    circdef.h_gate(1)
    circdef.h_gate(2)
    circdef.h_gate(3)
    circdef.h_gate(4)
    assert np.round(statevector(circdef), 3).tolist() == [0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                          0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                          0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                          0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j]


def test_cx_gate(circdef):
    circdef.cx_gate(0, 1)
    circdef.cx_gate(1, 2)
    circdef.cx_gate(2, 3)
    circdef.cx_gate(3, 4)
    assert statevector(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_cz_gate(circdef):
    circdef.cz_gate(0, 1)
    circdef.cz_gate(1, 2)
    circdef.cz_gate(2, 3)
    circdef.cz_gate(3, 4)
    assert statevector(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.-0.j,
                                             0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.+0.j,
                                             0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.-0.j,
                                             -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.+0.j, -0.+0.j]


def test_ccx_gate(circdef):
    circdef.ccx_gate(0, 1, 2)
    circdef.ccx_gate(1, 2, 3)
    circdef.ccx_gate(2, 3, 4)
    assert statevector(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_ry_gate(circdef):
    circdef.ry_gate(np.pi/6, 0)
    circdef.ry_gate(np.pi/4, 1)
    circdef.ry_gate(np.pi/3, 2)
    circdef.ry_gate(np.pi/2, 3)
    circdef.ry_gate(2*np.pi/3, 4)
    assert np.round(statevector(circdef), 3).tolist() == [0.273+0j, 0.073+0j, 0.113+0j, 0.03+0j, 0.158+0j, 0.042+0j, 0.065+0j, 0.018+0j,
                                                          0.273+0j, 0.073+0j, 0.113+0j, 0.03+0j, 0.158+0j, 0.042+0j, 0.065+0j, 0.018+0j,
                                                          0.473+0j, 0.127+0j, 0.196+0j, 0.053+0j, 0.273+0j, 0.073+0j, 0.113+0j, 0.03+0j,
                                                          0.473+0j, 0.127+0j, 0.196+0j, 0.053+0j, 0.273+0j, 0.073+0j, 0.113+0j, 0.03+0j]


def test_ryy_gate(circdef):
    circdef.ryy_gate(np.pi/4, 0, 1)
    circdef.ryy_gate(np.pi/3, 1, 2)
    circdef.ryy_gate(np.pi/2, 2, 3)
    circdef.ryy_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector(circdef), 3).tolist() == np.round([0.28287918+0.j, 0.+0.j, 0.+0.j, 0.+0.11717239j, 0.+0.j, 0.06764951+0.j, 0.+0.16332037j, 0.+0.j,
                                                                   0.+0.j, 0.-0.06764951j, 0.16332037+0.j, 0.+0.j, 0.+0.28287918j, 0.+0.j, 0.+0.j, -0.11717239+0.j,
                                                                   0.+0.j, -0.11717239+0.j, 0.-0.28287918j, 0.+0.j, 0.48996111+0.j, 0.+0.j, 0.+0.j, 0.+0.20294854j,
                                                                   0.+0.48996111j, 0.+0.j, 0.+0.j, -0.20294854+0.j, 0.+0.j, 0.+0.11717239j, -0.28287918+0.j, 0.+0.j], 3).tolist()


def test_rzz_gate(circdef):
    circdef.rzz_gate(np.pi/6, 0, 1)
    circdef.rzz_gate(np.pi/3, 1, 2)
    circdef.rzz_gate(np.pi/2, 2, 3)
    circdef.rzz_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector(circdef), 3).tolist() == [-0.866-0.5j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                          0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                          0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                          0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_rzx_gate(circdef):
    circdef.rzx_gate(np.pi/4, 0, 1)
    circdef.rzx_gate(np.pi/3, 1, 2)
    circdef.rzx_gate(np.pi/2, 2, 3)
    circdef.rzx_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector(circdef), 3).tolist() == np.round([0.28287918+0.j, 0.+0.j, 0.-0.11717239j, 0.+0.j, 0.-0.16332037j, 0.+0.j, 0.06764951+0.j, 0.+0.j,
                                                                   0.-0.28287918j, 0.+0.j, -0.11717239+0.j, 0.+0.j, 0.16332037+0.j, 0.+0.j, 0.+0.06764951j, 0.+0.j,
                                                                   0.-0.48996111j, 0.+0.j, -0.20294854+0.j, 0.+0.j, -0.28287918+0.j, 0.+0.j, 0.-0.11717239j, 0.+0.j,
                                                                   0.48996111+0.j, 0.+0.j, 0.-0.20294854j, 0.+0.j, 0.+0.28287918j, 0.+0.j, -0.11717239+0.j, 0.+0.j], 3).tolist()


def test_rz_gate(circdef):
    circdef.rz_gate(np.pi/6, 0)
    circdef.rz_gate(np.pi/4, 1)
    circdef.rz_gate(np.pi/3, 2)
    circdef.rz_gate(np.pi/2, 3)
    circdef.rz_gate(2*np.pi/3, 4)
    assert np.round(statevector(circdef), 3).tolist() == [-0.991-0.131j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                          0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                          0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                          0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_s_gate(circdef):
    circdef.s_gate(0)
    circdef.s_gate(1)
    circdef.s_gate(2)
    circdef.s_gate(3)
    circdef.s_gate(4)
    assert statevector(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_sdg_gate(circdef):
    circdef.sdg_gate(0)
    circdef.sdg_gate(1)
    circdef.sdg_gate(2)
    circdef.sdg_gate(3)
    circdef.sdg_gate(4)
    assert statevector(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_swap_gate(circdef):
    circdef.swap_gate(0, 1)
    circdef.swap_gate(1, 2)
    circdef.swap_gate(2, 3)
    circdef.swap_gate(3, 4)
    assert statevector(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_iswap_gate(circdef):
    circdef.iswap_gate(0, 1)
    circdef.measure(0)
    circdef.measure(1)
    assert True


def test_sx_gate(circdef):
    circdef.sx_gate(0)
    circdef.sx_gate(1)
    circdef.sx_gate(2)
    circdef.sx_gate(3)
    circdef.sx_gate(4)
    assert statevector(circdef).tolist() == [-0.125-0.125j, -0.125+0.125j, -0.125+0.125j, 0.125+0.125j, -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j,
                                             -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j,
                                             -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j,
                                             0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j, 0.125-0.125j, -0.125-0.125j, -0.125-0.125j, -0.125+0.125j]


def test_sxd_gate(circdef):
    circdef.sxd_gate(0)
    circdef.sxd_gate(1)
    circdef.sxd_gate(2)
    circdef.sxd_gate(3)
    circdef.sxd_gate(4)
    assert np.round(statevector(circdef), 3).tolist() == [-0.125+0.125j, -0.125-0.125j, -0.125-0.125j, 0.125-0.125j, -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j,
                                                          -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j,
                                                          -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j,
                                                          0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j, 0.125+0.125j, -0.125+0.125j, -0.125+0.125j, -0.125-0.125j]


def test_t_gate(circdef):
    circdef.t_gate(0)
    circdef.t_gate(1)
    circdef.t_gate(2)
    circdef.t_gate(3)
    circdef.t_gate(4)
    assert statevector(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_td_gate(circdef):
    circdef.td_gate(0)
    circdef.td_gate(1)
    circdef.td_gate(2)
    circdef.td_gate(3)
    circdef.td_gate(4)
    assert statevector(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                             0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_u_gate(circdef):
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 0)
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 1)
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 2)
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 3)
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 4)
    assert np.round(statevector(circdef), 3).tolist() == [0.841+0j, 0.159+0.159j, 0.159+0.159j, 0+0.06j, 0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j,
                                                          0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j, 0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j,
                                                          0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j, 0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j,
                                                          0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j, -0.011+0.011j, -0.004+0j, -0.004+0j, -0.001-0.001j]


def test_u1_gate(circdef):
    circdef.u1_gate(np.pi/4, 0)
    circdef.u1_gate(np.pi/3, 1)
    circdef.u1_gate(np.pi/2, 2)
    circdef.u1_gate(2*np.pi/3, 3)
    circdef.u1_gate(np.pi/5, 4)
    assert statevector(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                             -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j,
                                             -0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                             0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]


def test_u2_gate(circdef):
    circdef.u2_gate(np.pi/4, np.pi/3, 0)
    circdef.u2_gate(np.pi/3, np.pi/2, 1)
    circdef.u2_gate(np.pi/2, 2*np.pi/3, 2)
    circdef.u2_gate(2*np.pi/3, np.pi/5, 3)
    circdef.u2_gate(np.pi/5, np.pi/2, 4)
    assert np.round(statevector(circdef), 3).tolist() == np.round([1.76776695e-01+0.00000000e+00j, 1.25000000e-01+1.25000000e-01j, 8.83883476e-02+1.53093109e-01j,
                                                                   -4.57531755e-02+1.70753175e-01j,  1.08244507e-17+1.76776695e-01j, -1.25000000e-01+1.25000000e-01j,
                                                                   -1.53093109e-01+8.83883476e-02j, -1.70753175e-01-4.57531755e-02j, -8.83883476e-02+1.53093109e-01j,
                                                                   -1.70753175e-01+4.57531755e-02j, -1.76776695e-01+3.48486364e-17j, -1.25000000e-01-1.25000000e-01j,
                                                                   -1.53093109e-01-8.83883476e-02j, -4.57531755e-02-1.70753175e-01j, -5.06184712e-17-1.76776695e-01j,
                                                                   1.25000000e-01-1.25000000e-01j, 1.43015351e-01+1.03906734e-01j, 2.76539678e-02+1.74600281e-01j,
                                                                   -1.84781963e-02+1.75808294e-01j, -1.37381295e-01+1.11249179e-01j, -1.03906734e-01+1.43015351e-01j,
                                                                   -1.74600281e-01+2.76539678e-02j, -1.75808294e-01-1.84781963e-02j, -1.11249179e-01-1.37381295e-01j,
                                                                   -1.61493547e-01+7.19015596e-02j, -1.65035263e-01-6.33511018e-02j, -1.43015351e-01-1.03906734e-01j,
                                                                   -2.76539678e-02-1.74600281e-01j, -7.19015596e-02-1.61493547e-01j, 6.33511018e-02-1.65035263e-01j,
                                                                   1.03906734e-01-1.43015351e-01j, 1.74600281e-01-2.76539678e-02j], 3).tolist()


def test_u3_gate(circdef):
    circdef.u3_gate(np.pi/4, np.pi/3, 2*np.pi/3, 0)
    circdef.u3_gate(np.pi/3, np.pi/2, 2*np.pi/3, 1)
    circdef.u3_gate(np.pi/2, 2*np.pi/3, np.pi/2, 2)
    circdef.u3_gate(2*np.pi/3, np.pi/5, 2*np.pi/3, 3)
    circdef.u3_gate(np.pi/5, np.pi/2, np.pi/2, 4)
    assert np.round(statevector(circdef), 3).tolist() == np.round([2.69034087e-01+0.00000000e+00j, 5.57187838e-02+9.65077646e-02j, 9.51102971e-18+1.55326903e-01j,
                                                                   -5.57187838e-02+3.21692549e-02j, -1.34517044e-01+2.32990354e-01j, -1.11437568e-01+3.01417021e-17j,
                                                                   -1.34517044e-01-7.76634514e-02j, -2.55234704e-17-6.43385097e-02j,  3.76986312e-01+2.73896588e-01j,
                                                                   -2.01756166e-02+1.91958170e-01j, -1.58134269e-01+2.17653149e-01j, -1.10827101e-01-1.16483977e-02j,
                                                                   -4.25694559e-01+1.89531429e-01j, -1.56152843e-01-1.13451681e-01j, -1.09426022e-01-2.45774868e-01j,
                                                                   6.55013588e-02-9.01548861e-02j, 5.35259278e-18+8.74144739e-02j, -3.13572735e-02+1.81041303e-02j,
                                                                   -5.04687700e-02+6.18064177e-18j, -1.04524245e-02-1.81041303e-02j, -7.57031551e-02-4.37072370e-02j,
                                                                   -1.20107492e-17-3.62082606e-02j,  2.52343850e-02-4.37072370e-02j, 2.09048490e-02-9.57313107e-18j,
                                                                   -8.89943962e-02+1.22490278e-01j, -6.23709902e-02-6.55545523e-03j, -7.07197950e-02-5.13809386e-02j,
                                                                   3.78479384e-03-3.60099080e-02j, -6.15824943e-02-1.38316547e-01j, 3.68626859e-02-5.07371344e-02j,
                                                                   7.98570956e-02-3.55546697e-02j, 2.92930982e-02+2.12826816e-02j], 3).tolist()


def test_cy_gate(circdef):
    circdef.cy_gate(0, 1)
    circdef.cy_gate(1, 2)
    circdef.cy_gate(2, 3)
    circdef.cy_gate(3, 4)
    assert statevector(circdef).tolist() == [1.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j, -0.+0.j, 0.-0.j, 0.-0.j,
                                             0.-0.j, -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j,
                                             0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j, -0.+0.j, 0.-0.j, 0.-0.j,
                                             0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_i_gate(circdef):
    circdef.i_gate(0)
    circdef.i_gate(1)
    circdef.i_gate(2)
    circdef.i_gate(3)
    circdef.i_gate(4)
    assert statevector(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                             0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                             0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                             0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_rccx_gate(circdef):
    circdef.rccx_gate(0, 1, 2)
    circdef.rccx_gate(1, 2, 3)
    circdef.rccx_gate(2, 3, 4)
    assert True
    
    
def test_rc3x_gate(circdef):
    circdef.rc3x_gate(0, 1, 2, 3)
    circdef.measure(0)
    circdef.measure(1)
    circdef.measure(2)
    circdef.measure(3)
    assert True


def test_rxx_gate(circdef):
    circdef.rxx_gate(np.pi/4, 0, 1)
    circdef.rxx_gate(np.pi/3, 1, 2)
    circdef.rxx_gate(np.pi/2, 2, 3)
    circdef.rxx_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector(circdef), 3).tolist() == np.round([0.28287918+0.j, 0.+0.j, 0.+0.j, 0.-0.11717239j, 0.+0.j, -0.06764951+0.j, 0.-0.16332037j, 0.+0.j,
                                                                   0.+0.j, 0.+0.06764951j, -0.16332037+0.j, 0.+0.j, 0.-0.28287918j, 0.+0.j, 0.+0.j, -0.11717239+0.j,
                                                                   0.+0.j, 0.11717239+0.j, 0.+0.28287918j, 0.+0.j, -0.48996111+0.j, 0.+0.j, 0.+0.j, 0.+0.20294854j,
                                                                   0.-0.48996111j, 0.+0.j, 0.+0.j, -0.20294854+0.j, 0.+0.j, 0.+0.11717239j, -0.28287918+0.j, 0.+0.j], 3).tolist()


def test_rx_gate(circdef):
    circdef.rx_gate(np.pi/4, 0)
    circdef.rx_gate(np.pi/3, 1)
    circdef.rx_gate(np.pi/2, 2)
    circdef.rx_gate(2*np.pi/3, 3)
    circdef.rx_gate(np.pi/5, 4)
    assert np.round(statevector(circdef), 3).tolist() == np.round([0.26903409+0.j, 0.-0.11143757j, 0.-0.1553269j, -0.06433851+0.j, 0.-0.26903409j, -0.11143757+0.j,
                                                                   -0.1553269+0.j, 0.+0.06433851j, 0.-0.46598071j, -0.19301553+0.j, -0.26903409+0.j, 0.+0.11143757j,
                                                                   -0.46598071+0.j, 0.+0.19301553j, 0.+0.26903409j, 0.11143757+0.j, 0.-0.08741447j, -0.03620826+0.j,
                                                                   -0.05046877+0.j, 0.+0.02090485j, -0.08741447+0.j, 0.+0.03620826j, 0.+0.05046877j, 0.02090485+0.j,
                                                                   -0.15140631+0.j, 0.+0.06271455j, 0.+0.08741447j, 0.03620826+0.j, 0.+0.15140631j, 0.06271455+0.j,
                                                                   0.08741447+0.j, 0.-0.03620826j], 3).tolist()


def test_r_gate(circdef):
    circdef.r_gate(np.pi/4, np.pi/3, 0)
    circdef.r_gate(np.pi/3, np.pi/2, 1)
    circdef.r_gate(np.pi/2, 2*np.pi/3, 2)
    circdef.r_gate(2*np.pi/3, np.pi/5, 3)
    circdef.r_gate(np.pi/5, np.pi/2, 4)
    assert np.round(statevector(circdef), 3).tolist() == np.round([0.26903409+0.00000000e+00j, 0.09650776-5.57187838e-02j, 0.1553269-9.51102971e-18j, 0.05571878-3.21692549e-02j,
                                                                   0.23299035+1.34517044e-01j, 0.11143757-3.60170741e-17j, 0.13451704+7.76634514e-02j, 0.06433851-2.55234704e-17j,
                                                                   0.27389659-3.76986312e-01j, 0.02017562-1.91958170e-01j, 0.15813427-2.17653149e-01j, 0.0116484-1.10827101e-01j,
                                                                   0.42569456-1.89531429e-01j, 0.11345168-1.56152843e-01j, 0.24577487-1.09426022e-01j, 0.06550136-9.01548861e-02j,
                                                                   0.08741447-5.35259278e-18j, 0.03135727-1.81041303e-02j, 0.05046877-6.18064177e-18j, 0.01810413-1.04524245e-02j,
                                                                   0.07570316+4.37072370e-02j, 0.03620826-1.39197733e-17j, 0.04370724+2.52343850e-02j, 0.02090485-9.57313107e-18j,
                                                                   0.0889944-1.22490278e-01j, 0.00655546-6.23709902e-02j, 0.05138094-7.07197950e-02j, 0.00378479-3.60099080e-02j,
                                                                   0.13831655-6.15824943e-02j, 0.03686269-5.07371344e-02j, 0.0798571-3.55546697e-02j, 0.02128268-2.92930982e-02j], 3).tolist()


def test_p_gate(circdef):
    circdef.p_gate(np.pi/4, 0)
    circdef.p_gate(np.pi/3, 1)
    circdef.p_gate(np.pi/2, 2)
    circdef.p_gate(2*np.pi/3, 3)
    circdef.p_gate(np.pi/5, 4)
    assert statevector(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                             -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j,
                                             0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
                                             -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]


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
