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
import math


class RGate(Gate):
    """UR Gate"""

    def __init__(self, theta, phi):
        super(RGate, self).__init__(qubit_count=1, ascii_symbols=["R"])
        self.theta = float(theta)
        self.phi = float(phi)

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> numpy.ndarray:
        pass

    @circuit.subroutine(register=True)
    def r(self):
        cos = math.cos(self.theta / 2)
        sin = math.sin(self.theta / 2)
        exp_m = numpy.exp(-1j * self.phi)
        exp_p = numpy.exp(1j * self.phi)
        return numpy.array([[cos, -1j * exp_m * sin],
                            [-1j * exp_p * sin, cos]])


Gate.register_gate(RGate)
