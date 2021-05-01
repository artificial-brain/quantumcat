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


circuit = QCircuit(3, 3)
circuit.x_gate(0)
circuit.z_gate(0)
circuit.h_gate(1)
# circuit.u3_gate(30, 0, 2, 0)
# circuit.td_gate(0)
circuit.cx_gate(0, 1)
circuit.ccx_gate(0, 1, 2)
# circuit.measure(0, 0)
circuit.draw_circuit(provider=providers.IBM_PROVIDER)
circuit.draw_circuit(provider=providers.AMAZON_PROVIDER)
# print(circuit.execute(provider=providers.AMAZON_PROVIDER, repetitions=10))
# print(circuit)
