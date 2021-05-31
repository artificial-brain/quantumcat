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


class UGate(AngledGate):
    """U Gate"""

    def __init__(self, angle: float, theta, phi, lam):
        super(UGate, self).__init__(qubit_count=1, ascii_symbols=["U"])
        self.theta = theta
        self.phi = phi
        self.lam = lam

    def to_ir(self, target: QubitSet):
        return ir.UGate.construct(target=target[0], angle=self.angle)

    def to_matrix(self, *args, **kwargs) -> np.ndarray:
        return np.array([[np.cos(self.theta / 2), -np.exp(1j * self.lam) * np.sin(self.theta / 2)],
                         [np.exp(1j * self.phi) * np.sin(self.theta / 2), np.exp(1j * (self.phi + self.lam)) * np.cos(self.theta / 2)]], dtype=None)

    @staticmethod
    @circuit.subroutine(register=True)
    def u(target: QubitInput, angle: float):
        return Instruction(Gate.UGate(angle), target=target)


Gate.register_gate(UGate)
