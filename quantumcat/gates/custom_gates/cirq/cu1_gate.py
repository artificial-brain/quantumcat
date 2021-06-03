import cirq
import numpy


class CU1Gate(cirq.Gate):
    """
    The CU1Gate class enables all the methods for the execution of the CU1 gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self, lam):
        """
        Initializes CU1Gate class and enables running of all associated methods.

        Args:
            lam: angle(in radian) to be rotated.
        """
        super(CU1Gate, self).__init__()
        self.lam = lam

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
        exp1 = numpy.exp(1j*self.lam)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, exp1]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CU1 gate.

        Args:
            args: index names of qubits.

        Returns:
            Schematic representation of CU1 gate.
        """
        return ["CU1_c", "CU1_t"]
