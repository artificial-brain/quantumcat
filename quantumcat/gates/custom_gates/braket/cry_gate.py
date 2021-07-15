from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CRYGate(theta, dtype=None):
    theta2 = float(theta) / 2
    cos = numpy.cos(theta2)
    sin = numpy.sin(theta2)
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, cos, -sin],
                        [0, 0, sin, cos]], dtype=dtype)
