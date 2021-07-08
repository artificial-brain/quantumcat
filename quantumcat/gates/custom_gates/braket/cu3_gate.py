from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CU3Gate(theta, phi, lam, dtype=None):
    cos = numpy.cos(theta/2)
    sin = numpy.sin(theta/2)
    exp1 = numpy.exp(1j*lam)
    exp2 = numpy.exp(1j*phi)
    exp3 = numpy.exp(1j*(phi+lam))
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, cos, -1*exp1*sin],
                        [0, 0, exp2*sin, exp3*cos]], dtype=dtype)
