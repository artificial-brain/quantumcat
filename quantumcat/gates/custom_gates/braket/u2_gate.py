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

import numpy
from braket.circuits import *


class U2Gate(Gate):
    """U2 Gate"""

    def __init__(self, phi, lam):
        super(U2Gate, self).__init__()
        self.phi = phi
        self.lam = lam

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> numpy.ndarray:
        pass

    @circuit.subroutine(register=True)
    def u2(self, alpha, theta, phi):
        isqrt2 = 1 / numpy.sqrt(2)
        phi, lam = self.phi, self.lam
        phi, lam = float(phi), float(lam)
        return numpy.array([[isqrt2, -numpy.exp(1j * lam) * isqrt2],
            [numpy.exp(1j * phi) * isqrt2, numpy.exp(1j * (phi + lam)) * isqrt2]])


Gate.register_gate(U2Gate)
