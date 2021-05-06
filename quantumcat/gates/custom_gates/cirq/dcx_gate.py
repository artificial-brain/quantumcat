import cirq
import numpy


class DCXGate(cirq.Gate):

    def __init__(self):
        super(DCXGate, self).__init__()

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
        return numpy.array([[1, 0, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1],
                            [0, 1, 0, 0]], dtype=dtype)

    def _circuit_diagram_info_(self, args):
        return ["DCX_c1", "DCX_c2"]
