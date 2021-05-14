import cirq
import numpy


class CU3Gate(cirq.Gate):

    def __init__(self, theta, phi, lam):
        super(CU3Gate, self).__init__()
        self.theta = theta
        self.phi = phi
        self.lam = lam

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
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
        return ["CU3_c", "CU3_t"]
