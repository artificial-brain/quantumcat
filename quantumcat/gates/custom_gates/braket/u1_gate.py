from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def U1Gate(theta, dtype=None):
    lam = float(theta)
    return numpy.array([[1, 0],
                        [0, numpy.exp(1j * lam)]], dtype=dtype)
