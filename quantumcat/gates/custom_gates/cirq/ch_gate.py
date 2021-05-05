import cirq
import numpy


class CHGate(cirq.Gate):

    def __init__(self):
        super(CHGate, self).__init__()

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
        sqt2 = numpy.sqrt(2)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0] ,
                            [0, 0, 1/sqt2, 1/sqt2],
                            [0, 0, 1/sqt2, -1/sqt2]], dtype=dtype)
    
    def _circuit_diagram_info_(self, args):
        return ["CH_c", "CH_t"]
