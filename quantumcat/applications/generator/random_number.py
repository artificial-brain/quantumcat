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
import math
import numpy as np

# Todo: Correct the code when range difference is 1. For e.g: range(7,8)


class RandomNumber:

    def __init__(self, length=0, range=None, output_type=constants.BINARY):
        super(RandomNumber, self).__init__()
        self.length = length
        self.range = range
        self.num_qubits = self.length if range is None else self.get_num_bits()
        self.output_type = output_type
        self.provider = providers.DEFAULT_PROVIDER
        self.qc = None
        self.initialize()

    def initialize(self):
        if self.range is not None:
            self.range_circuit()
        else:
            self.length_circuit()

    def length_circuit(self):
        num_qubits = self.num_qubits
        qc = QCircuit(num_qubits)
        self.qc = qc
        for i in range(num_qubits):
            qc.h_gate(i)

        qc.measure_all()

    def get_binary_output(self, num_qubits, decimal_output):
        outputs_binary = []
        output = np.array(decimal_output)
        for n in range(num_qubits - 1, -1, -1):
            func = lambda x: self.nth_bit(x, n)
            outputs_binary.append(func(output))
        outputs_binary = np.asarray(outputs_binary, dtype='int8')
        return outputs_binary

    def range_circuit(self):
        lower_limit, upper_limit = self.range[0], self.range[1]
        num_qubits = self.num_qubits
        output = self.make_output(lower_limit, upper_limit, num_qubits)
        final_op = self.get_binary_output(num_qubits, output)
        sop = self.get_sop(final_op, num_qubits)

        qc = QCircuit(num_qubits * 3)
        self.qc = qc

        for i in range(num_qubits):
            qc.h_gate(i)

        for i in range(num_qubits):
            qc.cx_gate(i, i + (num_qubits * 2))
            qc.x_gate(i + (num_qubits * 2))
        cnt = 0

        for o in sop:
            for i in range(len(o)):
                lst = []
                if o[i] != 0:
                    for j in range(num_qubits):
                        if self.nth_bit(o[i] - 1, j) == 1:
                            lst.append(j)
                        else:
                            lst.append(j + (num_qubits * 2))
                    qc.mct_gate(lst, cnt + num_qubits)
            cnt += 1

        for i in range(num_qubits):
            qc.measure(num_qubits + i)

        return qc

    def get_num_bits(self):
        upper_limit = self.range[1]
        return math.floor(math.log(upper_limit, 2)) + 1

    @staticmethod
    def nth_bit(num, n):
        return num & (1 << n) != 0

    @staticmethod
    def make_output(lower_limit, upper_limit, num_qubits):
        num_vals = upper_limit - lower_limit + 1
        output = []
        rep = (2 ** num_qubits) // num_vals
        for i in range(lower_limit, upper_limit + 1):
            output += ([i] * rep)
        if (2 ** num_qubits) % num_vals != 0:
            for i in range(0, (2 ** num_qubits) % num_vals):
                output += [lower_limit]
                lower_limit += 1
        return output

    @staticmethod
    def get_sop(binary_output, num_qubits):
        inp = np.arange(1, ((2 ** num_qubits) + 1), 1, dtype='int32')
        sop = []
        for i in range(num_qubits):
            sop.append(inp * binary_output[i])
        return sop

    def execute(self, provider=providers.DEFAULT_PROVIDER,
                simulator_name=constants.DEFAULT_SIMULATOR, api=None, device=None):

        counts = self.qc.execute(provider=provider, repetitions=1,
                                 simulator_name=simulator_name, api=api, device=device)

        # Find a better way to remove this:
        random_number = list(counts.keys())[0][::-1] if self.range is not None \
            else next(iter(counts.keys()))

        # Find a better way to remove this:
        if provider == providers.IBM_PROVIDER and self.range is not None:
            random_number = random_number[:-self.num_qubits]

        if self.output_type == constants.DECIMAL:
            random_number = helper.binary_to_decimal(random_number)
        return random_number

    def draw_random_number_circuit(self, provider=providers.DEFAULT_PROVIDER):
        return self.qc.draw_circuit(provider=provider)


