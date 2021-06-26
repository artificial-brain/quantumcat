from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CHGate(dtype=None):
    _sqrt2o2 = 1 / numpy.sqrt(2)
    return numpy.array([[1, 0, 0, 0],
                        [0, _sqrt2o2, 0, _sqrt2o2],
                        [0, 0, 1, 0],
                        [0, _sqrt2o2, 0, -_sqrt2o2]],
                       dtype=complex)
