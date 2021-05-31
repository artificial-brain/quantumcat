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
    """ 
    RandomNumber class provides the requisite functions and definitions for creating a true random number generator circuit.
    These numbers are created using intrinsically random quantum physical principles.
    """
    def __init__(self, length, output_type=constants.BINARY):
        """
        Initializes the RandomNumber class and enable the smooth running of all the included
        operations.

        Parameters
        -----------

        <length>: takes in length of random number to be generated.
        <output_type>: takes in the form of representation of the random number.
        """
        super(RandomNumber, self).__init__()
        self.length = length
        self.output_type = output_type
        self.provider = providers.DEFAULT_PROVIDER
        self.circuit = None

    def execute(self, provider=providers.DEFAULT_PROVIDER,
                simulator_name=constants.DEFAULT_SIMULATOR, api=None, device=None):
        """
        Executes the circuit by calling in the provider that executes the algorithm

        Parameters
        -----------

        <provider>: takes in specified provider as a string input
        <simulator_name>: takes in the number of executions of the circuit
        <api>: takes in API token as string input, of the backend to be executed.
        <device>: takes in the name of specific quantum device to be used for execution.

        Returns
        --------

        Random number generated 
        """
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
        """
        Generates circuit diagram of the random number generator algorithm.

        Returns
        ---------
        
        Schematic representation of circuit for the algorithm
        """
        return self.circuit.draw_circuit(provider=self.provider)


