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

from braket.circuits import *
import numpy


class U1Gate(Gate):
    """U1 Gate"""

    def __init__(self, theta):
        super(U1Gate, self).__init__(qubit_count=1, ascii_symbols=["U1"])
        self.theta = theta

    @circuit.subroutine(register=True)
    def _unitary_(self, dtype=None):
        lam = float(self.theta)
        return numpy.array([[1, 0], [0, numpy.exp(1j * lam)]], dtype=dtype)


Gate.register_gate(U1Gate)
