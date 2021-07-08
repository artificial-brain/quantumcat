from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def DCXGate(dtype=None):
    return numpy.array([[1, 0, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1],
                            [0, 1, 0, 0]], dtype=dtype)
