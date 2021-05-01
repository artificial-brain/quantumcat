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
from typing import Any

import numpy as np
from braket.circuits import *


class U3Gate(Gate):
    """U3 Gate"""

    def __init__(self, theta, phi, lam):
        super().__init__(qubit_count=1, ascii_symbols=["U3"])
        self.theta = theta
        self.phi = phi
        self.lam = lam

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        pass

    @circuit.subroutine(register=True)
    def u3(self, target):
        """
        Function to return the matrix for a general single qubit rotation,
        given by exp(-i sigma*n/2*alpha), where alpha is the rotation angle,
        n defines the rotation axis via n=(sin(theta)cos(phi), sin(theta)sin(phi), cos(theta)),
        and sigma is the vector of Pauli matrices
        """

        u11 = np.cos(self.theta/2)-1j*np.sin(self.theta/2)*np.cos(self.phi)
        u12 = -1j*(np.exp(-1j*self.lam))*np.sin(self.phi)*np.sin(self.theta/2)
        u21 = -1j*(np.exp(1j*self.lam))*np.sin(self.phi)*np.sin(self.theta/2)
        u22 = np.cos(self.theta/2)+1j*np.sin(self.theta/2)*np.cos(self.phi)


        # define unitary as numpy matrix
        u = np.array([[u11, u12], [u21, u22]])
        # print('Unitary:', u)

        # define custom Braket gate
        circ = Circuit()
        circ.unitary(matrix=u, targets=target)

        return circ


Gate.register_gate(U3Gate)
