import cirq
import numpy


class CSXGate(cirq.Gate):

    def __init__(self):
        super(CSXGate, self).__init__()

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
        par1 = (1+1j)/2
        par2 = (1-1j)/2
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, par1, par2],
                            [0, 0, par2, par1]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        return ["CSX_c", "CSX_t"]
