import cirq
import numpy


class CRXGate(cirq.Gate):
    """
    The CRXGate class enables all the methods for the execution of the CRX gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self, theta):
        """
        Initializes CRXGate class and enables running of all associated methods.

        Args:
            theta: takes in the angle(in radian) to be rotated.
        """
        super(CRXGate, self).__init__()
        self.theta = theta

    def _num_qubits_(self):
        """
        Provides the number of qubits required for the gate operation.
      
        Returns:
            Number of qubits required.
        """
        return 2

    def _unitary_(self, dtype=None):
        """
        Provides the unitary matrix of the gate operation.

        Args:
            dtype: dtype.
      
        Returns:
            mat: Unitary matrix of gate.
        """
        theta2 = float(self.theta) / 2
        cos = numpy.cos(theta2)
        isin = 1j * numpy.sin(theta2)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, cos, -isin],
                            [0, 0, -isin, cos]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CRX gate.

        Args:
            args: index names of qubits.

        Returns:
            Schematic representation of CRX gate.
        """
        return ["CRX_c", "CRX_t"]
