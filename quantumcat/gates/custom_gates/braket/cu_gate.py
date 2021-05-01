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


class CUGate(Gate):
    """CU Gate"""
    def __init__(self, theta, phi, lam, gamma):
        super(CUGate, self).__init__(qubit_count=2, ascii_symbols=["C", "U"])
        self.theta = theta
        self.phi = phi
        self.lam = lam
        self.gamma = gamma

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        pass

    @circuit.subroutine(register=True)
    def cu(self):
        cos = np.cos(self.theta / 2)
        sin = np.sin(self.theta / 2)
        a = np.exp(1j * self.gamma) * cos
        b = -np.exp(1j * (self.gamma + self.lam)) * sin
        c = np.exp(1j * (self.gamma + self.phi)) * sin
        d = np.exp(1j * (self.gamma + self.phi + self.lam)) * cos
        return np.array([[1, 0, 0, 0],
                        [0, a, 0, b],
                        [0, 0, 1, 0],
                        [0, c, 0, d]])


Gate.register_gate(CUGate)
