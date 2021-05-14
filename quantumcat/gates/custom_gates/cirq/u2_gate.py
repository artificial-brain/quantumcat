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
import cirq
import numpy


class U2Gate(cirq.Gate):
    def __init__(self, phi, lam):
        super(U2Gate, self).__init__()
        self.phi = phi
        self.lam = lam

    def _num_qubits_(self):
        return 1

    def _unitary_(self, dtype=None):
        isqrt2 = 1 / numpy.sqrt(2)
        phi, lam = self.phi, self.lam
        phi, lam = float(phi), float(lam)
        return numpy.array([[isqrt2, -numpy.exp(1j * lam) * isqrt2],
                            [numpy.exp(1j * phi) * isqrt2, numpy.exp(1j * (phi + lam)) * isqrt2]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        return f"U2{self.phi, self.lam}"
