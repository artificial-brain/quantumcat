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


class CSXGate(Gate):
    """CSX Gate"""
    def __init__(self):
        super(CSXGate, self).__init__(qubit_count=2, ascii_symbols=["C", "Sx"])

    def to_ir(self, target: QubitSet) -> Any:
        pass

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        pass

    @circuit.subroutine(register=True)
    def ch(self):
        return np.array([[1, 0, 0, 0],
                        [0, (1 + 1j) / 2, 0, (1 - 1j) / 2],
                        [0, 0, 1, 0],
                        [0, (1 - 1j) / 2, 0, (1 + 1j) / 2]])


Gate.register_gate(CSXGate)