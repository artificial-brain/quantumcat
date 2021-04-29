import cirq
import numpy


class CRYGate(cirq.Gate):

    def __init__(self, theta):
        super(CRYGate, self).__init__()
        self.theta = theta

    def _num_qubits_(self):
        return 2

    def _unitary_(self, dtype=None):
        theta2 = float(self.theta) / 2
        cos = numpy.cos(theta2)
        sin = numpy.sin(theta2)
        return numpy.array([[1, 0, 0, 0], [0, cos, 0, -sin], [0, 0, 1, 0], [0, sin, 0, cos]],
                           dtype=dtype)

    def _circuit_diagram_info_(self, args):
       return ["CRYGate"] * self.num_qubits()
