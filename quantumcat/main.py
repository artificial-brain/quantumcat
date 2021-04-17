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
from quantumcat.utils import providers
from quantumcat.algorithms import GroversAlgorithm

if __name__ == '__main__':
    num_of_qubits = 3
    num_of_cbits = 3
    # circuit = QCircuit(num_of_qubits, num_of_cbits)
    # circuit.cz_gate(0, 2)
    # circuit.cz_gate(1, 2)
    clause_list = [[0, 1], [0, 2], [1, 3], [2, 3]]
    grovers_algorithm = GroversAlgorithm(clause_list, solution_known='N')
    results = grovers_algorithm.execute()
    grovers_algorithm.draw_grovers_circuit()
    print(results)


    # circuit.phase_kickback(0)

    # g_circuit.draw_circuit(provider=providers.IBM_PROVIDER)
    # print(g_circuit.execute(provider=providers.IBM_PROVIDER, repetitions=10))
