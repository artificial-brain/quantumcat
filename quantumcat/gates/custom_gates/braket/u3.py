from braket.circuits import circuit, Circuit
from braket.devices import LocalSimulator
import numpy as np


@circuit.subroutine(register=True)
def u3(theta, phi, lam, target):
    # print(theta, phi, lam, target)

    # set 2x2 matrix entries
    u11 = np.cos(theta/2)-1j*np.sin(theta/2)*np.cos(phi)
    u12 = -1j*(np.exp(-1j*lam))*np.sin(phi)*np.sin(theta/2)
    u21 = -1j*(np.exp(1j*lam))*np.sin(phi)*np.sin(theta/2)
    u22 = np.cos(theta/2)+1j*np.sin(theta/2)*np.cos(lam)

    # define unitary as numpy matrix
    u = np.array([[u11, u12], [u21, u22]])
    # print('Unitary:', u)

    # define custom Braket gate
    circ = Circuit()
    circ.unitary(matrix=u, targets=target, display_name="U3")

    return circ


# define example circuit applying custom single-qubit gate U to the first qubit
# angles = [np.pi/2, np.pi/2, np.pi/2]
# theta, phi, lam = np.pi/2, np.pi/2, np.pi/2

# build circuit using custom u3 gate
circ2 = Circuit().u3(np.pi/2, np.pi/2, np.pi/2, [0])
print(LocalSimulator().run(circ2.state_vector(), shots=0).result().values[0])
print(circ2)

