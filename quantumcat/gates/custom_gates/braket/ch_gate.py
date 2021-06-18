from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CHGate(dtype=None):
    sqt2 = numpy.sqrt(2)
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1/sqt2, 1/sqt2],
                        [0, 0, 1/sqt2, -1/sqt2]], dtype=dtype)
