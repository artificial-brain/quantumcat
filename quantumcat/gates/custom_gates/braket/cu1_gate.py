from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CU1Gate(lam, dtype=None):
    exp1 = numpy.exp(1j*lam)
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, exp1]], dtype=dtype)
