import cirq
import numpy


class C3XGate(cirq.Gate):

    def __init__(self):
        super(C3XGate, self).__init__()

    def _num_qubits_(self):
        return 4

    def _unitary_(self, dtype=None):
        mat = _compute_control_matrix(self.base_gate.to_matrix(),
                                      self.num_ctrl_qubits,
                                      ctrl_state=self.ctrl_state)
        if dtype:
            return numpy.asarray(mat, dtype=dtype)
        return mat
    
    def _circuit_diagram_info_(self, args):
        return ["C3XGate"] * self.num_qubits()
