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

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        pass

    @circuit.subroutine(register=True)
    def u3(self, alpha, theta, phi):
        """
        function to return matrix for general single qubit rotation
        rotation is given by exp(-i sigma*n/2*alpha) where alpha is rotation angle
        and n defines rotation axis as n=(sin(theta)cos(phi), sin(theta)sin(phi), cos(theta))
        sigma is vector of Pauli matrices
        """
        u11 = np.cos(alpha/2)-1j*np.sin(alpha/2)*np.cos(theta)
        u12 = -1j*(np.exp(-1j*phi))*np.sin(theta)*np.sin(alpha/2)
        u21 = -1j*(np.exp(1j*phi))*np.sin(theta)*np.sin(alpha/2)
        u22 = np.cos(alpha/2)+1j*np.sin(alpha/2)*np.cos(theta)

        return np.array([[u11, u12], [u21, u22]])


Gate.register_gate(U3Gate)
