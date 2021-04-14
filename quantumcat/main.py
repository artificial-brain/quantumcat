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
from qiskit import QuantumCircuit

if __name__ == '__main__':
    qc = QuantumCircuit(2,2)
    qc.x([0, 1])
    print(qc.draw())
    circuit = QCircuit(3, 3)
    # circuit.x_gate(0)
    # circuit.cx_gate(0, 1)
    # circuit.x_gate(1)
    circuit.entangle(0, 1)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    circuit.draw_circuit(provider=providers.IBM_PROVIDER)
    print(circuit.execute(provider=providers.IBM_PROVIDER, repetitions=10))
