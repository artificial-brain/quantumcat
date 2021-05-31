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
import math


class RGate(cirq.Gate):
    """
    The RGate class enables all the methods for the execution of the R gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """
    def __init__(self, theta, phi):
        """
        Initializes RGate class and enables running of all associated methods.

        Parameters
        ----------

        <theta>: takes in the angle(in radian) to be rotated.
        <phi>: takes in the angle(in radian) to be rotated.
        """
        super(RGate, self).__init__()
        self.theta = theta
        self.phi=phi

    def _num_qubits_(self):
        """
        Provides the number of qubits required for the gate operation.
      
        Returns
        --------

        Number of qubits required.
        """
        return 1

    def _unitary_(self, dtype=None):
        """
        Provides the unitary matrix of the gate operation.
      
        Returns
        --------

        Unitary matrix of gate.
        """
        theta, phi = float(self.theta), float(self.phi)
        cos = math.cos(theta / 2)
        sin = math.sin(theta / 2)
        exp_m = numpy.exp(-1j * phi)
        exp_p = numpy.exp(1j * phi)
        return numpy.array([[cos, -1j * exp_m * sin],
                            [-1j * exp_p * sin, cos]], dtype=dtype)


    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of R gate.

        Returns
        --------

        Schematic representation of R gate.
        """
        return f"R{self.theta, self.phi}"