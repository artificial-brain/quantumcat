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


class CRXGate(AngledGate):
    """CRX Gate"""
    def __init__(self, angle: float):
        super().__init__(
            angle=angle,
            qubit_count=2,
            ascii_symbols=["CRX({:.3g})".format(angle), "CRX({:.3g})".format(angle)])

    def to_ir(self, target: QubitSet):
        ir.CRXGate.construct(control=target[0], target=target[1], angle=self.angle)

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        half_theta = float(self.angle) / 2
        cos = np.cos(half_theta)
        isin = 1j * np.sin(half_theta)
        return np.array([[1, 0, 0, 0],
                         [0, cos, 0, -isin],
                         [0, 0, 1, 0],
                         [0, -isin, 0, cos]])

    @staticmethod
    @circuit.subroutine(register=True)
    def crx(control: QubitInput, target: QubitInput, angle: float) -> Instruction:
        return Instruction(Gate.CRXGate(angle), target=[control, target])


Gate.register_gate(CRXGate)
