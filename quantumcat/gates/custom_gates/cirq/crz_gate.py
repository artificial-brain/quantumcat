import cirq
import numpy


class CRZGate(cirq.Gate):
    """
    The CRZGate class enables all the methods for the execution of the CRZ gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self, lam):
        """
        Initializes CRZGate class and enables running of all associated methods.

        Parameters
        ----------

        <theta>: takes in the angle(in radian) to be rotated.
        """
        super(CRZGate, self).__init__()
        self.lam = lam

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
        lamd = float(self.lam)/2
        lam1 = numpy.exp(-1j * lamd)
        lam2 = numpy.exp(1j * lamd)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, lam1, 0],
                            [0, 0, 0, lam2]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CRZ gate.

        Returns
        --------

        Schematic representation of CRZ gate.
        """
        return ["CRZ_c", "CRZ_t"]
