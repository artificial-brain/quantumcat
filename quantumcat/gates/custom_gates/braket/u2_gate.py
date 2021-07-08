from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def U2Gate(phi, lam, dtype=None):
    isqrt2 = 1 / numpy.sqrt(2)
    phi, lam = float(phi), float(lam)
    return numpy.array([[isqrt2, -numpy.exp(1j * lam) * isqrt2],
                        [numpy.exp(1j * phi) * isqrt2, numpy.exp(1j * (phi + lam)) * isqrt2]], dtype=dtype)
