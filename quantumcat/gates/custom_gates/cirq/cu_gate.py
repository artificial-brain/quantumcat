import cirq
import numpy


class CUGate(cirq.Gate):
    """
    The CUGate class enables all the methods for the execution of the CU gate.
    The class methods initializes the operation, performs the calculation and generates a schematic representation.
    """

    def __init__(self, theta, phi, lam, gam):
        """
        Initializes CUGate class and enables running of all associated methods.

        Args:
            theta: angle(in radian) to be rotated.
            phi: angle(in radian) to be rotated.
            lam: angle(in radian) to be rotated.
            gam: angle(in radian) to be rotated.
        """
        super(CUGate, self).__init__()
        self.theta = theta
        self.phi = phi
        self.lam = lam
        self.gam = gam

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
        cos = numpy.cos(self.theta/2)
        sin = numpy.sin(self.theta/2)  
        exp1 = numpy.exp(1j*self.gam)
        exp2 = numpy.exp(1j*(self.gam+self.lam))
        exp3 = numpy.exp(1j*(self.gam+self.phi))
        exp4 = numpy.exp(1j*(self.gam+self.phi+self.lam))
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, exp1*cos, -exp2*sin],
                            [0, 0, exp3*sin, exp4*cos]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        """
        Generates circuit representation of CU gate.

        Args:
            args: index names of qubits.

        Returns:
            Schematic representation of CU gate.
        """
        return ["CU_c", "CU_t"]
