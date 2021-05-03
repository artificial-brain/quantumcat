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

from quantumcat.utils import constants
from qiskit import Aer
from qiskit import execute, QuantumCircuit
import cirq


def on_qiskit(q_circuit, backend, simulator_name, repetitions, api):
    if backend == constants.SIMULATOR:
        if simulator_name is None:
            simulator_name = constants.QASM_SIMULATOR
        results = execute(q_circuit, Aer.get_backend(simulator_name), shots=repetitions).result()
        return results


def on_cirq(q_circuit, backend, simulator_name, repetitions, api):
    if backend == constants.SIMULATOR:
        simulator = cirq.Simulator()
        results = simulator.run(q_circuit, repetitions=repetitions)
        return results


