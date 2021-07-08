from braket.circuits import circuit
import numpy


@circuit.subroutine(register=True)
def CSXGate(dtype=None):
    par1 = (1+1j)/2
    par2 = (1-1j)/2
    return numpy.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, par1, par2],
                        [0, 0, par2, par1]], dtype=dtype)
