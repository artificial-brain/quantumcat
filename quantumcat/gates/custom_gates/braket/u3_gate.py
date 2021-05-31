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


class U3Gate(AngledGate):
    """U3 Gate"""

    def __init__(self, angle: float, theta, phi, lam):
        super().__init__(
            angle=angle,
            qubit_count=1,
            ascii_symbols=["U3({:.3g})".format(angle)])
        self.theta = theta
        self.phi = phi
        self.lam = lam

    def to_ir(self, target: QubitSet):
        return ir.U3Gate.construct(target=target[0], angle=self.angle)

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        theta, phi, lam = float(self.theta), float(self.phi), float(self.lam)
        cos = np.cos(theta / 2)
        sin = np.sin(theta / 2)
        return np.array([[cos, -np.exp(1j * lam) * sin],
                         [np.exp(1j * phi) * sin, np.exp(1j * (phi + lam)) * cos]])

    @staticmethod
    @circuit.subroutine(register=True)
    def u3(target: QubitInput, angle: float) -> Instruction:
        return Instruction(Gate.U3Gate(angle), target=target[0])


Gate.register_gate(U3Gate)
