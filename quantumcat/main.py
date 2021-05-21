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
from quantumcat.utils import providers, constants
from quantumcat.algorithms import GroversAlgorithm

from quantumcat.applications import ProteinFolding

from quantumcat.applications.generator import RandomNumber



def create_circuit_demo():
    circuit = QCircuit(6)
    circuit.x_gate(0)
    circuit.measure_all()
    # circuit.measure(0)
    # circuit.measure(1)
    # # circuit.measure(2)
    circuit.draw_circuit(provider=providers.IBM_PROVIDER)
    print(circuit.execute(provider=providers.IBM_PROVIDER, repetitions=10,
                          simulator_name=constants.STATEVECTOR_SIMULATOR))


def grovers_demo():
    clause_list_sudoku = [[0, 1], [0, 2], [1, 3], [2, 3]]
    clause_list_light_board = [[0, 1, 3], [1, 0, 2, 4], [2, 1, 5], [3, 0, 4, 6],
                               [4, 1, 3, 5, 7], [5, 2, 4, 8], [6, 3, 7], [7, 4, 6, 8],
                               [8, 5, 7]]

    input_arr = [0, 0, 0, 1, 0, 1, 1, 1, 0]

    grovers_algorithm_unknown_solution = GroversAlgorithm(clause_list=clause_list_light_board, input_arr=input_arr,
                                                          flip_output=True, solution_known='N')

    grovers_algorithm_known_solution = GroversAlgorithm(solution_known='Y', search_keyword=101)

    results = grovers_algorithm_unknown_solution.execute(repetitions=10, provider=providers.IBM_PROVIDER)

    # grovers_algorithm_unknown_solution.draw_grovers_circuit()

    print(results)

def random_number_demo():
    random_number = RandomNumber(length=4, output_type=constants.DECIMAL)\
        .execute(api=constants.IBM_API, device=constants.IBM_DEVICE_NAME)
    print(random_number)

def run_on_real_device():
    circuit = QCircuit(1)
    circuit.x_gate(0)
    circuit.measure_all()
    # circuit.draw_circuit(provider=providers.GOOGLE_PROVIDER)
    print(circuit.execute(provider=providers.IBM_PROVIDER, repetitions=10,
                          api=constants.IBM_API, device=constants.IBM_DEVICE_NAME))

def test_demo():
    a = [0, 1, 2]
    b = [3, 4, 5]
    qc = QCircuit(6)
    qc.x_gate(2)
    qc.x_gate(5)
    qc.measure(0)
    qc.measure(2)
    #qc.measure_all()
    """for i in range(6):
        qc.measure(i)"""
    qc.draw_circuit(provider=providers.IBM_PROVIDER)
    print(qc.execute(provider=providers.GOOGLE_PROVIDER, repetitions=10))

def protein_folding_demo():
    job = ProteinFolding(11)                    #11 is currently dummy, placed parameter for future improvements on code
    result = job.run(providers.GOOGLE_PROVIDER)
    print(result)

if __name__ == '__main__':
    protein_folding_demo()