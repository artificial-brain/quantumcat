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
from quantumcat.exceptions import CircuitError
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
        This function is aimed at initializing the QCircuit class and enable the smooth running of all the included
        operations.
        """
        super(QCircuit, self).__init__()
        self.qubits = qubits
        self.operations = []
        self.converted_q_circuit = None
        self.provider = provider

    def x_gate(self, qubit):
        """
        The X gate, which produces a bit flip for thw two state in the computational basis.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.x_gate: [qubit]})
        return self

    def y_gate(self, qubit):
        """
        The Y gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.y_gate: [qubit]})
        return self

    def z_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.z_gate: [qubit]})
        return self

    def h_gate(self, qubit):
        """
        The Hadamard gate, which transforms the states in the computational basis into a state of superposition.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.h_gate: [qubit]})
        return self

    def cx_gate(self, control_qubit, target_qubit):
        """
        The controlled-X gate. This operator employs a control qubit to decide the application of the X gate to the target qubit.
        If the control qubit is in the |0> state, the X gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the X gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cx_gate: [[control_qubit], [target_qubit]]})
        return self

    def cz_gate(self, control_qubit, target_qubit):
        """
        The controlled-Z gate. This operator employs a control qubit to decide the application of the Z gate to the target qubit.
        If the control qubit is in the |0> state, the Z gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the Z gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.operations.append({OpType.cz_gate: [[control_qubit], [target_qubit]]})
        return self

    def ccx_gate(self, control_qubit1, control_qubit2, target_qubit):
        """
        The  3 qubit controlled-X gate, also known as the Toffoli gate. This operator employs 2 control qubits to decide
        the application of the X gate to the target qubit. If both the control qubits are in the |1> state, the X gate is performed
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.ccx_gate: [[control_qubit1], [control_qubit2], [target_qubit]]})
        return self

    def ry_gate(self, theta, qubit):
        """
        The Ry gate produces a single qubit rotation around the Y-axis, for a specific angle which is entered as
        the first parameter, followed by the intended qubit. 
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.ry_gate: [qubit],
                                constants.PARAMS: [theta]})
        return self

    def ryy_gate(self, theta, qubit1, qubit2):
        """
        The Ryy gate which is a parametric two-qubit gate
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append({OpType.ryy_gate: [[qubit1], [qubit2]],
                                constants.PARAMS: [theta]})
        return self

    def rzz_gate(self, theta, qubit1, qubit2):
        """
        The Rzz gate which is a parametric two-qubit gate
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append({OpType.rzz_gate: [[qubit1], [qubit2]],
                                constants.PARAMS: [theta]})
        return self

    def rzx_gate(self, theta, qubit1, qubit2):
        """
        The Rzx gate which is a parametric two-qubit gate
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append({OpType.rzx_gate: [[qubit1], [qubit2]],
                                constants.PARAMS: [theta]})
        return self

    def rz_gate(self, phi, qubit):
        """
        The Rz gate produces a single qubit rotation around the Z-axis, for a specific angle which is entered as
        the first parameter, followed by the intended qubit. 
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
        The S gate, produces a rotation of pi/2 around the Z axis. It is a Clifford gate and is known as root of Z gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.s_gate: [qubit]})
        return self

    def sdg_gate(self, qubit):
        """
        The S gate, produces a rotation of -pi/2 around the Z axis. It is a Clifford gate and is known as root of Z gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sdg_gate: [qubit]})
        return self

    def swap_gate(self, qubit1, qubit2):
        """
        The Swap gate produces a interchange in the states of the target qubits.
        It is symmetric and a Clifford gate.
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append(({OpType.swap_gate: [[qubit1], [qubit2]]}))
        return self

    def iswap_gate(self, qubit_a, qubit_b):
        """
        The iSwap gate produces a interchange in the states of the target qubits and also adds a phase of i,
        to the amplitudes of |01> and |10>.
        It is symmetric and a Clifford gate.
        """
        self.check_qubit_boundary(qubit_a)
        self.check_qubit_boundary(qubit_b)
        self.operations.append(({OpType.iswap_gate: [[qubit_a], [qubit_b]]}))
        return self

    def sx_gate(self, qubit):
        """
        The Sx gate, produces a rotation of pi/2 around the X axis. It is a Clifford gate and is known as root of X gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sx_gate: [qubit]})
        return self

    def sxd_gate(self, qubit):
        """
        The Sx gate, produces a rotation of -pi/2 around the X axis. It is a Clifford gate and is known as root of X gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sxd_gate: [qubit]})
        return self

    def t_gate(self, qubit):
        """
        The T gate, produces a rotation of pi/4 around the Z axis. It is a Clifford gate and is known as 4th root of Z gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.t_gate: [qubit]})
        return self

    def td_gate(self, qubit):
        """
        The Td gate, produces a rotation of -pi/4 around the Z axis. It is a Clifford gate and is known as 4th root of Z gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.td_gate: [qubit]})
        return self

    def u_gate(self, theta, phi, lam, qubit):
        """
        The U Gate, induces a single qubit rotation with 3 Euler angles. This is the most generic form of single
        wubit rotation operators and all the other rotation operators are specific instances of the U gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.u_gate: [qubit],
                                constants.PARAMS: [theta, phi, lam]})
        return self

    def u1_gate(self, theta, qubit):
        """
        The U1 gate, is a special case of the U gate, with theta = phi = 0. The U1 gate is equaivalent to the RZ gate.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.u1_gate: [qubit],
                                constants.PARAMS: [theta]})
        return self

    def u2_gate(self, phi, lam, qubit):
        """
        The U2 gate, is a special case of the U gate, with theta = pi/2.
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
        """
        self.check_qubit_boundary(qubit)
        self.operations.append(({OpType.u3_gate: [qubit],
                                 constants.PARAMS: [theta, phi, lam]}))
        return self

    def cy_gate(self, control_qubit, target_qubit):
        """
        The controlled-Y gate. This operator employs a control qubit to decide the application of the Y gate to the target qubit.
        If the control qubit is in the |0> state, the Y gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the Y gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.operations.append({OpType.cy_gate: [[control_qubit], [target_qubit]]})
        return self

    def i_gate(self, qubit):
        """
        The I gate is an identity gate. It does not produce any changes on the qubit and it basically does nothing.
        It's matrix is the identity matrix. This gate is primarily nominal and is not generallu used in computation.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.i_gate: [qubit]})
        return self

    def rccx_gate(self, control_qubit1, control_qubit2, target_qubit):
        """
        The RCCX gate is the simplified 2 control X gate, where in the Toffoli gate is implemented up to relative phases.
        Note, that the simplified Toffoli is not equivalent to the Toffoli.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.rccx_gate: [[control_qubit1], [control_qubit2], [target_qubit]]})
        return self

    def rc3x_gate(self, control_qubit1, control_qubit2, control_qubit3, target_qubit):
        """
        The RC3X gate is the simplified 3 control X gate, where in the C3X gate is implemented up to relative phases.
        Note, that the simplified C3X gate is not equivalent to the C3X gate.
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
        The Rxx gate which is a parametric two-qubit gate
        """
        self.check_qubit_boundary(qubit1)
        self.check_qubit_boundary(qubit2)
        self.operations.append({OpType.rxx_gate: [[qubit1], [qubit2]], constants.PARAMS: [theta]})
        return self

    def rx_gate(self, theta, qubit):
        """
        The Rx gate produces a single qubit rotation around the X-axis, for a specific angle which is entered as
        the first parameter, followed by the intended qubit. 
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.rx_gate: [qubit], constants.PARAMS: [theta]})
        return self

    def r_gate(self, theta, phi, qubit):
        """
        The R gate produces a rotation of theta, around the cos(phi)x+sin(phi)y axis. The angle theta is entered
        as the first parameter and angle phi is entered as the second parameter.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.r_gate: [qubit], constants.PARAMS: [theta, phi]})
        return self

    def p_gate(self, theta, qubit):
        """
        The Phase gate. This gate produces a single qubit rotation around the Z-axis.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.p_gate: [qubit], constants.PARAMS: [theta]})
        return self

    def c3x_gate(self, control_qubit1, control_qubit2, control_qubit3, target_qubit):
        """ 
        The  3 qubit controlled-X gate, also known as the Toffoli gate. This operator employs 3 control qubits to decide
        the application of the X gate to the target qubit.If all the control qubits are in the |1> state, the X gate is performed
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.
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
        The  3 qubit controlled-SX gate. This operator employs 3 control qubits to decide
        the application of an SX gate to the target qubit. If all the control qubits are in the |1> state, the SX gate is performed
        on the target qubit. Otherwise, the the SX gate is not performed on the target qubit.
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
        The  4 qubit controlled-SX gate. This operator employs 4 control qubits to decide
        the application of an X gate to the target qubit. If all the control qubits are in the |1> state, the X gate is performed
        on the target qubit. Otherwise, the the X gate is not performed on the target qubit.
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
        The Double CX gate. A 2-qubit Clifford gate consisting of two back-to-back CXs with alternate controls.
        """
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.operations.append({OpType.dcx_gate: [[control_qubit1], [control_qubit2]]})
        return self

    def ch_gate(self, control_qubit, target_qubit):
        """
        The controlled-H gate. This operator employs a control qubit to decide the application of the H gate to the target qubit.
        If the control qubit is in the |0> state, the H gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the H gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.ch_gate: [[control_qubit], [target_qubit]]})
        return self

    def csx_gate(self, control_qubit, target_qubit):
        """
        The controlled-SX gate. This operator employs a control qubit to decide the application of the SX gate to the target qubit.
        If the control qubit is in the |0> state, the SX gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the SX gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.csx_gate: [[control_qubit], [target_qubit]]})
        return self

    def cswap_gate(self, control_qubit, target_qubit1, target_qubit2):
        """
        The controlled-Swap gate. This operator employs a control qubit to decide the application of the Swap gate to the target qubit.
        If the control qubit is in the |0> state, the Swap gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the Swap gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit1)
        self.check_qubit_boundary(target_qubit2)
        self.operations.append({OpType.cswap_gate: [[control_qubit], [target_qubit1], [target_qubit2]]})
        return self

    def cphase_gate(self, theta, control_qubit, target_qubit):
        """
        The controlled-Phase gate. This operator employs a control qubit to decide the application of the Phase gate to the target qubit.
        If the control qubit is in the |0> state, the Phase gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the Phase gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cphase_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def crx_gate(self, theta, control_qubit, target_qubit):
        """
        The controlled-RX gate. This operator employs a control qubit to decide the application of the RX gate to the target qubit.
        If the control qubit is in the |0> state, the RX gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the RX gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.crx_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def cry_gate(self, theta, control_qubit, target_qubit):
        """
        The controlled-RY gate. This operator employs a control qubit to decide the application of the RY gate to the target qubit.
        If the control qubit is in the |0> state, the RY gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the RY gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cry_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def crz_gate(self, theta, control_qubit, target_qubit):
        """
        The controlled-RZ gate. This operator employs a control qubit to decide the application of the RZ gate to the target qubit.
        If the control qubit is in the |0> state, the RZ gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the RZ gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.crz_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def cu_gate(self, theta, phi, lam, gamma, control_qubit, target_qubit):
        """
        The controlled-U gate. This operator employs a control qubit to decide the application of the U gate to the target qubit.
        If the control qubit is in the |0> state, the U gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the U gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cu_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta, phi, lam, gamma]})
        return self

    def cu1_gate(self, theta, control_qubit, target_qubit):
        """
        The controlled-U1 gate. This operator employs a control qubit to decide the application of the U1 gate to the target qubit.
        If the control qubit is in the |0> state, the U1ate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the U1gate is performed on the target qubit.
        """
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cu1_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta]})
        return self

    def cu3_gate(self, theta, phi, lam, control_qubit, target_qubit):
        """
        The controlled-U3 gate. This operator employs a control qubit to decide the application of the U3 gate to the target qubit.
        If the control qubit is in the |0> state, the U3 gate is not performed on the target qubit. If the control qubit is
        in the |1> state, then the U3 gate is performed on the target qubit.
        """        
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cu3_gate: [[control_qubit], [target_qubit]],
                                constants.PARAMS: [theta, phi, lam]})
        return self

    def mcx_gate(self, control_qubits, target_qubit, ancilla_qubits=[], mode='nonancilla'):
        """
        The multi-control X gate. This operator performs the same functions as the CX gate, but it can accomodate multiple control qubits.
        The list of control qubits are entered as the first parameter and the target qubit is entered as the second parameter.
        This gate performs an X gate on the target qubit considering the state of the
        multiple control qubits.
        """
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append({OpType.mcx_gate: control_qubits[:] + [target_qubit] + ancilla_qubits[:],
                                constants.PARAMS: [len(control_qubits)]})
        return self

    def mcxgc_gate(self, control_qubits, target_qubit):
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append(
            {OpType.mcxgc_gate: control_qubits[:] + [target_qubit], constants.PARAMS: [len(control_qubits)]})
        return self

    def mcxvchain_gate(self, control_qubits, target_qubit, dirty_ancilla):
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append({OpType.mcxvchain_gate: control_qubits[:] + [target_qubit],
                                constants.PARAMS: [len(control_qubits), dirty_ancilla]})
        return self

    def mcxrec_gate(self, control_qubits, target_qubit):
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append(
            {OpType.mcxrec_gate: control_qubits[:] + [target_qubit], constants.PARAMS: [len(control_qubits)]})
        return self

    def mcp_gate(self, lam, control_qubits, target_qubit):
        self.check_qubit_boundary(target_qubit)
        for qubit in control_qubits:
            self.check_qubit_boundary(qubit)
        self.operations.append(
            {OpType.mcp_gate: control_qubits[:] + [target_qubit], constants.PARAMS: [lam, len(control_qubits)]})
        return self

    def mct_gate(self, control_qubits, target_qubit, ancilla_qubits=None, mode='noancilla'):
        """
        The multi-control X gate. This operator performs the same functions as the CX gate, but it can accomodate multiple control qubits.
        The list of control qubits are entered as the first parameter and the target qubit is entered as the second parameter.
        This gate performs an X gate on the target qubit considering the state of the
        multiple control qubits.
        """
        # self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.mct_gate: [control_qubits, [target_qubit], ancilla_qubits, mode]})
        return self

    def measure(self, qubit):
        """ 
        The measure function executes the act of measuring the state of the qubits to a classical bit. The readouts
        from the classical bits are used to stude the results generated by the quantum device.
        The function takes in the qubit to be measured as the first parameter and the classical bit as the second parameter.
        """
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.measure: [qubit]})

    def measure_all(self):
        """
        Measures the state of all the qubits, used in the program, to classical bits.
        The function does not take in any parameters.
        """
        self.operations.append({OpType.measure_all: OpType.measure_all})

    def get_operations(self):
        return self.operations

    def check_qubit_boundary(self, qubit):
        if qubit > (self.qubits - 1):
            raise CircuitError(ErrorMessages.qubit_out_of_bound)

    def draw_circuit(self, provider=providers.DEFAULT_PROVIDER):
        self.check_and_convert(provider)

        if self.provider == providers.IBM_PROVIDER:
            print(self.converted_q_circuit.draw())
        elif self.provider == providers.GOOGLE_PROVIDER:
            print(self.converted_q_circuit)
        elif self.provider == providers.MICROSOFT_PROVIDER:
            pass

    def convert_circuit(self):
        converted_q_circuit = None
        if self.provider == providers.IBM_PROVIDER:
            converted_q_circuit = convert.to_qiskit(self, self.qubits)
        elif self.provider == providers.GOOGLE_PROVIDER:
            converted_q_circuit = convert.to_cirq(self, self.qubits)
        if self.provider == providers.MICROSOFT_PROVIDER:
            converted_q_circuit = convert.to_q_sharp(self, self.qubits)
        return converted_q_circuit

    def execute(self, provider=providers.DEFAULT_PROVIDER,
                simulator_name=constants.DEFAULT_SIMULATOR,
                repetitions=1000, api=None, device=None):
        self.check_and_convert(provider)
        if self.provider == providers.IBM_PROVIDER:
            return execute_circuit.on_qiskit(self.converted_q_circuit,
                                             simulator_name, repetitions,
                                             api, device)
        elif self.provider == providers.GOOGLE_PROVIDER:
            return execute_circuit.on_cirq(self.converted_q_circuit,
                                           simulator_name, repetitions, api, self.get_operations())

    def check_and_convert(self, provider):
        if self.converted_q_circuit is None or self.provider != provider:
            self.provider = provider
            converted_q_circuit = self.convert_circuit()
            self.converted_q_circuit = converted_q_circuit

    def superposition(self, qubit):
        """
        The Superposition function places a qubit into a superposed state of |0> and |1>
        """

        self.h_gate(qubit)

    def entangle(self, qubit1, qubit2):
        """
        The Entangle function places two qubits into an entangled states.
        """
        self.superposition(qubit1)
        self.cx_gate(qubit1, qubit2)

    def phase_kickback(self, qubit):
        self.x_gate(qubit)
        self.h_gate(qubit)
