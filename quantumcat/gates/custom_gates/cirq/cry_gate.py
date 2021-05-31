import cirq
import numpy


class CRYGate(cirq.Gate):
    """
    The CRYGate class enables all the methods for the execution of the CRY gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self, theta):
        """
        Initializes CRYGate class and enables running of all associated methods.

        Parameters
        ----------

        <theta>: takes in the angle(in radian) to be rotated.
        """
        super(CRYGate, self).__init__()
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
        Provides the number of qubits required for the gate operation.
      
        Returns
        --------

        Number of qubits required.
        """
        theta2 = float(self.theta) / 2
        cos = numpy.cos(theta2)
        sin = numpy.sin(theta2)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, cos, -sin],
                            [0, 0, sin, cos]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CRY gate.

        Returns
        --------

        Schematic representation of CRY gate.
        """
        return ["CRY_c", "CRY_t"]
