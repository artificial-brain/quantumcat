import cirq
import numpy


class CRZGate(cirq.Gate):

    def __init__(self, lam):
        super(CRZGate, self).__init__()
        self.lam = lam

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
        lamd = float(self.lam)/2
        lam1 = numpy.exp(-1j * lamd)
        lam2 = numpy.exp(1j * lamd)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, lam1, 0],
                            [0, 0, 0, lam2]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        return ["CRZ_c", "CRZ_t"]
