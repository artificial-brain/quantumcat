from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def RZXGate(theta, dtype=None):
    half_theta = float(theta) / 2
    cos = numpy.cos(half_theta)
    isin = 1j * numpy.sin(half_theta)
    return numpy.array([[cos, 0, -isin, 0],
                        [0, cos, 0, isin],
                        [-isin, 0, cos, 0],
                        [0, isin, 0, cos]], dtype=dtype)
