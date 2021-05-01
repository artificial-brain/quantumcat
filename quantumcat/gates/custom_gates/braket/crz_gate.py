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


class CRZGate(Gate):
    """CRY Gate"""
    def __init__(self, theta):
        super(CRZGate, self).__init__(qubit_count=2, ascii_symbols=["C", "Rz"])
        self.theta = theta

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        pass

    @circuit.subroutine(register=True)
    def crz(self):
        arg = 1j * float(self.params[0]) / 2
        if self.ctrl_state:
            return np.array([[1, 0, 0, 0],
                            [0, np.exp(-arg), 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, np.exp(arg)]],)


Gate.register_gate(CRZGate)
