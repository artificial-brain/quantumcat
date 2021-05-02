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
from braket.circuits import Instruction, AngledGate, QubitSet, QubitInput, circuit, Gate


class CU1Gate(AngledGate):
    """CU1 Gate"""
    def __init__(self, angle: float):
        super().__init__(
            angle=angle,
            qubit_count=2,
            ascii_symbols=["CU1({:.3g})".format(angle), "CU1({:.3g})".format(angle)],
        )

    def to_ir(self, target: QubitSet):
        return ir.CU1Gate.construct(targets=[target[0], target[1]], angle=self.angle)

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        eith = np.exp(1j * float(self.angle))
        return np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, eith]])

    @staticmethod
    @circuit.subroutine(register=True)
    def cu1(target1: QubitInput, target2: QubitInput, angle: float) -> Instruction:
        return Instruction(Gate.CU1Gate(angle), target=[target1, target2])


Gate.register_gate(CU1Gate)
