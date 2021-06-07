# (C) Copyright Artificial Brain 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from quantumcat.circuit.op_type import OpType
from quantumcat.exceptions import CircuitError, APIDetailsNotFoundError
from quantumcat.utils import ErrorMessages
from quantumcat.circuit import convert
from quantumcat.utils import providers
from quantumcat.utils import constants
from quantumcat.circuit import execute_circuit


class QCircuit:
    """
    The QCircuit class functions to enable all the gate functions and also enable associated operations
    required for the successful execution of quantum circuits and validation of results. The class also provides
    the classical logic gates which are built from the quantum logic gates.
    """
    def __init__(self, qubits, provider=providers.DEFAULT_PROVIDER):
        """
        Function is aimed at initializing the QCircuit class and enable the smooth running of all the included
        operations.
        """
        super(QCircuit, self).__init__()
        self.qubits = qubits
        self.operations = []
        self.converted_q_circuit = None
        self.provider = provider

    def x_gate(self, qubit):
        """
        Produces a single qubit rotation of pi(in radian) angle along the X-axis.
        Flips the |0> state to |1> and vice versa.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.x_gate: [qubit]})
        return self

    def y_gate(self, qubit):
        """
        Produces a single qubit rotation of pi(in radian) angle along the Y-axis.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.y_gate: [qubit]})
        return self

    def z_gate(self, qubit):
        """
        Produces a single qubit rotation of pi(in radian) angle along the Z-axis.

        Args:
            qubit: index of qubit, to which the gate is to be applied.
        
        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.z_gate: [qubit]})
        return self

    def h_gate(self, qubit):
        """
        Produces a superposition of the state of |0> and |1>
        If the qubit is in |0> state, it changes to the |+> state.
        If the qubit is in |1> state, it changes to the |-> state.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.h_gate: [qubit]})
        return self

    def cx_gate(self, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the X gate to the target qubit.
        If the control qubit is in the |0> state, the X gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the X gate is performed on the target qubit.

        Args:
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cx_gate: [[control_qubit], [target_qubit]]})
        return self

    def cz_gate(self, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the Z gate to the target qubit.
        If the control qubit is in the |0> state, the Z gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the Z gate is performed on the target qubit.

        Args:
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.operations.append({OpType.cz_gate: [[control_qubit], [target_qubit]]})
        return self

    def ccx_gate(self, control_qubit1, control_qubit2, target_qubit):
        """
        Also known as the Toffoli gate. Uses 2 control qubits to decide the application of the X gate 
        to the target qubit. If both the control qubits are in the |1> state, the X gate is performed
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.
       
        Args:
            control_qubit1: index of control qubit 1, to which the gate is to be applied.
            control_qubit2: index of control qubit 2, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.ccx_gate: [[control_qubit1], [control_qubit2], [target_qubit]]})
        return self

    def ry_gate(self, theta, qubit):
        """
        Produces a single qubit rotation around the Y-axis, for a specific angle taken as input.

        Args:
            theta: the angle(in radian) to be rotated.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.ry_gate: [qubit],
                                constants.PARAMS: [theta]})
        return self

    def ryy_gate(self, theta, qubit1, qubit2):
        """
        Parametric two qubit gate, performing rotation of theta angle, about YY axis.

        Args:
        

        theta: the angle(in radian) to be rotated.
        qubit1: index of qubit, to which the gate is to be applied.
        qubit2: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append({OpType.ryy_gate: [[qubit1], [qubit2]],
                                constants.PARAMS: [theta]})
        return self

    def rzz_gate(self, theta, qubit1, qubit2):
        """
        Parametric two qubit gate, performing rotation of theta angle, about ZZ axis.

        Args:
            theta: the angle(in radian) to be rotated.
            qubit1: index of qubit, to which the gate is to be applied.
            qubit2: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append({OpType.rzz_gate: [[qubit1], [qubit2]],
                                constants.PARAMS: [theta]})
        return self

    def rzx_gate(self, theta, qubit1, qubit2):
        """
        Parametric two qubit gate, performing rotation of theta angle, about ZX axis.

        Args:
            theta: the angle(in radian) to be rotated.
            qubit1: index of qubit, to which the gate is to be applied.
            qubit2: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append({OpType.rzx_gate: [[qubit1], [qubit2]],
                                constants.PARAMS: [theta]})
        return self

    def rz_gate(self, phi, qubit):
        """
        Produces a single qubit rotation around the Z-axis, for a specific angle taken as input.

        Args:
            phi: the angle(in radian) to be rotated.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.rz_gate: [qubit],
                                constants.PARAMS: [phi]})
        return self

    # Couldn't file class to map ecr gates in gates_map.py
    # def ecr_gate(self, qubit1, qubit2):
    #     self.check_qubit_boundary(qubit1)
    #     self.check_qubit_boundary(qubit2)
    #     self.operations.append({OpType.ecr_gate: [[qubit1], [qubit2]]})

    def s_gate(self, qubit):
        """
        Produces a single qubit rotation of pi/2 around the Z axis.
        It is a Clifford gate and is known as root of Z gate.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.s_gate: [qubit]})
        return self

    def sdg_gate(self, qubit):
        """
        Produces a single qubit rotation of -pi/2 around the Z axis.
        It is a Clifford gate and is known as root of Z gate.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """

        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sdg_gate: [qubit]})
        return self

    def swap_gate(self, qubit1, qubit2):
        """
        Produces an interchange in the states of the target qubits.
        It is symmetric and a Clifford gate.

        Args:
            qubit1: index of qubit, to which the gate is to be applied.
            qubit2: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append(({OpType.swap_gate: [[qubit1], [qubit2]]}))
        return self

    def iswap_gate(self, qubit1, qubit2):
        """
        Produces an interchange in the states of the target qubits and also adds a phase of i,
        to the amplitudes of |01> and |10>.
        It is symmetric and a Clifford gate.

        Args:
            qubit1: index of qubit, to which the gate is to be applied.
            qubit2: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit_1)
        self.check_qubit_boundary(qubit_2)
        self.operations.append(({OpType.iswap_gate: [[qubit_1], [qubit_2]]}))
        return self

    def sx_gate(self, qubit):
        """
        Produces a single qubit rotation of pi/2 around the X axis.
        It is a Clifford gate and is known as root of X gate.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sx_gate: [qubit]})
        return self

    def sxd_gate(self, qubit):
        """
        Produces a single qubit rotation of -pi/2 around the X axis.
        It is a Clifford gate and is known as root of X gate.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sxd_gate: [qubit]})
        return self

    def t_gate(self, qubit):
        """
        Produces a single qubit rotation of pi/4 around the Z axis.
        It is a Clifford gate and is known as 4th root of Z gate.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.t_gate: [qubit]})
        return self

    def td_gate(self, qubit):
        """
        Produces a single qubit rotation of -pi/4 around the Z axis.
        It is a Clifford gate and is known as 4th root of Z gate.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.td_gate: [qubit]})
        return self

    def u_gate(self, theta, phi, lam, qubit):
        """
        Produces a single qubit rotation with 3 Euler angles. This is the most generic form of single
        qubit rotation operators and all the other rotation operators are specific instances of the U gate.

        Args:
            theta: angle(in radian) to be rotated.
            phi: angle(in radian) to be rotated.
            lam: angle(in radian) to be rotated.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.u_gate: [qubit],
                                constants.PARAMS: [theta, phi, lam]})
        return self

    def u1_gate(self, theta, qubit):
        """
        U1 gate is a special case of the U gate.
        Produces a single qubit rotation with theta = phi = 0 and angle theta.
        The U1 gate is equaivalent to the RZ gate.

        Args:
            theta: angle(in radian) to be rotated.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.u1_gate: [qubit],
                                constants.PARAMS: [theta]})
        return self

    def u2_gate(self, phi, lam, qubit):
        """
        U2 gate, is a special case of the U gate.
        Produces a single qubit rotation with theta = pi/2 and angles phi and lam.

        Args:
            phi: angle(in radian) to be rotated.
            lam: angle(in radian) to be rotated.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.u2_gate: [qubit],
                                constants.PARAMS: [phi, lam]})
        return self

    def u3_gate(self, theta, phi, lam, qubit):
        """
        The U Gate, which is same as the U gate, induces a single qubit rotation with 3 Euler angles. 
        This is the most generic form of single qubit rotation operators and all the other 
        rotation operators are specific instances of the U gate.

        Args:
            theta: angle(in radian) to be rotated.
            phi: angle(in radian) to be rotated.
            lam: angle(in radian) to be rotated.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append(({OpType.u3_gate: [qubit],
                                 constants.PARAMS: [theta, phi, lam]}))
        return self

    def cy_gate(self, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the Y gate to the target qubit.
        If the control qubit is in the |0> state, the Y gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the Y gate is performed on the target qubit.

        Args:
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.operations.append({OpType.cy_gate: [[control_qubit], [target_qubit]]})
        return self

    def i_gate(self, qubit):
        """
        The Identity gate does not effect any changes on the qubit.
        It's matrix is the identity matrix.
        This gate is primarily nominal and is not generally used in computation.

        Args:
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.i_gate: [qubit]})
        return self

    def rccx_gate(self, control_qubit1, control_qubit2, target_qubit):
        """
        Simplified 2 control Toffoli gate, where in the Toffoli gate is implemented up to relative phases.
        The simplified Toffoli gate is not equivalent to the Toffoli gate.
        It can be used in places where the Toffoli gate is uncomputed again.

        Args:
            control_qubit1: index of control qubit 1, to which the gate is to be applied.
            control_qubit2: index of control qubit 2, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.

        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.rccx_gate: [[control_qubit1], [control_qubit2], [target_qubit]]})
        return self

    def rc3x_gate(self, control_qubit1, control_qubit2, control_qubit3, target_qubit):
        """
        Simplified 3 control Toffoli gate, where in the Toffoli gate is implemented up to relative phases.
        The simplified Toffoli gate is not equivalent to the Toffoli gate.
        It can be used in places where the Toffoli gate is uncomputed again.

        Args:
            control_qubit1: index of control qubit 1, to which the gate is to be applied.
            control_qubit2: index of control qubit 2, to which the gate is to be applied.
            control_qubit3: index of control qubit 3, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(control_qubit3)
        self.check_qubit_boundary(target_qubit)
        self.operations.append(
            {OpType.rc3x_gate: [[control_qubit1], [control_qubit2], [control_qubit3], [target_qubit]]})
        return self

    def rxx_gate(self, theta, qubit1, qubit2):
        """
        Parametric two qubit gate, performing rotation of theta angle, about XX axis.

        Args:
            theta: the angle(in radian) to be rotated.
            qubit1: index of qubit, to which the gate is to be applied.
            qubit2: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append({OpType.rxx_gate: [[qubit1], [qubit2]], constants.PARAMS: [theta]})
        return self

    def rx_gate(self, theta, qubit):
        """
        Produces a single qubit rotation around the X-axis, for a specific angle taken as input.

        Args:
            theta: the angle(in radian) to be rotated.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.rx_gate: [qubit], constants.PARAMS: [theta]})
        return self

    def r_gate(self, theta, phi, qubit):
        """
        Produces a rotation of theta, around the cos(phi)x+sin(phi)y axis.

        Args:
            theta: the angle(in radian) to be rotated.
            phi: the angle(in radian) to compute the axis of rotation.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.r_gate: [qubit], constants.PARAMS: [theta, phi]})
        return self

    def p_gate(self, theta, qubit):
        """
        Produces a single qubit rotation around the Z-axis, for a specific angle taken as input.
        The Z gate, S gate and T gate are specific instances of the P gate.

        Args:
            theta: the angle(in radian) to be rotated.
            qubit: index of qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.p_gate: [qubit], constants.PARAMS: [theta]})
        return self

    def c3x_gate(self, control_qubit1, control_qubit2, control_qubit3, target_qubit):
        """
        Also known as the Toffoli gate.
        Uses 3 control qubits to decide the application of the X gate to the target qubit.
        If all the control qubits are in the |1> state, the X gate is performed
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.

        Args:
            control_qubit1: index of control qubit 1, to which the gate is to be applied.
            control_qubit2: index of control qubit 2, to which the gate is to be applied.
            control_qubit3: index of control qubit 3, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(control_qubit3)
        self.check_qubit_boundary(target_qubit)
        self.operations.append(
            {OpType.c3x_gate: [[control_qubit1], [control_qubit2], [control_qubit3], [target_qubit]]})
        return self

    def c3sx_gate(self, control_qubit1, control_qubit2, control_qubit3, target_qubit):
        """
        Uses 3 control qubits to decide the application of the SX gate to the target qubit.
        If all the control qubits are in the |1> state, the SX gate is performed
        on the target qubit. Otherwise, the the SX gate is not performed on the target qubit.

        Args:
            control_qubit1: index of control qubit 1, to which the gate is to be applied.
            control_qubit2: index of control qubit 2, to which the gate is to be applied.
            control_qubit3: index of control qubit 3, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(control_qubit3)
        self.check_qubit_boundary(target_qubit)
        self.operations.append(
            {OpType.c3sx_gate: [[control_qubit1], [control_qubit2], [control_qubit3], [target_qubit]]})
        return self

    def c4x_gate(self, control_qubit1, control_qubit2, control_qubit3, control_qubit4, target_qubit):
        """
        Also known as the Toffoli gate.
        Uses 4 control qubits to decide the application of the X gate to the target qubit.
        If all the control qubits are in the |1> state, the X gate is performed
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.

        Args:
            control_qubit1: index of control qubit 1, to which the gate is to be applied.
            control_qubit2: index of control qubit 2, to which the gate is to be applied.
            control_qubit3: index of control qubit 3, to which the gate is to be applied.
            control_qubit4: index of control qubit 4, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(control_qubit3)
        self.check_qubit_boundary(control_qubit4)
        self.check_qubit_boundary(target_qubit)
        self.operations.append(
            {OpType.c4x_gate: [[control_qubit1], [control_qubit2], [control_qubit3], [control_qubit4], [target_qubit]]})
        return self

    def dcx_gate(self, control_qubit1, control_qubit2):
        """
        Produces a set of double CX gate with back to back controls.
        The first CX is applied on the second qubit with first qubit as control.
        The second CX is applied on the first qubit with second qubit as control.

        Args:
            control_qubit1: index of control qubit 1, to which the gate is to be applied.
            control_qubit2: index of control qubit 2, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.operations.append({OpType.dcx_gate: [[control_qubit1], [control_qubit2]]})
        return self

    def ch_gate(self, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the H gate to the target qubit.
        If the control qubit is in the |0> state, the H gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the H gate is performed on the target qubit.

        Args:
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.ch_gate: [[control_qubit], [target_qubit]]})
        return self

    def csx_gate(self, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the SX gate to the target qubit.
        If the control qubit is in the |0> state, the SX gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the SX gate is performed on the target qubit.

        Args:
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.csx_gate: [[control_qubit], [target_qubit]]})
        return self

    def cswap_gate(self, control_qubit, target_qubit1, target_qubit2):
        """
        Uses a control qubit to decide the application of the Swap gate to the target qubit.
        If the control qubit is in the |0> state, the Swap gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the Swap gate is performed on the target qubit.

        Args:
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit1: index of target qubit, to which the gate is to be applied.
            target_qubit2: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit1)
        self.check_qubit_boundary(target_qubit2)
        self.operations.append({OpType.cswap_gate: [[control_qubit], [target_qubit1], [target_qubit2]]})
        return self

    def cphase_gate(self, theta, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the Phase gate to the target qubit.
        If the control qubit is in the |0> state, the Phase gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the Phase gate is performed on the target qubit.

        Args:
            theta: the angle(in radian) to be rotated.
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cphase_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def crx_gate(self, theta, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the RX gate to the target qubit.
        If the control qubit is in the |0> state, the RX gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the RX gate is performed on the target qubit.

        Args:
            theta: the angle(in radian) to be rotated.
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.crx_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def cry_gate(self, theta, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the RY gate to the target qubit.
        If the control qubit is in the |0> state, the RY gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the RY gate is performed on the target qubit.

        Args:
            theta: the angle(in radian) to be rotated. 
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cry_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def crz_gate(self, theta, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the RZ gate to the target qubit.
        If the control qubit is in the |0> state, the RZ gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the RZ gate is performed on the target qubit.

        Args:
            theta: the angle(in radian) to be rotated.
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.crz_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def cu_gate(self, theta, phi, lam, gamma, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the U gate to the target qubit.
        If the control qubit is in the |0> state, the U gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the U gate is performed on the target qubit.

        Args:
            theta: the angle(in radian) to be rotated.
            phi: the angle(in radian) to be rotated.
            lam: the angle(in radian) to be rotated.
            gamma: the angle(in radian) to be rotated.
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cu_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta, phi, lam, gamma]})
        return self

    def cu1_gate(self, theta, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the U1 gate to the target qubit.
        If the control qubit is in the |0> state, the U1 gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the U1 gate is performed on the target qubit.

        Args:
            theta: the angle(in radian) to be rotated.
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cu1_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def cu3_gate(self, theta, phi, lam, control_qubit, target_qubit):
        """
        Uses a control qubit to decide the application of the U3 gate to the target qubit.
        If the control qubit is in the |0> state, the U3 gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the U3 gate is performed on the target qubit.

        Args:
            theta: the angle(in radian) to be rotated.
            phi: the angle(in radian) to be rotated.
            lam: the angle(in radian) to be rotated.
            control_qubit: index of control qubit, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cu3_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta, phi, lam]})
        return self

    def mcx_gate(self, control_qubits, target_qubit, ancilla_qubits=[], mode='nonancilla'):
        """
        Uses multiple control qubits to decide the application of the X gate to the target qubit.
        If all the control qubits are in the |1> state, the X gate is performed
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.

        Args:
            control_qubits: list of control qubit indices, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.
            ancilla_qubits: list of ancilla qubits.
            mode: current mode of gate, concerning ancilla qubits.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append({OpType.mcx_gate: control_qubits[:] + [target_qubit] + ancilla_qubits[:],
                                constants.PARAMS: [len(control_qubits)]})
        return self

    def mcxgc_gate(self, control_qubits, target_qubit):
        """
        Implements the multi-control X gate using Gray Code
        If all the control qubits are in the |1> state, the X gate is performed using Gray code,
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.

        Args:
            control_qubits: list of control qubit indices, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append(
            {OpType.mcxgc_gate: control_qubits[:] + [target_qubit], constants.PARAMS: [len(control_qubits)]})
        return self

    def mcxvchain_gate(self, control_qubits, target_qubit, dirty_ancilla):
        """
        Implements the multi-control X gate using V-chain of CX gates
        If all the control qubits are in the |1> state, the X gate is performed using V chain of CX gates,
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.

        Args:
            control_qubits: list of control qubit indices, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.
            dirty_ancilla: list of dirty ancilla qubits.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append({OpType.mcxvchain_gate: control_qubits[:] + [target_qubit],
                                constants.PARAMS: [len(control_qubits), dirty_ancilla]})
        return self

    def mcxrec_gate(self, control_qubits, target_qubit):
        """
        Implements the multi-control X gate using recursion.
        If all the control qubits are in the |1> state, the X gate is performed using recursion,
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.

        Args:
            control_qubits: list of control qubit indices, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append(
            {OpType.mcxrec_gate: control_qubits[:] + [target_qubit], constants.PARAMS: [len(control_qubits)]})
        return self

    def mcp_gate(self, lam, control_qubits, target_qubit):
        """
        Uses multiple control qubits to decide the application of the P gate to the target qubit.
        If all the control qubits are in the |1> state, the P gate is performed
        on the target qubit. Otherwise, the the P gate is not performed on the target qubit.

        Args:
            lam: the angle(in radian) to be rotated.
            control_qubits: list of control qubit indices, to which the gate is to be applied.
            target_qubit: index of target qubit, to which the gate is to be applied.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append(
            {OpType.mcp_gate: control_qubits[:] + [target_qubit], constants.PARAMS: [lam, len(control_qubits)]})
        return self

    def mct_gate(self, control_qubits, target_qubits, ancilla_qubits=None, mode='noancilla'):
        """
        Uses multiple control qubits to decide the application of the X gate to multiple target qubits.
        If all the control qubits are in the |1> state, the X gate is performed
        on the target qubits. Otherwise, the the X gate is not performed on the target qubits.

        Args:
            control_qubits: list of control qubit indices, to which the gate is to be applied.
            target_qubits: list of target qubit indices, to which the gate is to be applied.
            ancilla_qubits: list of ancilla qubits.
            mode: current mode of gate, concerning ancilla qubits.

        Returns:
            self: modified state of the qubit to the circuit.

        Raises:
            CircuitError: if qubit index is not within range.
        """
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        for qubit in target_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append({OpType.mct_gate: [control_qubits, [target_qubits], ancilla_qubits, mode]})
        return self

    def measure(self, qubit):
        """
        Executes the act of measuring the state of a qubit to a classical bit. The readouts
        from the classical bits are used to study the results generated by the quantum device.

        Args:
            qubit: index of qubit, to be measured.

        Raises:
            CircuitError: if qubit index is not within range.

        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.measure: [qubit]})

    def measure_all(self):
        """
        Measures the state of all the qubits used in the circuit, to classical bits.
        The qubits are measured to the same corresponding index of classical bits.
        The function does not take in any arguments.
        """
        self.operations.append({OpType.measure_all: OpType.measure_all})

    def get_operations(self):
        return self.operations

    def check_qubit_boundary(self, qubit):
        """
        Checks if the index of the qubits entered in gate are permissible within the limits of the number of qubits declared.
        
        Args:
            qubit: index of qubit to be checked.
        """
        if qubit > (self.qubits - 1):
            raise CircuitError(ErrorMessages.qubit_out_of_bound)

    def draw_circuit(self, provider=providers.DEFAULT_PROVIDER):
        """
        Generates the circuit diagram of the circuit that has been built.

        Args:
            provider: the name of backend provider as string input.
        """
        self.check_and_convert(provider)

        if self.provider == providers.IBM_PROVIDER:
            print(self.converted_q_circuit.draw())
        elif self.provider == providers.GOOGLE_PROVIDER:
            print(self.converted_q_circuit)
        elif self.provider == providers.MICROSOFT_PROVIDER:
            pass
        elif self.provider == providers.AMAZON_PROVIDER:
            print(self.converted_q_circuit)

    def convert_circuit(self):
        """
        Converts the circuit to the required backend, as requested by the user.
        """
        converted_q_circuit = None
        if self.provider == providers.IBM_PROVIDER:
            converted_q_circuit = convert.to_qiskit(self, self.qubits)
        elif self.provider == providers.GOOGLE_PROVIDER:
            converted_q_circuit = convert.to_cirq(self, self.qubits)
        elif self.provider == providers.IONQ_PROVIDER:
            converted_q_circuit = convert.to_cirq(self, self.qubits)
        elif self.provider == providers.MICROSOFT_PROVIDER:
            converted_q_circuit = convert.to_q_sharp(self, self.qubits)
        elif self.provider == providers.AMAZON_PROVIDER:
            converted_q_circuit = convert.to_braket(self, self.qubits)
        return converted_q_circuit

    def execute(self, provider=providers.DEFAULT_PROVIDER,
                simulator_name=constants.DEFAULT_SIMULATOR,
                repetitions=1000, api=None, device=None,
                default_target='simulator'):
        """
        Executes the circuit using the backend which is given as an input by the user.

        Args:
            provider: the name of backend provider as string input.
            simulator_name: the name of simulator as string input.
            repetitions: the number of times the circuit is to be executed.
            api: the API token for the backend device as string input.
            device: the device name, where the circuit is to be executed, as string input.
            default_target: set as simulator.


        Returns:
            Results after execution.
        """
        self.check_and_convert(provider)
        if self.provider == providers.IBM_PROVIDER:
            return execute_circuit.on_qiskit(self.converted_q_circuit,
                                             simulator_name, repetitions,
                                             api, device)
        elif self.provider == providers.GOOGLE_PROVIDER:
            return execute_circuit.on_cirq(self.converted_q_circuit,
                                           simulator_name, repetitions, api, self.get_operations())
        elif self.provider == providers.AMAZON_PROVIDER:
            return execute_circuit.on_braket(self.converted_q_circuit,
                                             simulator_name, repetitions, api)
        elif self.provider == providers.IONQ_PROVIDER:
            if api is None:
                raise APIDetailsNotFoundError(ErrorMessages.ionq_api_details_not_provided)
            return execute_circuit.on_ionq(self.converted_q_circuit,
                                           default_target, repetitions, api, self.get_operations())

    def check_and_convert(self, provider):
        """
        Checks the circuit inputs and proceed to convert the circuit to required backend.

        Args:
            provider: the name of backend provider as string input.
        """
        if self.converted_q_circuit is None or self.provider != provider:
            self.provider = provider
            converted_q_circuit = self.convert_circuit()
            self.converted_q_circuit = converted_q_circuit

    def superposition(self, qubit):
        """
        Produces a superposition of the |0> and |1> on the qubit.

        Args:
            qubit: the index of the qubit to be superposed.
        """
        self.h_gate(qubit)

    def entangle(self, qubit1, qubit2):
        """
        Produces an entangled state of the |00> and |11> on the qubit.

        Args:
            qubit1: the index of the qubit 1 to be entangled.
            qubit2: the index of the qubit 2 to be entangled.
        """
        self.superposition(qubit1)
        self.cx_gate(qubit1, qubit2)

    def phase_kickback(self, qubit):
        """
        Produces a phase kickback on the qubit.

        Args:
            qubit: the index of the qubit, in which the phase kickback is performed.
        """
        self.x_gate(qubit)
        self.h_gate(qubit)
