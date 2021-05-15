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
from braket.circuits import Instruction, Gate, QubitSet, QubitInput, circuit, AngledGate


class U2Gate(AngledGate):
    """U2 Gate"""

    def __init__(self, angle: float, phi, lam):
        super().__init__(
            angle=angle,
            qubit_count=1,
            ascii_symbols=["U2({:.3g})".format(angle)])
        self.phi = phi
        self.lam = lam

    def to_ir(self, target: QubitSet):
        return ir.U2Gate.construct(target=target[0], angle=self.angle)

    def to_matrix(self, *args, **kwargs) -> numpy.ndarray:
        isqrt2 = 1 / numpy.sqrt(2)
        phi, lam = self.phi, self.lam
        phi, lam = float(phi), float(lam)
        return numpy.array([[isqrt2, -numpy.exp(1j * lam) * isqrt2],
                            [numpy.exp(1j * phi) * isqrt2, numpy.exp(1j * (phi + lam)) * isqrt2]])

    @staticmethod
    @circuit.subroutine(register=True)
    def u2(target: QubitInput, angle: float) -> Instruction:
        return Instruction(Gate.U2Gate(angle), target=target)


Gate.register_gate(U2Gate)
