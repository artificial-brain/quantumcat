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


class RandInt:
    def __init__(self, range, output_type=constants.DECIMAL):
        super(RandInt, self).__init__()
        self.upper_limit = range[1]
        self.lower_limit = range[0]
        self.num_qubits = self.get_num_bits()
        self.output_type = output_type
        self.provider = providers.DEFAULT_PROVIDER
        self.unitary_matrix = None
        self.qc = None

    def get_num_bits(self):
        return math.floor(math.log(self.upper_limit, 2)) + 1

    def zero_rows(self):
        lst = []
        lst = list(range(0, self.lower_limit))
        lst.extend(list((range(self.upper_limit + 1, 2 ** self.num_qubits))))
        return lst

    def make_matrix(self, lst):
        H = [[1, 1],
             [1, -1]]
        H2 = H
        for i in range(self.num_qubits - 1):
            H2 = np.kron(H2, H)
        for i in lst:
            H2[i] = np.zeros(1)
        return H2

    @staticmethod
    def gs(self, matrix):
        Q, R = np.linalg.qr(matrix)
        return Q

    def unitary_matrix_gen(self):
        lst = self.zero_rows()
        matrix = self.make_matrix(lst)
        self.unitary_matrix = self.gs(self, matrix)

    def make_circuit(self):
        self.unitary_matrix_gen()
        qubits = list(range(0, self.num_qubits))
        qc = QCircuit(self.num_qubits)
        self.qc = qc
        qc.unitary(self.unitary_matrix, qubits)
        qc.measure_all()

    def execute(self, provider=providers.DEFAULT_PROVIDER,
                simulator_name=constants.DEFAULT_SIMULATOR, api=None, device=None):
        self.make_circuit()
        counts = self.qc.execute(provider=provider, repetitions=1024,
                                 simulator_name=simulator_name, api=api, device=device)

        random_number = list(counts.keys())[0]
        if self.output_type == constants.DECIMAL:
            if provider == providers.GOOGLE_PROVIDER:
                random_number = random_number[::-1]
            random_number = helper.binary_to_decimal(random_number)
        return random_number

    def draw_random_number_circuit(self, provider=providers.DEFAULT_PROVIDER):
        self.make_circuit()
        return self.qc.draw_circuit(provider=provider)
