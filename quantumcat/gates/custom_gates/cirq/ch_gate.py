import cirq
import numpy


class CHGate(cirq.Gate):
    """
    The CHGate class enables all the methods for the execution of the CH gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self):
        """
        Initializes CHGate class and enables running of all associated methods.
        """
        super(CHGate, self).__init__()

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
        sqt2 = numpy.sqrt(2)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0] ,
                            [0, 0, 1/sqt2, 1/sqt2],
                            [0, 0, 1/sqt2, -1/sqt2]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CH gate.

        Returns
        --------

        Schematic representation of CH gate.
        """
        return ["CH_c", "CH_t"]
