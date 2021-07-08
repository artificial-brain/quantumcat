from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CRXGate(theta, dtype=None):
    theta2 = float(theta) / 2
    cos = numpy.cos(theta2)
    isin = 1j * numpy.sin(theta2)
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, cos, -isin],
                        [0, 0, -isin, cos]], dtype=dtype)
