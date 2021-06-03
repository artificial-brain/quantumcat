import cirq
import numpy


class CSXGate(cirq.Gate):
    """
    The CSXGate class enables all the methods for the execution of the CSX gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self):
        """
        Initializes CSXGate class and enables running of all associated methods.
        """
        super(CSXGate, self).__init__()

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
        par1 = (1+1j)/2
        par2 = (1-1j)/2
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, par1, par2],
                            [0, 0, par2, par1]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CSX gate.

        Args:
            args: index names of qubits.

        Returns:
            Schematic representation of CSX gate.
        """
        return ["CSX_c", "CSX_t"]
