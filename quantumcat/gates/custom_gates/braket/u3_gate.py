from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def U3Gate(theta, phi, lam, dtype=None):
    theta, phi, lam = float(theta), float(phi), float(lam)
    cos = numpy.cos(theta / 2)
    sin = numpy.sin(theta / 2)
    return numpy.array([[cos, -numpy.exp(1j * lam) * sin],
                        [numpy.exp(1j * phi) * sin, numpy.exp(1j * (phi + lam)) * cos]], dtype=dtype)
