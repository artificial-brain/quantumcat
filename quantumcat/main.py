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
from quantumcat.applications.generator import RandomNumber


def create_circuit_demo():
    circuit = QCircuit(6)
    circuit.h_gate(0)
    circuit.x_gate(3)
    circuit.measure_all()
    # circuit.draw_circuit(provider=providers.IBM_PROVIDER)
    print(circuit.execute(provider=providers.IBM_PROVIDER, repetitions=10))


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
    random_number = RandomNumber(length=2, output_type=constants.DECIMAL)\
        .execute(provider=providers.AMAZON_PROVIDER)
    print(random_number)


def run_on_real_device():
    circuit = QCircuit(1)
    circuit.x_gate(0)
    circuit.measure_all()
    # circuit.draw_circuit(provider=providers.GOOGLE_PROVIDER)
    print(circuit.execute(provider=providers.IBM_PROVIDER, repetitions=10,
                          api=constants.IBM_API, device=constants.IBM_DEVICE_NAME))


def braket_demo():
    circuit = QCircuit(3)
    # circuit.h_gate(0)
    # circuit.cx_gate(0, 1)
    # circuit.x_gate(0)
    # circuit.z_gate(0)
    # circuit.ccx_gate(0, 1, 2)
    # circuit.s_gate(0)
    # circuit.sdg_gate(0)
    # circuit.swap_gate(0, 1)
    # circuit.iswap_gate(0, 1)
    # circuit.sx_gate(0)
    # circuit.sxd_gate(0)
    # circuit.t_gate(0)
    # circuit.td_gate(0)
    # circuit.i_gate(0)
    # circuit.cy_gate(0, 1)
    # circuit.cz_gate(0, 1)
    # circuit.cswap_gate(0, 1, 2)
    # circuit.rx_gate(30, 0)
    # circuit.ry_gate(30, 0)
    # circuit.cphase_gate(30, 0, 1)
    # circuit.ryy_gate(30, 0, 1)
    # circuit.rz_gate(30, 0)
    # circuit.rxx_gate(30, 0, 1)
    # circuit.p_gate(30, 0)
    # circuit.rzz_gate(30, 0, 1)

    circuit.draw_circuit(provider=providers.AMAZON_PROVIDER)
    print(circuit.execute(provider=providers.AMAZON_PROVIDER))
    # print(circuit.execute(provider=providers.AMAZON_PROVIDER, simulator_name=constants.STATEVECTOR_SIMULATOR))


if __name__ == '__main__':
    random_number_demo()
