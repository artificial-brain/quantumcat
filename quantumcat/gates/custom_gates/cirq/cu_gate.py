import cirq
import numpy


class CUGate(cirq.Gate):

    def __init__(self, theta, phi, lam, gam):
        super(CUGate, self).__init__()
        self.theta = theta
        self.phi = phi
        self.lam = lam
        self.gam = gam

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
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
        return ["CU_c", "CU_t"]
