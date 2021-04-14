from quantumcat.circuit.op_type import OpType
from quantumcat.exceptions import CircuitError
from quantumcat.utils import ErrorMessages
from quantumcat.circuit import convert
from quantumcat.utils import providers
from quantumcat.utils import constants
from quantumcat.circuit import execute_circuit


class QCircuit:
    """docstring for Circuit."""

    def __init__(self, qubits, cbits, theta=0, phi=0, lam=0, provider=providers.DEFAULT_PROVIDER):
        super(QCircuit, self).__init__()
        self.qubits = qubits
        self.cbits = cbits
        self.theta = theta
        self.phi = phi
        self.lam = lam
        self.operations = []
        self.converted_q_circuit = None
        self.provider = provider

    def x_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.x_gate: [qubit]})

    def y_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.y_gate: [qubit]})

    def z_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.z_gate: [qubit]})

    def cx_gate(self, control_qubit, target_qubit):
        self.check_qubit_boundary(control_qubit)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cx_gate: [[control_qubit], [target_qubit]]})

    def ccx_gate(self, control_qubit1, control_qubit2, target_qubit):
        self.check_qubit_boundary(control_qubit1)
        self.check_qubit_boundary(control_qubit2)
        self.check_qubit_boundary(target_qubit)
        self.operations.append({OpType.cx_gate: [[control_qubit1], [control_qubit2], [target_qubit]]})

    def rzz_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.rzz_gate: [qubit]})

    def rzx_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.rzx_gate: [qubit]})

    # def ecr_gate(self):
    #     pass

    def s_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.s_gate: [qubit]})

    def sdg_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sd_gate: [qubit]})

    def swap_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append(({OpType.swap_gate: [qubit]}))

    def iswap_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append(({OpType.iswap_gate: [qubit]}))

    def sx_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sx_gate: [qubit]})

    def sxd_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.sxd_gate: [qubit]})

    def t_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.t_gate: [qubit]})

    def td_gate(self, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.td_gate: [qubit]})

    def u_gate(self, theta, phi, lam, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.u_gate: [[theta], [phi], [lam], [qubit]]})

    def u1_gate(self, theta, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.u1_gate: [[theta], [qubit]]})

    def u2_gate(self, phi, lam, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append({OpType.u2_gate: [[phi], [lam], [qubit]]})

    def u3_gate(self, theta, phi, lam, qubit):
        self.check_qubit_boundary(qubit)
        self.operations.append(({OpType.u3_gate: [[theta], [phi], [lam], [qubit]]}))

    def measure(self, qubit, cbit):
        self.check_qubit_boundary(qubit)
        self.check_cbit_boundary(cbit)
        self.operations.append({OpType.measure: [[qubit], [cbit]]})

    def get_operations(self):
        return self.operations

    def check_qubit_boundary(self, qubit):
        if qubit > (self.qubits - 1):
            raise CircuitError(ErrorMessages.qubit_out_of_bound)

    def check_cbit_boundary(self, cbit):
        if cbit > (self.cbits - 1):
            raise CircuitError(ErrorMessages.cbit_out_of_bound)

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
            converted_q_circuit = convert.to_qiskit(self, self.qubits, self.cbits)
        elif self.provider == providers.GOOGLE_PROVIDER:
            converted_q_circuit = convert.to_cirq(self, self.qubits, self.cbits)
        if self.provider == providers.MICROSOFT_PROVIDER:
            converted_q_circuit = convert.to_q_sharp(self, self.qubits, self.cbits)
        return converted_q_circuit

    def execute(self, provider=providers.DEFAULT_PROVIDER, backend=constants.SIMULATOR,
                simulator_name=None, repetitions=1000, api=None):
        self.check_and_convert(provider)
        if self.provider == providers.IBM_PROVIDER:
            return execute_circuit.on_qiskit(self.converted_q_circuit, backend,
                                             simulator_name, repetitions, api).get_counts()
        elif self.provider == providers.GOOGLE_PROVIDER:
            return execute_circuit.on_cirq(self.converted_q_circuit, backend,
                                           simulator_name, repetitions, api)

    def check_and_convert(self, provider):
        if self.converted_q_circuit is None or self.provider != provider:
            self.provider = provider
            converted_q_circuit = self.convert_circuit()
            self.converted_q_circuit = converted_q_circuit
