import cirq
import numpy


class CPhaseGate(cirq.Gate):
    """
    The CPhaseGate class enables all the methods for the execution of the CPhase gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self, lam):
        """
        Initializes CPhaseGate class and enables running of all associated methods.

        Parameters
        ----------

        <lam>: takes in the angle(in radian) to be rotated.
        """
        super(CPhaseGate, self).__init__()
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
        Provides the unitary matrix of the gate operation.
      
        Returns
        --------

        Unitary matrix of gate.
        """
        exp1 = numpy.exp(1j*self.lam)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, exp1]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CPhase gate.

        Returns
        --------

        Schematic representation of CPhase gate.
        """
        return ["CPhase_c", "CPhase_t"]
