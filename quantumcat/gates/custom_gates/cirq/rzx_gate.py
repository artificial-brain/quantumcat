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


class RZXGate(cirq.Gate):
    """
    The RZXGate class enables all the methods for the execution of the RZX Gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """
    def __init__(self, theta):
        """
        Initializes RZXGate class and enables running of all associated methods.

        Parameters
        ----------

        <theta>: takes in the angle(in radian) to be rotated.
        """
        super(RZXGate, self).__init__()
        self.theta = theta

    def _num_qubits_(self):
        """
        Provides the number of qubits required for the gate operation.
      
        Returns
        --------

        Number of qubits required.
        """
        return 2

    def _unitary_(self, dtype=None):
        """
        Provides the unitary matrix of the gate operation.
      
        Returns
        --------

        Unitary matrix of gate.
        """
        half_theta = float(self.theta) / 2
        cos = numpy.cos(half_theta)
        isin = 1j * numpy.sin(half_theta)
        return numpy.array([[cos, 0, -isin, 0],
                            [0, cos, 0, isin],
                            [-isin, 0, cos, 0],
                            [0, isin, 0, cos]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of RZX Gate.

        Returns
        --------

        Schematic representation of RZX Gate.
        """
        return [f"RZX({self.theta})"] * self.num_qubits()
