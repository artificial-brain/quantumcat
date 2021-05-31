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


class RZZGate(cirq.Gate):
    """
    The RZZGate class enables all the methods for the execution of the RZZ Gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """
    def __init__(self, theta):
        """
        Initializes RZZGate class and enables running of all associated methods.

        Parameters
        ----------

        <theta>: takes in the angle(in radian) to be rotated.
        """
        super(RZZGate, self).__init__()
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
        itheta2 = 1j * float(self.theta) / 2
        return numpy.array([[numpy.exp(-itheta2), 0, 0, 0],
                            [0, numpy.exp(itheta2), 0, 0],
                            [0, 0, numpy.exp(itheta2), 0],
                            [0, 0, 0, numpy.exp(-itheta2)]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of RZZ Gate.

        Returns
        --------

        Schematic representation of RZZ Gate.
        """
        return [f"RZZ({self.theta})"] * self.num_qubits()
