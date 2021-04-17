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
from quantumcat.circuit import QCircuit
import numpy as np


class GroversAlgorithm:
    """docstring for Circuit."""

    def __init__(self, clause_list, solution_known='N', num_of_iterations=None):
        super(GroversAlgorithm, self).__init__()
        self.clause_list = clause_list
        self.solution_known = solution_known
        self.num_of_qubits = len(self.clause_list)
        self.total_qubits = 0
        self.circuit = None
        self.provider = None
        if num_of_iterations is None:
            self.num_of_iterations = self.get_num_of_iterations()

    def initialize(self, provider):
        self.total_qubits = (2 * self.num_of_qubits) + 1
        self.circuit = QCircuit(self.total_qubits,  self.num_of_qubits)
        self.provider = provider

        # Initialise input qubits in superposition
        for qubit in range(self.num_of_qubits):
            self.circuit.h_gate(qubit)

        # Initialise output qubit in the |-⟩ state.
        self.circuit.x_gate(self.total_qubits - 1)
        self.circuit.h_gate(self.total_qubits - 1)

    def create_oracle(self):
        output_qubit = self.total_qubits - 1
        clause_qubits = []

        for index in range(len(self.clause_list)):
            clause_qubit = self.num_of_qubits + index
            self.XOR(self.clause_list[index], clause_qubit)
            clause_qubits.append(clause_qubit)

        # Flip 'output' bit if all clauses are satisfied
        self.circuit.mct_gate(clause_qubits, output_qubit)

        for index in range(len(self.clause_list)):
            clause_qubit = self.num_of_qubits + index
            self.XOR(self.clause_list[index], clause_qubit)

    def XOR(self, qubits, output_qubit):
        for qubit in qubits:
            self.circuit.cx_gate(qubit, output_qubit)

    def diffuser(self):
        q_circuit = self.circuit
        qubits = self.num_of_qubits

        for qubit in range(qubits):
            q_circuit.h_gate(qubit)

        for qubit in range(qubits):
            q_circuit.x_gate(qubit)

        q_circuit.h_gate(qubits-1)
        q_circuit.mct_gate(list(range(qubits-1)), qubits-1)
        q_circuit.h_gate(qubits-1)

        for qubit in range(qubits):
            q_circuit.x_gate(qubit)

        for qubit in range(qubits):
            q_circuit.h_gate(qubit)

    def execute(self, provider=providers.DEFAULT_PROVIDER):
        self.initialize(provider)

        for _ in range(self.num_of_iterations):
            self.create_oracle()
            self.diffuser()

        for i in range(self.num_of_qubits):
            self.circuit.measure(i, i)

        return self.circuit.execute(provider=provider, repetitions=10)

    def draw_grovers_circuit(self):
        return self.circuit.draw_circuit(provider=self.provider)

    def get_num_of_iterations(self):
        return int(0.5*(0.5*np.pi/np.arcsin(1/(np.sqrt(2 ** self.num_of_qubits)))-1))
