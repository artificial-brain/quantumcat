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


class RXXGate(cirq.Gate):
    def __init__(self, theta):
        super(RXXGate, self).__init__()
        self.theta = theta

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
        theta2 = float(self.theta) / 2
        cos = numpy.cos(theta2)
        isin = 1j * numpy.sin(theta2)
        return numpy.array([[cos, 0, 0, -isin],
                            [0, cos, -isin, 0],
                            [0, -isin, cos, 0],
                            [-isin, 0, 0, cos]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        return [f"RXX({self.theta})"] * self.num_qubits()
