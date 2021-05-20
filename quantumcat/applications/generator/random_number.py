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


from quantumcat.circuit import QCircuit
from quantumcat.utils import providers, constants, helper


class RandomNumber:

    def __init__(self, length, output_type=constants.BINARY):
        super(RandomNumber, self).__init__()
        self.length = length
        self.output_type = output_type
        self.provider = providers.DEFAULT_PROVIDER
        self.circuit = None

    def execute(self, provider=providers.DEFAULT_PROVIDER,
                simulator_name=constants.DEFAULT_SIMULATOR, api=None, device=None):
        num_qubits = self.length
        circuit = QCircuit(num_qubits)
        self.circuit = circuit
        self.provider = provider

        for i in range(num_qubits):
            circuit.h_gate(i)

        circuit.measure_all()

        counts = circuit.execute(provider=provider, repetitions=1,
                                 simulator_name=simulator_name, api=api, device=device)

        random_number = next(iter(counts.keys()))

        if self.output_type == constants.DECIMAL:
            random_number = helper.binary_to_decimal(random_number)

        return random_number

    def draw_random_number_circuit(self):
        return self.circuit.draw_circuit(provider=self.provider)


