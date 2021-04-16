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
from quantumcat.utils import providers


class GroversAlgorithm:
    """docstring for Circuit."""

    def __init__(self, q_circuit, num_of_qubits, oracle=None):
        super(GroversAlgorithm, self).__init__()
        self.oracle = oracle
        self.q_circuit = q_circuit
        self.num_of_qubits = num_of_qubits

    def initialize(self):
        for qubit in range(self.num_of_qubits):
            self.q_circuit.h_gate(qubit)

    def diffuser(self):
        q_circuit = self.q_circuit
        qubits = self.num_of_qubits

        for qubit in range(qubits):
            q_circuit.h_gate(qubit)

        for qubit in range(qubits):
            q_circuit.x_gate(qubit)

        q_circuit.h_gate(qubits-1)
        q_circuit.mct_gate(list(range(qubits-1)), qubits-1)  # multi-controlled-toffoli
        q_circuit.h_gate(qubits-1)

        for qubit in range(qubits):
            q_circuit.x_gate(qubit)

        for qubit in range(qubits):
            q_circuit.h_gate(qubit)

        return q_circuit

    def execute(self, provider=providers.DEFAULT_PROVIDER, num_of_iterations=None):
        pass
