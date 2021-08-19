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


from quantumcat.utils import providers, constants
from quantumcat.circuit import QCircuit
import numpy as np


class DeutschJozsa:
    """Class for implementing Deutsch Jozsa algorithm """

    def __init__(self, case, num_qubits):
        super(DeutschJozsa, self).__init__()
        self.case = case
        self.num_qubits = num_qubits
        self.dj_circuit = None

    def draw_algorithm(self, provider=providers.DEFAULT_PROVIDER, filename=None, output='text'):
        dj_circuit = self.dj_algorithm()
        dj_circuit.draw_circuit(provider=provider, filename=filename, output=output)

    def dj_algorithm(self):
        n = self.num_qubits
        dj_circuit = QCircuit(n + 1)
        self.dj_circuit = dj_circuit
        dj_circuit.x_gate(n)
        dj_circuit.h_gate(n)

        # And set up the input register:
        for qubit in range(n):
            dj_circuit.superposition(qubit)

        self.dj_oracle()

        # Finally, perform the H-gates again and measure:
        for qubit in range(n):
            dj_circuit.h_gate(qubit)

        for i in range(n):
            print(i, n)
            dj_circuit.measure(i)

        return dj_circuit

    def execute(self, provider=providers.DEFAULT_PROVIDER, repetitions = constants.DEFAULT_REPETITIONS,
                api=None, device=None):

        dj_circuit = self.dj_algorithm()

        return dj_circuit.execute(provider=provider, repetitions=repetitions,
                                  api=api, device=device)

    def dj_oracle(self):
        oracle_qc = self.dj_circuit
        case = self.case
        n = self.num_qubits
        # We need to make a QuantumCircuit object to return
        # This circuit has n+1 qubits: the size of the input,
        # plus one output qubit

        # First, let's deal with the case in which oracle is balanced
        if case == "balanced":
            # First generate a random number that tells us which CNOTs to
            # wrap in X-gates:
            b = np.random.randint(1, 2 ** n)
            # Next, format 'b' as a binary string of length 'n', padded with zeros:
            b_str = format(b, '0' + str(n) + 'b')
            # Next, we place the first X-gates. Each digit in our binary string
            # corresponds to a qubit, if the digit is 0, we do nothing, if it's 1
            # we apply an X-gate to that qubit:
            for qubit in range(len(b_str)):
                if b_str[qubit] == '1':
                    oracle_qc.x_gate(qubit)
            # Do the controlled-NOT gates for each qubit, using the output qubit
            # as the target:
            for qubit in range(n):
                oracle_qc.cx_gate(qubit, n)
            # Next, place the final X-gates
            for qubit in range(len(b_str)):
                if b_str[qubit] == '1':
                    oracle_qc.x_gate(qubit)

        # Case in which oracle is constant
        if case == "constant":
            # First decide what the fixed output of the oracle will be
            # (either always 0 or always 1)
            output = np.random.randint(2)
            if output == 1:
                oracle_qc.x_gate(n)
