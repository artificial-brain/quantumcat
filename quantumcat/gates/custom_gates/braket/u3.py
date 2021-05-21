import numpy as np
from braket.circuits import Circuit, circuit


@circuit.subroutine(register=True)
def u3(theta, phi, lam, target):
    """
    Function to return the matrix for a general single qubit rotation,
    given by exp(-i sigma*n/2*alpha), where alpha is the rotation angle,
    n defines the rotation axis via n=(sin(theta)cos(phi), sin(theta)sin(phi), cos(theta)),
    and sigma is the vector of Pauli matrices
    """
    print(target)
    # get angles
    alpha = theta
    theta = phi
    phi = lam

    # set 2x2 matrix entries
    u11 = np.cos(alpha/2)-1j*np.sin(alpha/2)*np.cos(theta)
    u12 = -1j*(np.exp(-1j*phi))*np.sin(theta)*np.sin(alpha/2)
    u21 = -1j*(np.exp(1j*phi))*np.sin(theta)*np.sin(alpha/2)
    u22 = np.cos(alpha/2)+1j*np.sin(alpha/2)*np.cos(theta)

    # define unitary as numpy matrix
    u = np.array([[u11, u12], [u21, u22]])
    # print('Unitary:', u)

    # define custom Braket gate
    circ = Circuit()
    circ.unitary(matrix=u, targets=[target], display_name="U3")

    return circ


# angles = [np.pi/2, np.pi/2, np.pi/2]

# build circuit using custom u3 gate
# circ2 = Circuit().u3(np.pi/2, np.pi/2, np.pi/2, 0).cnot(control=0, target=1)
# print(circ2)
