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


def statevector_qiskit(circ):
    return circ.execute(provider=providers.IBM_PROVIDER, repetitions=10, simulator_name=constants.STATEVECTOR_SIMULATOR)


def statevector_cirq(circ):
    return circ.execute(provider=providers.GOOGLE_PROVIDER, repetitions=10, simulator_name=constants.STATEVECTOR_SIMULATOR)


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
    assert statevector_qiskit(circdef).tolist() == [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j]

    assert statevector_cirq(circdef).tolist() == [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 1+0j]


def test_y_gate(circdef):
    circdef.y_gate(0)
    circdef.y_gate(1)
    circdef.y_gate(2)
    circdef.y_gate(3)
    circdef.y_gate(4)
    assert statevector_qiskit(circdef).tolist() == [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+1j]

    assert statevector_cirq(circdef).tolist() == [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+1j]


def test_z_gate(circdef):
    circdef.z_gate(0)
    circdef.z_gate(1)
    circdef.z_gate(2)
    circdef.z_gate(3)
    circdef.z_gate(4)
    assert statevector_qiskit(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert statevector_cirq(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_h_gate(circdef):
    circdef.h_gate(0)
    circdef.h_gate(1)
    circdef.h_gate(2)
    circdef.h_gate(3)
    circdef.h_gate(4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == [0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                                 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                                 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                                 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j]

    assert np.round(statevector_cirq(circdef).astype(np.float64), 3).tolist() == [0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                                                  0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                                                  0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j,
                                                                                  0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j, 0.177+0j]


def test_cx_gate(circdef):
    circdef.cx_gate(0, 1)
    circdef.cx_gate(1, 2)
    circdef.cx_gate(2, 3)
    circdef.cx_gate(3, 4)
    assert statevector_qiskit(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert statevector_cirq(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_cz_gate(circdef):
    circdef.cz_gate(0, 1)
    circdef.cz_gate(1, 2)
    circdef.cz_gate(2, 3)
    circdef.cz_gate(3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.-0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.-0.j,
                                                    -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.+0.j, -0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.-0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.+0.j, 0.+0.j, -0.+0.j, 0.-0.j,
                                                  -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.+0.j, -0.+0.j]


def test_ccx_gate(circdef):
    circdef.ccx_gate(0, 1, 2)
    circdef.ccx_gate(1, 2, 3)
    circdef.ccx_gate(2, 3, 4)
    assert statevector_qiskit(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert statevector_cirq(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_ry_gate(circdef):
    circdef.ry_gate(np.pi/6, 0)
    circdef.ry_gate(np.pi/4, 1)
    circdef.ry_gate(np.pi/3, 2)
    circdef.ry_gate(np.pi/2, 3)
    circdef.ry_gate(2*np.pi/3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == [0.273+0j, 0.073+0j, 0.113+0j, 0.03+0j, 0.158+0j, 0.042+0j, 0.065+0j, 0.018+0j,
                                                                 0.273+0j, 0.073+0j, 0.113+0j, 0.03+0j, 0.158+0j, 0.042+0j, 0.065+0j, 0.018+0j,
                                                                 0.473+0j, 0.127+0j, 0.196+0j, 0.053+0j, 0.273+0j, 0.073+0j, 0.113+0j, 0.03+0j,
                                                                 0.473+0j, 0.127+0j, 0.196+0j, 0.053+0j, 0.273+0j, 0.073+0j, 0.113+0j, 0.03+0j]

    assert np.around(statevector_cirq(circdef).astype(np.float64), 3).tolist() == np.round([0.2732403+0.j, 0.47326607+0.j, 0.2732403+0.j, 0.47326607+0.j,
                                                                                            0.15775536+0.j, 0.2732403+0.j, 0.15775536+0.j, 0.2732403+0.j,
                                                                                            0.11317984+0.j, 0.19603322+0.j, 0.11317984+0.j, 0.19603322+0.j,
                                                                                            0.06534441+0.j, 0.11317983+0.j, 0.06534441+0.j, 0.11317983+0.j,
                                                                                            0.07321451+0.j, 0.12681125+0.j, 0.07321451+0.j, 0.12681125+0.j,
                                                                                            0.04227042+0.j, 0.07321451+0.j, 0.04227042+0.j, 0.07321451+0.j,
                                                                                            0.03032645+0.j, 0.05252694+0.j, 0.03032645+0.j, 0.05252694+0.j,
                                                                                            0.01750898+0.j, 0.03032644+0.j, 0.01750898+0.j, 0.03032644+0.j], 3).tolist()


def test_ryy_gate(circdef):
    circdef.ryy_gate(np.pi/4, 0, 1)
    circdef.ryy_gate(np.pi/3, 1, 2)
    circdef.ryy_gate(np.pi/2, 2, 3)
    circdef.ryy_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([0.28287918+0.j, 0.+0.j, 0.+0.j, 0.+0.11717239j, 0.+0.j, 0.06764951+0.j, 0.+0.16332037j, 0.+0.j,
                                                                          0.+0.j, 0.-0.06764951j, 0.16332037+0.j, 0.+0.j, 0.+0.28287918j, 0.+0.j, 0.+0.j, -0.11717239+0.j,
                                                                          0.+0.j, -0.11717239+0.j, 0.-0.28287918j, 0.+0.j, 0.48996111+0.j, 0.+0.j, 0.+0.j, 0.+0.20294854j,
                                                                          0.+0.48996111j, 0.+0.j, 0.+0.j, -0.20294854+0.j, 0.+0.j, 0.+0.11717239j, -0.28287918+0.j, 0.+0.j], 3).tolist()

    assert np.around(statevector_cirq(circdef).astype(np.complex), 3).tolist() == np.round([0.28287917+0.j, 0.+0.j, 0.+0.j, 0.+0.4899611j, 0.+0.j, 0.4899611+0.j, 0.+0.28287917j,
                                                                                            0.+0.j, 0.+0.j, 0.-0.28287917j, 0.16332036+0.j, 0.+0.j, 0.+0.16332036j, 0.+0.j, 0.+0.j,
                                                                                            -0.28287917+0.j, 0.+0.j, -0.11717239+0.j, 0.-0.06764951j, 0.+0.j, 0.06764951+0.j, 0.+0.j,
                                                                                            0.+0.j, 0.+0.11717239j, 0.+0.11717239j, 0.+0.j, 0.+0.j, -0.20294853+0.j, 0.+0.j, 0.+0.20294853j,
                                                                                            -0.11717239+0.j, 0.+0.j], 3).tolist()


def test_rzz_gate(circdef):
    circdef.rzz_gate(np.pi/6, 0, 1)
    circdef.rzz_gate(np.pi/3, 1, 2)
    circdef.rzz_gate(np.pi/2, 2, 3)
    circdef.rzz_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == [-0.866-0.5j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                                 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                                 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                                 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert np.around(statevector_cirq(circdef).astype(np.complex), 3).tolist() == np.round([-0.86602527-0.4999999j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                                                            0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                                                            0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                                                            0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j], 3).tolist()


def test_rzx_gate(circdef):
    circdef.rzx_gate(np.pi/4, 0, 1)
    circdef.rzx_gate(np.pi/3, 1, 2)
    circdef.rzx_gate(np.pi/2, 2, 3)
    circdef.rzx_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([0.28287918+0.j, 0.+0.j, 0.-0.11717239j, 0.+0.j, 0.-0.16332037j, 0.+0.j, 0.06764951+0.j, 0.+0.j,
                                                                          0.-0.28287918j, 0.+0.j, -0.11717239+0.j, 0.+0.j, 0.16332037+0.j, 0.+0.j, 0.+0.06764951j, 0.+0.j,
                                                                          0.-0.48996111j, 0.+0.j, -0.20294854+0.j, 0.+0.j, -0.28287918+0.j, 0.+0.j, 0.-0.11717239j, 0.+0.j,
                                                                          0.48996111+0.j, 0.+0.j, 0.-0.20294854j, 0.+0.j, 0.+0.28287918j, 0.+0.j, -0.11717239+0.j, 0.+0.j], 3).tolist()

    assert np.around(statevector_cirq(circdef).astype(np.complex), 3).tolist() == np.round([0.28287917+0.j, 0.+0.j, 0.-0.4899611j, 0.+0.j, 0.-0.28287917j, 0.+0.j,
                                                                                            -0.4899611+0.j, 0.+0.j, 0.-0.16332036j, 0.+0.j, -0.28287917+0.j, 0.+0.j,
                                                                                            -0.16332036+0.j, 0.+0.j, 0.+0.28287917j, 0.+0.j, 0.-0.11717239j, 0.+0.j,
                                                                                            -0.20294853+0.j, 0.+0.j, -0.11717239+0.j, 0.+0.j, 0.+0.20294853j, 0.+0.j,
                                                                                            -0.06764951+0.j, 0.+0.j, 0.+0.11717239j, 0.+0.j, 0.+0.06764951j, 0.+0.j,
                                                                                            0.11717239+0.j, 0.+0.j], 3).tolist()


def test_rz_gate(circdef):
    circdef.rz_gate(np.pi/6, 0)
    circdef.rz_gate(np.pi/4, 1)
    circdef.rz_gate(np.pi/3, 2)
    circdef.rz_gate(np.pi/2, 3)
    circdef.rz_gate(2*np.pi/3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == [-0.991-0.131j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                                 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                                 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                                 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert np.round(statevector_cirq(circdef).astype(np.complex), 3).tolist() == np.round([-0.9914448-0.13052619j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                                                           0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                                                           0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                                                           0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j], 3).tolist()


def test_s_gate(circdef):
    circdef.s_gate(0)
    circdef.s_gate(1)
    circdef.s_gate(2)
    circdef.s_gate(3)
    circdef.s_gate(4)
    assert statevector_qiskit(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert statevector_cirq(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_sdg_gate(circdef):
    circdef.sdg_gate(0)
    circdef.sdg_gate(1)
    circdef.sdg_gate(2)
    circdef.sdg_gate(3)
    circdef.sdg_gate(4)
    assert statevector_qiskit(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert statevector_cirq(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_swap_gate(circdef):
    circdef.swap_gate(0, 1)
    circdef.swap_gate(1, 2)
    circdef.swap_gate(2, 3)
    circdef.swap_gate(3, 4)
    assert statevector_qiskit(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert statevector_cirq(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_iswap_gate(circdef):
    circdef.iswap_gate(0, 1)
    circdef.iswap_gate(1, 2)
    circdef.iswap_gate(2, 3)
    circdef.iswap_gate(3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([1.00000000e+00-2.10292737e-17j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 1.01465364e-17-8.80915192e-17j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j], 3).tolist()

    assert np.round(statevector_cirq(circdef).astype(np.float64), 3).tolist() == np.round([1.00000000e+00-2.10292737e-17j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 1.01465364e-17-8.80915192e-17j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j], 3).tolist()


def test_sx_gate(circdef):
    circdef.sx_gate(0)
    circdef.sx_gate(1)
    circdef.sx_gate(2)
    circdef.sx_gate(3)
    circdef.sx_gate(4)
    assert statevector_qiskit(circdef).tolist() == [-0.125-0.125j, -0.125+0.125j, -0.125+0.125j, 0.125+0.125j, -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j,
                                                    -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j,
                                                    -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j,
                                                    0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j, 0.125-0.125j, -0.125-0.125j, -0.125-0.125j, -0.125+0.125j]

    assert statevector_cirq(circdef).tolist() == [-0.125-0.125j, -0.125+0.125j, -0.125+0.125j, 0.125+0.125j, -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j,
                                                  -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j,
                                                  -0.125+0.125j, 0.125+0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j,
                                                  0.125+0.125j, 0.125-0.125j, 0.125-0.125j, -0.125-0.125j, 0.125-0.125j, -0.125-0.125j, -0.125-0.125j, -0.125+0.125j]


def test_sxd_gate(circdef):
    circdef.sxd_gate(0)
    circdef.sxd_gate(1)
    circdef.sxd_gate(2)
    circdef.sxd_gate(3)
    circdef.sxd_gate(4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == [-0.125+0.125j, -0.125-0.125j, -0.125-0.125j, 0.125-0.125j, -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j,
                                                                 -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j,
                                                                 -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j,
                                                                 0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j, 0.125+0.125j, -0.125+0.125j, -0.125+0.125j, -0.125-0.125j]

    assert statevector_cirq(circdef).tolist() == [-0.125+0.125j, -0.125-0.125j, -0.125-0.125j, 0.125-0.125j, -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j,
                                                  -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j,
                                                  -0.125-0.125j, 0.125-0.125j, 0.125-0.125j, 0.125+0.125j, 0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j,
                                                  0.125-0.125j, 0.125+0.125j, 0.125+0.125j, -0.125+0.125j, 0.125+0.125j, -0.125+0.125j, -0.125+0.125j, -0.125-0.125j]


def test_t_gate(circdef):
    circdef.t_gate(0)
    circdef.t_gate(1)
    circdef.t_gate(2)
    circdef.t_gate(3)
    circdef.t_gate(4)
    assert statevector_qiskit(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert statevector_cirq(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_td_gate(circdef):
    circdef.td_gate(0)
    circdef.td_gate(1)
    circdef.td_gate(2)
    circdef.td_gate(3)
    circdef.td_gate(4)
    assert statevector_qiskit(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                    0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]

    assert statevector_cirq(circdef).tolist() == [1+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j,
                                                  0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j]


def test_u_gate(circdef):
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 0)
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 1)
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 2)
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 3)
    circdef.u_gate(np.pi/6, np.pi/4, np.pi/3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == [0.841+0j, 0.159+0.159j, 0.159+0.159j, 0+0.06j, 0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j,
                                                                 0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j, 0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j,
                                                                 0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j, 0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j,
                                                                 0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j, -0.011+0.011j, -0.004+0j, -0.004+0j, -0.001-0.001j]

    assert statevector_cirq(circdef).astype(np.complex).round(3).tolist() == [0.841+0j, 0.159+0.159j, 0.159+0.159j, 0+0.06j, 0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j,
                                                                              0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j, 0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j,
                                                                              0.159+0.159j, 0+0.06j, 0+0.06j, -0.011+0.011j, 0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j,
                                                                              0+0.06j, -0.011+0.011j, -0.011+0.011j, -0.004+0j, -0.011+0.011j, -0.004+0j, -0.004+0j, -0.001-0.001j]


def test_u1_gate(circdef):
    circdef.u1_gate(np.pi/4, 0)
    circdef.u1_gate(np.pi/3, 1)
    circdef.u1_gate(np.pi/2, 2)
    circdef.u1_gate(2*np.pi/3, 3)
    circdef.u1_gate(np.pi/5, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j,
                                                    -0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j,
                                                  -0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]


def test_u2_gate(circdef):
    circdef.u2_gate(np.pi/4, np.pi/3, 0)
    circdef.u2_gate(np.pi/3, np.pi/2, 1)
    circdef.u2_gate(np.pi/2, 2*np.pi/3, 2)
    circdef.u2_gate(2*np.pi/3, np.pi/5, 3)
    circdef.u2_gate(np.pi/5, np.pi/2, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([1.76776695e-01+0.00000000e+00j, 1.25000000e-01+1.25000000e-01j, 8.83883476e-02+1.53093109e-01j,
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

    assert statevector_cirq(circdef).astype(np.complex).round(3).tolist() == np.round([1.76776677e-01+0.00000000e+00j, 1.43015340e-01+1.03906721e-01j, -8.83883387e-02+1.53093100e-01j,
                                                                                       -1.61493540e-01+7.19015598e-02j, 1.08244499e-17+1.76776677e-01j, -1.03906721e-01+1.43015340e-01j,
                                                                                       -1.53093100e-01-8.83883387e-02j, -7.19015598e-02-1.61493540e-01j, 8.83883387e-02+1.53093114e-01j,
                                                                                       -1.84782073e-02+1.75808296e-01j, -1.76776692e-01-1.05367119e-08j, -1.43015355e-01-1.03906743e-01j,
                                                                                       -1.53093114e-01+8.83883387e-02j, -1.75808296e-01-1.84782073e-02j, 1.05367119e-08-1.76776692e-01j,
                                                                                       1.03906743e-01-1.43015355e-01j, 1.24999985e-01+1.24999985e-01j, 2.76539698e-02+1.74600273e-01j,
                                                                                       -1.70753166e-01+4.57531735e-02j, -1.65035248e-01-6.33510947e-02j, -1.24999985e-01+1.24999985e-01j,
                                                                                       -1.74600273e-01+2.76539698e-02j, -4.57531735e-02-1.70753166e-01j, 6.33510947e-02-1.65035248e-01j,
                                                                                       -4.57531810e-02+1.70753166e-01j, -1.37381285e-01+1.11249164e-01j, -1.24999985e-01-1.24999993e-01j,
                                                                                       -2.76539624e-02-1.74600273e-01j, -1.70753166e-01-4.57531810e-02j, -1.11249164e-01-1.37381285e-01j,
                                                                                       1.24999993e-01-1.24999985e-01j, 1.74600273e-01-2.76539624e-02j], 3).tolist()


def test_u3_gate(circdef):
    circdef.u3_gate(np.pi/4, np.pi/3, 2*np.pi/3, 0)
    circdef.u3_gate(np.pi/3, np.pi/2, 2*np.pi/3, 1)
    circdef.u3_gate(np.pi/2, 2*np.pi/3, np.pi/2, 2)
    circdef.u3_gate(2*np.pi/3, np.pi/5, 2*np.pi/3, 3)
    circdef.u3_gate(np.pi/5, np.pi/2, np.pi/2, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([2.69034087e-01+0.00000000e+00j, 5.57187838e-02+9.65077646e-02j, 9.51102971e-18+1.55326903e-01j,
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

    assert statevector_cirq(circdef).astype(np.complex).round(3).tolist() == np.round([2.69034088e-01+0.0000000e+00j, 5.35259269e-18+8.7414473e-02j,
                                                                                       3.76986325e-01+2.7389660e-01j, -8.89943987e-02+1.2249028e-01j,
                                                                                       -1.34517044e-01+2.3299037e-01j, -7.57031590e-02-4.3707237e-02j,
                                                                                       -4.25694555e-01+1.8953146e-01j, -6.15825057e-02-1.3831654e-01j,
                                                                                       9.51102939e-18+1.5532690e-01j, -5.04687689e-02+6.1806414e-18j,
                                                                                       -1.58134267e-01+2.1765316e-01j, -7.07197934e-02-5.1380940e-02j,
                                                                                       -1.34517044e-01-7.7663451e-02j, 2.52343845e-02-4.3707237e-02j,
                                                                                       -1.09426022e-01-2.4577485e-01j, 7.98570886e-02-3.5554670e-02j,
                                                                                       5.57187833e-02+9.6507765e-02j, -3.13572735e-02+1.8104130e-02j,
                                                                                       -2.01756153e-02+1.9195817e-01j, -6.23709932e-02-6.5554548e-03j,
                                                                                       -1.11437574e-01+0.0000000e+00j, -2.21711660e-18-3.6208265e-02j,
                                                                                       -1.56152859e-01-1.1345168e-01j, 3.68626863e-02-5.0737143e-02j,
                                                                                       -5.57187833e-02+3.2169256e-02j, -1.04524251e-02-1.8104130e-02j,
                                                                                       -1.10827103e-01-1.1648393e-02j, 3.78479250e-03-3.6009908e-02j,
                                                                                       -1.77148085e-09-6.4338513e-02j, 2.09048502e-02-5.7558902e-10j,
                                                                                       6.55013621e-02-9.0154894e-02j, 2.92930994e-02+2.1282682e-02j], 3).tolist()


def test_cy_gate(circdef):
    circdef.cy_gate(0, 1)
    circdef.cy_gate(1, 2)
    circdef.cy_gate(2, 3)
    circdef.cy_gate(3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j, -0.+0.j, 0.-0.j, 0.-0.j,
                                                    0.-0.j, -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j,
                                                    0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j, -0.+0.j, 0.-0.j, 0.-0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j, -0.+0.j, 0.-0.j, 0.-0.j,
                                                  0.-0.j, -0.+0.j, -0.+0.j, -0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j,
                                                  0.+0.j, 0.-0.j, 0.-0.j, 0.-0.j, 0.-0.j, -0.+0.j, 0.-0.j, 0.-0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_i_gate(circdef):
    circdef.i_gate(0)
    circdef.i_gate(1)
    circdef.i_gate(2)
    circdef.i_gate(3)
    circdef.i_gate(4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_rccx_gate(circdef):
    circdef.rccx_gate(0, 1, 2)
    circdef.rccx_gate(1, 2, 3)
    circdef.rccx_gate(2, 3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([1.00000000e+00-6.10622664e-16j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          -5.47382213e-48-3.76325271e-48j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, -6.16297582e-33-3.69778549e-32j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          -9.24446373e-32+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 1.23259516e-32-8.01186857e-32j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j], 3).tolist()

    assert np.round(statevector_cirq(circdef).astype(np.float64), 3).tolist() == np.round([1.00000000e+00-6.10622664e-16j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           5.47382213e-48-3.76325271e-48j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, -6.16297582e-33-3.69778549e-32j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -9.24446373e-32+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 1.23259516e-32-8.01186857e-32j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j], 3).tolist()


def test_rc3x_gate(circdef):
    circdef.rc3x_gate(0, 1, 2, 3)
    circdef.rc3x_gate(1, 2, 3, 4)
    circdef.rc3x_gate(2, 3, 4, 1)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([1.00000000e+00-6.10622664e-16j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          -5.47382213e-48-3.76325271e-48j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, -6.16297582e-33-3.69778549e-32j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          -9.24446373e-32+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 1.23259516e-32-8.01186857e-32j, 0.00000000e+00+0.00000000e+00j,
                                                                          0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j], 3).tolist()

    assert np.round(statevector_cirq(circdef).astype(np.float64), 3).tolist() == np.round([1.00000000e+00-6.10622664e-16j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -5.47382213e-48-3.76325271e-48j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 5.55111512e-17+2.77555756e-16j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, -6.16297582e-33-3.69778549e-32j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                          -9.24446373e-32+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 1.23259516e-32-8.01186857e-32j, 0.00000000e+00+0.00000000e+00j,
                                                                                           0.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j], 3).tolist()


def test_rxx_gate(circdef):
    circdef.rxx_gate(np.pi/4, 0, 1)
    circdef.rxx_gate(np.pi/3, 1, 2)
    circdef.rxx_gate(np.pi/2, 2, 3)
    circdef.rxx_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([0.28287918+0.j, 0.+0.j, 0.+0.j, 0.-0.11717239j, 0.+0.j, -0.06764951+0.j, 0.-0.16332037j, 0.+0.j,
                                                                          0.+0.j, 0.+0.06764951j, -0.16332037+0.j, 0.+0.j, 0.-0.28287918j, 0.+0.j, 0.+0.j, -0.11717239+0.j,
                                                                          0.+0.j, 0.11717239+0.j, 0.+0.28287918j, 0.+0.j, -0.48996111+0.j, 0.+0.j, 0.+0.j, 0.+0.20294854j,
                                                                          0.-0.48996111j, 0.+0.j, 0.+0.j, -0.20294854+0.j, 0.+0.j, 0.+0.11717239j, -0.28287918+0.j, 0.+0.j], 3).tolist()

    assert statevector_cirq(circdef).astype(np.complex).round(3).tolist() == np.round([0.28287917+0.j, 0.+0.j, 0.+0.j, 0.-0.4899611j, 0.+0.j, -0.4899611+0.j, 0.-0.28287917j, 0.+0.j,
                                                                                       0.+0.j, 0.+0.28287917j, -0.16332036+0.j, 0.+0.j, 0.-0.16332036j, 0.+0.j, 0.+0.j, -0.28287917+0.j,
                                                                                       0.+0.j, 0.11717239+0.j, 0.+0.06764951j, 0.+0.j, -0.06764951+0.j, 0.+0.j, 0.+0.j, 0.+0.11717239j,
                                                                                       0.-0.11717239j, 0.+0.j, 0.+0.j, -0.20294853+0.j, 0.+0.j, 0.+0.20294853j, -0.11717239+0.j, 0.+0.j], 3).tolist()


def test_rx_gate(circdef):
    circdef.rx_gate(np.pi/4, 0)
    circdef.rx_gate(np.pi/3, 1)
    circdef.rx_gate(np.pi/2, 2)
    circdef.rx_gate(2*np.pi/3, 3)
    circdef.rx_gate(np.pi/5, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([0.26903409+0.j, 0.-0.11143757j, 0.-0.1553269j, -0.06433851+0.j, 0.-0.26903409j, -0.11143757+0.j,
                                                                          -0.1553269+0.j, 0.+0.06433851j, 0.-0.46598071j, -0.19301553+0.j, -0.26903409+0.j, 0.+0.11143757j,
                                                                          -0.46598071+0.j, 0.+0.19301553j, 0.+0.26903409j, 0.11143757+0.j, 0.-0.08741447j, -0.03620826+0.j,
                                                                          -0.05046877+0.j, 0.+0.02090485j, -0.08741447+0.j, 0.+0.03620826j, 0.+0.05046877j, 0.02090485+0.j,
                                                                          -0.15140631+0.j, 0.+0.06271455j, 0.+0.08741447j, 0.03620826+0.j, 0.+0.15140631j, 0.06271455+0.j,
                                                                          0.08741447+0.j, 0.-0.03620826j], 3).tolist()

    assert statevector_cirq(circdef).astype(np.complex).round(3).tolist() == np.round([0.2690341+0.j, 0.-0.08741447j, 0.-0.4659807j, -0.1514063+0.j,
                                                                                       0.-0.2690341j,  -0.08741447+0.j, -0.4659807+0.j, 0.+0.1514063j,
                                                                                       0.-0.1553269j, -0.05046877+0.j, -0.2690341+0.j, 0.+0.08741447j,
                                                                                       -0.1553269+0.j, 0.+0.05046877j,  0.+0.2690341j, 0.08741447+0.j,
                                                                                       0.-0.11143757j, -0.03620826+0.j, -0.19301552+0.j, 0.+0.06271455j,
                                                                                       -0.11143757+0.j, 0.+0.03620826j, 0.+0.19301552j,  0.06271455+0.j,
                                                                                       -0.06433851+0.j, 0.+0.02090485j,  0.+0.11143757j, 0.03620826+0.j,
                                                                                       0.+0.06433851j,  0.02090485+0.j, 0.11143757+0.j, 0.-0.03620826j], 3).tolist()


def test_r_gate(circdef):
    circdef.r_gate(np.pi/4, np.pi/3, 0)
    circdef.r_gate(np.pi/3, np.pi/2, 1)
    circdef.r_gate(np.pi/2, 2*np.pi/3, 2)
    circdef.r_gate(2*np.pi/3, np.pi/5, 3)
    circdef.r_gate(np.pi/5, np.pi/2, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([0.26903409+0.00000000e+00j, 0.09650776-5.57187838e-02j, 0.1553269-9.51102971e-18j, 0.05571878-3.21692549e-02j,
                                                                          0.23299035+1.34517044e-01j, 0.11143757-3.60170741e-17j, 0.13451704+7.76634514e-02j, 0.06433851-2.55234704e-17j,
                                                                          0.27389659-3.76986312e-01j, 0.02017562-1.91958170e-01j, 0.15813427-2.17653149e-01j, 0.0116484-1.10827101e-01j,
                                                                          0.42569456-1.89531429e-01j, 0.11345168-1.56152843e-01j, 0.24577487-1.09426022e-01j, 0.06550136-9.01548861e-02j,
                                                                          0.08741447-5.35259278e-18j, 0.03135727-1.81041303e-02j, 0.05046877-6.18064177e-18j, 0.01810413-1.04524245e-02j,
                                                                          0.07570316+4.37072370e-02j, 0.03620826-1.39197733e-17j, 0.04370724+2.52343850e-02j, 0.02090485-9.57313107e-18j,
                                                                          0.0889944-1.22490278e-01j, 0.00655546-6.23709902e-02j, 0.05138094-7.07197950e-02j, 0.00378479-3.60099080e-02j,
                                                                          0.13831655-6.15824943e-02j, 0.03686269-5.07371344e-02j, 0.0798571-3.55546697e-02j, 0.02128268-2.92930982e-02j], 3).tolist()

    assert statevector_cirq(circdef).astype(np.complex).round(3).tolist() == np.round([0.2690341+0.0000000e+00j, 0.08741447-5.3525927e-18j, 0.2738966-3.7698632e-01j, 0.0889944-1.2249028e-01j,
                                                                                       0.23299037+1.3451704e-01j, 0.07570316+4.3707237e-02j, 0.42569456-1.8953146e-01j, 0.13831654-6.1582506e-02j,
                                                                                       0.1553269-9.5110294e-18j, 0.05046877-6.1806414e-18j, 0.15813427-2.1765316e-01j, 0.05138094-7.0719793e-02j,
                                                                                       0.13451704+7.7663451e-02j, 0.04370724+2.5234384e-02j, 0.24577485-1.0942602e-01j, 0.07985709-3.5554670e-02j,
                                                                                       0.09650777-5.5718783e-02j, 0.03135727-1.8104130e-02j, 0.02017562-1.9195817e-01j, 0.00655545-6.2370993e-02j,
                                                                                       0.11143757+0.0000000e+00j, 0.03620826-2.2171166e-18j, 0.11345168-1.5615286e-01j, 0.03686269-5.0737143e-02j,
                                                                                       0.05571878-3.2169256e-02j, 0.01810413-1.0452425e-02j, 0.01164839-1.1082710e-01j, 0.00378479-3.6009908e-02j,
                                                                                       0.06433851-1.7714809e-09j, 0.02090485-5.7558902e-10j, 0.06550136-9.0154894e-02j, 0.02128268-2.9293099e-02j], 3).tolist()


def test_p_gate(circdef):
    circdef.p_gate(np.pi/4, 0)
    circdef.p_gate(np.pi/3, 1)
    circdef.p_gate(np.pi/2, 2)
    circdef.p_gate(2*np.pi/3, 3)
    circdef.p_gate(np.pi/5, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j,
                                                    0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
                                                    -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j,
                                                  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
                                                  -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]


def test_dcx_gate(circdef):
    circdef.dcx_gate(0, 1)
    circdef.dcx_gate(1, 2)
    circdef.dcx_gate(2, 3)
    circdef.dcx_gate(3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_ch_gate(circdef):
    circdef.ch_gate(0, 1)
    circdef.ch_gate(1, 2)
    circdef.ch_gate(2, 3)
    circdef.ch_gate(3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([1.00000000e+00+3.60822483e-16j, 0.00000000e+00+0.00000000e+00j, -3.92523115e-17-9.02546913e-34j,
                                                                          0.00000000e+00+0.00000000e+00j, -3.92523115e-17+2.17894100e-33j, 0.00000000e+00+0.00000000e+00j,
                                                                          -2.77555756e-17-6.16297582e-33j, 0.00000000e+00+0.00000000e+00j, -3.92523115e-17+3.92523115e-17j,
                                                                          0.00000000e+00+0.00000000e+00j, 4.27642354e-50-4.51273456e-34j, 0.00000000e+00+0.00000000e+00j,
                                                                          -2.77555756e-17-3.71968495e-33j, 0.00000000e+00+0.00000000e+00j, -1.96261557e-17-7.57154484e-33j,
                                                                          0.00000000e+00+0.00000000e+00j, -5.55111512e-17+2.46519033e-32j, 0.00000000e+00+0.00000000e+00j,
                                                                          3.08148791e-33-6.38197043e-34j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00-6.38197043e-34j,
                                                                          0.00000000e+00+0.00000000e+00j, 1.54074396e-33-1.54074396e-33j, 0.00000000e+00+0.00000000e+00j,
                                                                          -3.92523115e-17+3.92523115e-17j, 0.00000000e+00+0.00000000e+00j, 1.28292706e-49-4.51273456e-34j,
                                                                          0.00000000e+00+0.00000000e+00j, -2.77555756e-17-8.34191682e-33j, 0.00000000e+00+0.00000000e+00j,
                                                                          -1.96261557e-17-1.21937767e-32j, 0.00000000e+00+0.00000000e+00j], 3).tolist()

    assert np.round(statevector_cirq(circdef).astype(np.float64), 3).tolist() == np.round([1.00000000e+00+3.60822483e-16j, 0.00000000e+00+0.00000000e+00j, -3.92523115e-17-9.02546913e-34j,
                                                                                           0.00000000e+00+0.00000000e+00j, -3.92523115e-17+2.17894100e-33j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -2.77555756e-17-6.16297582e-33j, 0.00000000e+00+0.00000000e+00j, -3.92523115e-17+3.92523115e-17j,
                                                                                           0.00000000e+00+0.00000000e+00j, 4.27642354e-50-4.51273456e-34j, 0.00000000e+00+0.00000000e+00j,
                                                                                          -2.77555756e-17-3.71968495e-33j, 0.00000000e+00+0.00000000e+00j, -1.96261557e-17-7.57154484e-33j,
                                                                                          0.00000000e+00+0.00000000e+00j, -5.55111512e-17+2.46519033e-32j, 0.00000000e+00+0.00000000e+00j,
                                                                                           3.08148791e-33-6.38197043e-34j, 0.00000000e+00+0.00000000e+00j, 0.00000000e+00-6.38197043e-34j,
                                                                                           0.00000000e+00+0.00000000e+00j, 1.54074396e-33-1.54074396e-33j, 0.00000000e+00+0.00000000e+00j,
                                                                                          -3.92523115e-17+3.92523115e-17j, 0.00000000e+00+0.00000000e+00j, 1.28292706e-49-4.51273456e-34j,
                                                                                           0.00000000e+00+0.00000000e+00j, -2.77555756e-17-8.34191682e-33j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -1.96261557e-17-1.21937767e-32j, 0.00000000e+00+0.00000000e+00j], 3).tolist()


def test_csx_gate(circdef):
    circdef.csx_gate(0, 1)
    circdef.csx_gate(1, 2)
    circdef.csx_gate(2, 3)
    circdef.csx_gate(3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_cswap_gate(circdef):
    circdef.cswap_gate(0, 1, 2)
    circdef.cswap_gate(1, 2, 3)
    circdef.cswap_gate(2, 3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_cphase_gate(circdef):
    circdef.cphase_gate(np.pi/4, 0, 1)
    circdef.cphase_gate(np.pi/3, 1, 2)
    circdef.cphase_gate(np.pi/2, 2, 3)
    circdef.cphase_gate(2*np.pi/3, 3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]


def test_crx_gate(circdef):
    circdef.crx_gate(np.pi/4, 0, 1)
    circdef.crx_gate(np.pi/3, 1, 2)
    circdef.crx_gate(np.pi/2, 2, 3)
    circdef.crx_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([1.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, -1.21047942e-33-2.36309336e-19j,
                                                                          0.00000000e+00+0.00000000e+00j, 5.25430464e-34+8.66418136e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                          -9.64728823e-20+4.88268892e-34j, 0.00000000e+00+0.00000000e+00j, 2.12412088e-33-1.08174986e-17j,
                                                                          0.00000000e+00+0.00000000e+00j, -1.15237898e-37-4.49301625e-50j, 0.00000000e+00+0.00000000e+00j,
                                                                          4.33209068e-18+2.54881708e-36j, 0.00000000e+00+0.00000000e+00j, 2.41180816e-34+4.82364412e-20j,
                                                                          0.00000000e+00+0.00000000e+00j, -1.37800288e-34+7.43708407e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                          -6.49946566e-36-5.02782168e-51j, 0.00000000e+00+0.00000000e+00j, 9.02014647e-35+2.54844219e-50j,
                                                                          0.00000000e+00+0.00000000e+00j, 3.24970257e-50-1.54305530e-36j, 0.00000000e+00+0.00000000e+00j,
                                                                          -1.87364573e-17-4.82636241e-33j, 0.00000000e+00+0.00000000e+00j, -7.78335461e-50+1.99597894e-37j,
                                                                          0.00000000e+00+0.00000000e+00j, 4.63865491e-34-7.50340116e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                          8.35479669e-20-4.12621590e-34j, 0.00000000e+00+0.00000000e+00j], 3).tolist()

    assert np.round(statevector_cirq(circdef).astype(np.float64), 3).tolist() == np.round([1.00000000e+00+0.00000000e+00j, 0.00000000e+00+0.00000000e+00j, -1.21047942e-33-2.36309336e-19j,
                                                                                           0.00000000e+00+0.00000000e+00j, 5.25430464e-34+8.66418136e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -9.64728823e-20+4.88268892e-34j, 0.00000000e+00+0.00000000e+00j, 2.12412088e-33-1.08174986e-17j,
                                                                                           0.00000000e+00+0.00000000e+00j, -1.15237898e-37-4.49301625e-50j, 0.00000000e+00+0.00000000e+00j,
                                                                                           4.33209068e-18+2.54881708e-36j, 0.00000000e+00+0.00000000e+00j, 2.41180816e-34+4.82364412e-20j,
                                                                                           0.00000000e+00+0.00000000e+00j, -1.37800288e-34+7.43708407e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -6.49946566e-36-5.02782168e-51j, 0.00000000e+00+0.00000000e+00j, 9.02014647e-35+2.54844219e-50j,
                                                                                           0.00000000e+00+0.00000000e+00j, 3.24970257e-50-1.54305530e-36j, 0.00000000e+00+0.00000000e+00j,
                                                                                          -1.87364573e-17-4.82636241e-33j, 0.00000000e+00+0.00000000e+00j, -7.78335461e-50+1.99597894e-37j,
                                                                                           0.00000000e+00+0.00000000e+00j, 4.63865491e-34-7.50340116e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                                           8.35479669e-20-4.12621590e-34j, 0.00000000e+00+0.00000000e+00j], 3).tolist()


def test_cry_gate(circdef):
    circdef.cry_gate(np.pi/4, 0, 1)
    circdef.cry_gate(np.pi/3, 1, 2)
    circdef.cry_gate(np.pi/2, 2, 3)
    circdef.cry_gate(2*np.pi/3, 3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([1.00000000e+00+0.j, 0.00000000e+00+0.j, -2.36309336e-19+0.j, 0.00000000e+00+0.j,
                                                                          8.66418136e-18+0.j, 0.00000000e+00+0.j, -9.64728823e-20+0.j, 0.00000000e+00+0.j,
                                                                          -1.08174986e-17+0.j, 0.00000000e+00+0.j, 1.15237898e-37+0.j, 0.00000000e+00+0.j,
                                                                          4.33209068e-18+0.j, 0.00000000e+00+0.j, -4.82364412e-20+0.j, 0.00000000e+00+0.j,
                                                                          7.43708407e-18+0.j, 0.00000000e+00+0.j, 6.49946566e-36+0.j, 0.00000000e+00+0.j,
                                                                          1.30088099e-35+0.j, 0.00000000e+00+0.j, -1.54305530e-36+0.j, 0.00000000e+00+0.j,
                                                                          -1.87364573e-17+0.j, 0.00000000e+00+0.j, 1.99597894e-37+0.j, 0.00000000e+00+0.j,
                                                                          7.50340116e-18+0.j, 0.00000000e+00+0.j, -8.35479669e-20+0.j, 0.00000000e+00+0.j], 3).tolist()

    assert np.round(statevector_cirq(circdef).astype(np.float64), 3).tolist() == np.round([1.00000000e+00+0.j, 0.00000000e+00+0.j, -2.36309336e-19+0.j, 0.00000000e+00+0.j,
                                                                                           8.66418136e-18+0.j, 0.00000000e+00+0.j, -9.64728823e-20+0.j, 0.00000000e+00+0.j,
                                                                                           -1.08174986e-17+0.j, 0.00000000e+00+0.j, 1.15237898e-37+0.j, 0.00000000e+00+0.j,
                                                                                           4.33209068e-18+0.j, 0.00000000e+00+0.j, -4.82364412e-20+0.j, 0.00000000e+00+0.j,
                                                                                           7.43708407e-18+0.j, 0.00000000e+00+0.j, 6.49946566e-36+0.j, 0.00000000e+00+0.j,
                                                                                           1.30088099e-35+0.j, 0.00000000e+00+0.j, -1.54305530e-36+0.j, 0.00000000e+00+0.j,
                                                                                           -1.87364573e-17+0.j, 0.00000000e+00+0.j, 1.99597894e-37+0.j, 0.00000000e+00+0.j,
                                                                                           7.50340116e-18+0.j, 0.00000000e+00+0.j, -8.35479669e-20+0.j, 0.00000000e+00+0.j], 3).tolist()


def test_crz_gate(circdef):
    circdef.crz_gate(np.pi/4, 0, 1)
    circdef.crz_gate(np.pi/3, 1, 2)
    circdef.crz_gate(np.pi/2, 2, 3)
    circdef.crz_gate(2*np.pi/3, 3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_cu_gate(circdef):
    circdef.cu_gate(np.pi/4, np.pi/3, 2*np.pi/3, np.pi/5, 0, 1)
    circdef.cu_gate(np.pi/3, np.pi/4, 2*np.pi/3, np.pi/6, 1, 2)
    circdef.cu_gate(np.pi/4, np.pi/6, 2*np.pi/3, np.pi/2, 2, 3)
    circdef.cu_gate(np.pi/5, np.pi/2, 2*np.pi/3, np.pi/3, 3, 4)
    assert np.round(statevector_qiskit(circdef), 3).tolist() == np.round([1.00000000e+00-8.45106957e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                          1.39522544e-18+2.17710947e-17j, 0.00000000e+00+0.00000000e+00j,
                                                                          -8.98385651e-19+2.34744432e-17j, 0.00000000e+00+0.00000000e+00j,
                                                                          -8.73769284e-18-7.68521223e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                          7.77752738e-19-2.95582339e-17j, 0.00000000e+00+0.00000000e+00j,
                                                                          6.11096685e-35+2.31133418e-34j, 0.00000000e+00+0.00000000e+00j,
                                                                          -9.24753408e-18-3.53910500e-19j, 0.00000000e+00+0.00000000e+00j,
                                                                          3.02751641e-18-3.44213115e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                          -4.13139347e-34+6.72197234e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                          2.18570485e-34+1.95153664e-35j, 0.00000000e+00+0.00000000e+00j,
                                                                          -5.37740566e-35+3.69909923e-37j, 0.00000000e+00+0.00000000e+00j,
                                                                          -2.76196315e-34+7.34481266e-35j, 0.00000000e+00+0.00000000e+00j,
                                                                          9.60405239e-18+2.52707183e-19j, 0.00000000e+00+0.00000000e+00j,
                                                                          -7.50998001e-35+1.98557349e-35j, 0.00000000e+00+0.00000000e+00j,
                                                                          1.14992492e-19-3.00470596e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                          1.11841621e-18+9.83699712e-19j, 0.00000000e+00+0.00000000e+00j], 3).tolist()

    assert np.round(statevector_cirq(circdef).astype(np.float64), 3).tolist() == np.round([1.00000000e+00-8.45106957e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                                           1.39522544e-18+2.17710947e-17j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -8.98385651e-19+2.34744432e-17j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -8.73769284e-18-7.68521223e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                                           7.77752738e-19-2.95582339e-17j, 0.00000000e+00+0.00000000e+00j,
                                                                                           6.11096685e-35+2.31133418e-34j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -9.24753408e-18-3.53910500e-19j, 0.00000000e+00+0.00000000e+00j,
                                                                                           3.02751641e-18-3.44213115e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -4.13139347e-34+6.72197234e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                                           2.18570485e-34+1.95153664e-35j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -5.37740566e-35+3.69909923e-37j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -2.76196315e-34+7.34481266e-35j, 0.00000000e+00+0.00000000e+00j,
                                                                                           9.60405239e-18+2.52707183e-19j, 0.00000000e+00+0.00000000e+00j,
                                                                                           -7.50998001e-35+1.98557349e-35j, 0.00000000e+00+0.00000000e+00j,
                                                                                           1.14992492e-19-3.00470596e-18j, 0.00000000e+00+0.00000000e+00j,
                                                                                           1.11841621e-18+9.83699712e-19j, 0.00000000e+00+0.00000000e+00j], 3).tolist()


def test_cu1_gate(circdef):
    circdef.cu1_gate(np.pi/4, 0, 1)
    circdef.cu1_gate(np.pi/3, 1, 2)
    circdef.cu1_gate(np.pi/2, 2, 3)
    circdef.cu1_gate(2*np.pi/3, 3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]


def test_cu3_gate(circdef):
    circdef.cu3_gate(np.pi/4, np.pi/3, 2*np.pi/3, 0, 1)
    circdef.cu3_gate(np.pi/3, np.pi/2, 2*np.pi/3, 1, 2)
    circdef.cu3_gate(np.pi/2, 2*np.pi/3, np.pi/2, 2, 3)
    circdef.cu3_gate(0, np.pi/5, 2*np.pi/3, 3, 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]

    assert statevector_cirq(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                  -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j, -0.+0.j]


def test_mcx_gate(circdef):
    circdef.mcx_gate([0, 1], 2)
    circdef.mcx_gate([0, 2], 1)
    circdef.mcx_gate([0, 3], 2)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_mcp_gate(circdef):
    circdef.mcp_gate(np.pi/4, [0, 1], 2)
    circdef.mcp_gate(np.pi/4, [0, 2, 3], 4)
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]


def test_mct_gate(circdef):
    circdef.mct_gate([0, 1], 2, [3, 4])
    circdef.mct_gate([0, 1], 3, [2, 4])
    circdef.mct_gate([0, 2], 1, [3, 4])
    assert statevector_qiskit(circdef).tolist() == [1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                                                    0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]
