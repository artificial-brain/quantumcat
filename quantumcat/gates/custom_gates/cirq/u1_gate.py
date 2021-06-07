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


class U1Gate(cirq.Gate):
    """
    The U1Gate class enables all the methods for the execution of the U1 Gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """
    def __init__(self, theta):
        """
        Initializes U1Gate class and enables running of all associated methods.

        Args:
            theta: angle(in radian) to be rotated.
        """
        super(U1Gate, self).__init__()
        self.theta = theta

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
        lam = float(self.theta)
        return numpy.array([[1, 0],
                            [0, numpy.exp(1j * lam)]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of U1 Gate.
        
        Args:
            args: index names of qubits.

        Returns:
            Schematic representation of U1 Gate.
        """
        return f"U1({self.theta})"
