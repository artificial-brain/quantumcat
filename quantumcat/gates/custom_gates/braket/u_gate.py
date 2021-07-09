from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def UGate(theta, phi, lam, dtype=None):
    theta, phi, lam = float(theta), float(phi), float(lam)
    return numpy.array([[numpy.cos(theta / 2), -numpy.exp(1j * lam) * numpy.sin(theta / 2)],
                        [numpy.exp(1j * phi) * numpy.sin(theta / 2), numpy.exp(1j * (phi + lam))* numpy.cos(theta / 2)]], dtype=dtype)
