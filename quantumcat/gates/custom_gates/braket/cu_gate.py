from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CUGate(theta, phi, lam, gam, dtype=None):
    theta, phi, lam, gam = float(theta), float(phi), float(lam), float(gam)
    cos = numpy.cos(theta/2)
    sin = numpy.sin(theta/2)
    exp1 = numpy.exp(1j*gam)
    exp2 = numpy.exp(1j*(gam+lam))
    exp3 = numpy.exp(1j*(gam+phi))
    exp4 = numpy.exp(1j*(gam+phi+lam))
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, exp1*cos, -exp2*sin],
                        [0, 0, exp3*sin, exp4*cos]], dtype=dtype)
