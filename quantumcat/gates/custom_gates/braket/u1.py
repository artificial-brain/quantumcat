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

import numpy as np
import braket.ir.jaqcd as ir
from braket.circuits import Instruction, Gate, QubitSet, QubitInput, circuit, AngledGate


class U1Gate(AngledGate):
    """U1 Gate"""

    def __init__(self, angle: float):
        super().__init__(
            angle=angle,
            qubit_count=1, ascii_symbols=["U1({:.3g})".format(angle)])

    def to_ir(self, target: QubitSet):
        return ir.XY.construct(target=target[0], angle=self.angle)

    def to_matrix(self) -> np.ndarray:
        lam = float(self.angle)
        return np.array([[1, 0], [0, np.exp(1j * lam)]])

    @staticmethod
    @circuit.subroutine(register=True)
    def u1(target: QubitInput, angle: float) -> Instruction:
        return Instruction(Gate.U1Gate(angle), target=target)


Gate.register_gate(U1Gate)
