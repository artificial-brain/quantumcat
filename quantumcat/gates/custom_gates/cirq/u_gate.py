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


class UGate(cirq.Gate):
    """
    The UGate class enables all the methods for the execution of the U Gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """
    def __init__(self, theta, phi, lam):
        """
        Initializes UGate class and enables running of all associated methods.

        Args:
            theta: angle(in radian) to be rotated.
            phi: angle(in radian) to be rotated.
            lam: angle(in radian) to be rotated.
        """
        super(UGate, self).__init__()
        self.theta = theta
        self.phi = phi
        self.lam = lam

    def _num_qubits_(self):
        """
        Provides the number of qubits required for the gate operation.
      
        Returns:
            Number of qubits required.
        """
        return 1

    def _unitary_(self, dtype=None):
        """
        Provides the unitary matrix of the gate operation.

        Args:
            dtype: dtype.
      
        Returns:
            mat: Unitary matrix of gate.
        """
        return numpy.array([[numpy.cos(self.theta / 2), -numpy.exp(1j * self.lam) * numpy.sin(self.theta / 2)],
                            [numpy.exp(1j * self.phi) * numpy.sin(self.theta / 2), numpy.exp(1j * (self.phi + self.lam))* numpy.cos(self.theta / 2)]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of U Gate.
        
        Args:
            args: index names of qubits.

        Returns:
            Schematic representation of U Gate.
        """
        return f"U{self.theta, self.phi, self.lam}"
