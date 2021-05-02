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

import numpy
import braket.ir.jaqcd as ir
from braket.circuits import Instruction, Gate, QubitSet, QubitInput, circuit


class RCCXGate(Gate):
    """RCCX Gate"""

    def __init__(self):
        super().__init__(qubit_count=3, ascii_symbols=["RC", "C", "X"])

    def to_ir(self, target: QubitSet):
        return ir.RCCXGate.construct(controls=[target[0], target[1]], target=target[2])

    def to_matrix(self, *args, **kwargs) -> numpy.ndarray:
        return numpy.array([[1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, -1j],
                            [0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, -1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 1j, 0, 0, 0, 0]])

    @staticmethod
    @circuit.subroutine(register=True)
    def rccx(control1: QubitInput, control2: QubitInput, target: QubitInput) -> Instruction:
        return Instruction(Gate.RCCXGate(), target=[control1, control2, target])


Gate.register_gate(RCCXGate)
