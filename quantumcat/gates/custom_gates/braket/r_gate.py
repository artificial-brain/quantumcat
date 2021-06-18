from braket.circuits import circuit
import numpy
import math


@circuit.subroutine(register=True)
def RGate(theta, phi, dtype=None):
    theta, phi = float(theta), float(phi)
    cos = math.cos(theta / 2)
    sin = math.sin(theta / 2)
    exp_m = numpy.exp(-1j * phi)
    exp_p = numpy.exp(1j * phi)
    return numpy.array([[cos, -1j * exp_m * sin],
                        [-1j * exp_p * sin, cos]], dtype=dtype)
