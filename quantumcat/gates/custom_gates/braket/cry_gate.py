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


class CRYGate(Gate):
    """CRY Gate"""
    def __init__(self, theta):
        super(CRYGate, self).__init__(qubit_count=2, ascii_symbols=["C", "Ry"])
        self.theta = theta

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        pass

    @circuit.subroutine(register=True)
    def cry(self):
        half_theta = float(self.theta) / 2
        cos = np.cos(half_theta)
        sin = np.sin(half_theta)
        return np.array([[1, 0, 0, 0],
                        [0, cos, 0, -sin],
                        [0, 0, 1, 0],
                        [0, sin, 0, cos]])


Gate.register_gate(CRYGate)
