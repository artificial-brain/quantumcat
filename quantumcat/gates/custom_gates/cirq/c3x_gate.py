import cirq
import numpy


class C3XGate(cirq.Gate):
    """
    The C3XGate class enables all the methods for the execution of the C3X gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self):
        """
        Initializes C3XGate class and enables running of all associated methods.
        """
        super(C3XGate, self).__init__()

    def _num_qubits_(self):
        """
        Provides the number of qubits required for the gate operation.
      
        Returns:
            Number of qubits required.
        """
        return 4

    def _unitary_(self, dtype=None):
        """
        Provides the unitary matrix of the gate operation.

        Args:
            dtype: dtype.
      
        Returns:
            mat: Unitary matrix of gate.
        """
        mat = numpy.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]], dtype=dtype)
        return mat

    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of C3X gate.

        Args:
            args: index names of qubits.

        Returns:
            Schematic representation of C3X gate.
        """
        return ["C3X_c1", "C3X_c2", "C3X_c3", "C3X_t"]
