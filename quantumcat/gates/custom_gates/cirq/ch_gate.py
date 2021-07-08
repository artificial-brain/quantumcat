import cirq
import numpy


class CHGate(cirq.Gate):

    def __init__(self):
        super(CHGate, self).__init__()

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
        _sqrt2o2 = 1 / numpy.sqrt(2)
        return numpy.array([[1, 0, 0, 0],
                            [0, _sqrt2o2, 0, _sqrt2o2],
                            [0, 0, 1, 0],
                            [0, _sqrt2o2, 0, -_sqrt2o2]],
                           dtype=complex)
    def _circuit_diagram_info_(self, args):
        return ["CH_c", "CH_t"]
