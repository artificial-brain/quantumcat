from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CRZGate(lam, dtype=None):
    lamd = float(lam)/2
    lam1 = numpy.exp(-1j * lamd)
    lam2 = numpy.exp(1j * lamd)
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, lam1, 0],
                        [0, 0, 0, lam2]], dtype=dtype)
