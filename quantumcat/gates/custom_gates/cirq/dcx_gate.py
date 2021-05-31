import cirq
import numpy


class DCXGate(cirq.Gate):
    """
    The DCXGate class enables all the methods for the execution of the DCX gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self):
        """
        Initializes DCXGate class and enables running of all associated methods.
        """
        super(DCXGate, self).__init__()

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
        return numpy.array([[1, 0, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1],
                            [0, 1, 0, 0]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of DCX gate.

        Returns
        --------

        Schematic representation of DCX gate.
        """
        return ["DCX_c1", "DCX_c2"]
