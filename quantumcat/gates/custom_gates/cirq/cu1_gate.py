import cirq
import numpy


class CU1Gate(cirq.Gate):

    def __init__(self, lam):
        super(CU1Gate, self).__init__()
        self.lam = lam

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
        exp1 = numpy.exp(1j*self.lam)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, exp1]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        return ["CU1_c", "CU1_t"]
