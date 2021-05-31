import cirq
import numpy


class CU3Gate(cirq.Gate):
    """
    The CU3Gate class enables all the methods for the execution of the CU3 gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self, theta, phi, lam):
        """
        Initializes CU3Gate class and enables running of all associated methods.

        Parameters
        ----------

        <theta>: takes in the angle(in radian) to be rotated.
        <phi>: takes in the angle(in radian) to be rotated.
        <lam>: takes in the angle(in radian) to be rotated.
        """
        super(CU3Gate, self).__init__()
        self.theta = theta
        self.phi = phi
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
        cos = numpy.cos(self.theta/2)
        sin = numpy.sin(self.theta/2)
        exp1 = numpy.exp(1j*self.lam)
        exp2 = numpy.exp(1j*self.phi)
        exp3 = numpy.exp(1j*(self.phi+self.lam))
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, cos, -1*exp1*sin],
                            [0, 0, exp2*sin, exp3*cos]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CU3 gate.

        Returns
        --------

        Schematic representation of CU3 gate.
        """
        return ["CU3_c", "CU3_t"]
