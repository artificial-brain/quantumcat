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


class UGate(Gate):
    """U Gate"""

    def __init__(self, theta, phi, lam):
        super(UGate, self).__init__()
        self.theta = theta
        self.phi = phi
        self.lam = lam

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> numpy.ndarray:
        pass

    @circuit.subroutine(register=True)
    def u(self, theta, phi, lam):
        return numpy.array([
            [numpy.cos(self.theta / 2), -numpy.exp(1j * self.lam) * numpy.sin(self.theta / 2)],
            [numpy.exp(1j * self.phi) * numpy.sin(self.theta / 2), numpy.exp(1j * (self.phi + self.lam))
                * numpy.cos(self.theta / 2)]], dtype=None)


Gate.register_gate(UGate)
