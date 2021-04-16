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
from math import pi

from quantumcat.circuit import QCircuit
from quantumcat.utils import providers
from qiskit import QuantumCircuit


if __name__ == '__main__':
    circuit = QCircuit(3, 3)
    circuit.x_gate(0)
    circuit.x_gate(1)
    circuit.ccx_gate(0, 1, 2)
    circuit.s_gate(0)
    # circuit.sdg_gate(0)  # not in cirq
    circuit.swap_gate(0, 1)
    circuit.iswap_gate(1, 0)
    # circuit.sx_gate(0)  # not in cirq
    # circuit.sxd_gate(0)  # not in cirq
    circuit.t_gate(0)
    # circuit.td_gate(0)  # not in cirq
    circuit.u1_gate(pi, 0)
    # circuit.x_gate(1)
    # circuit.entangle(0, 1)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    circuit.measure(2, 2)
    circuit.draw_circuit(provider=providers.IBM_PROVIDER)
    # circuit.draw_circuit(provider=providers.GOOGLE_PROVIDER)
    # print(circuit.execute(provider=providers.GOOGLE_PROVIDER, repetitions=10))
