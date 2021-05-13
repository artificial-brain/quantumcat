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

from quantumcat.utils import constants, helper
from qiskit import Aer
from qiskit import execute, QuantumCircuit
import cirq


def on_qiskit(q_circuit, simulator_name, repetitions, api):
    results = execute(q_circuit, Aer.get_backend(simulator_name), shots=repetitions).result()
    if simulator_name == constants.DEFAULT_SIMULATOR:
        return results.get_counts()
    elif simulator_name == constants.STATEVECTOR_SIMULATOR:
        return results.get_statevector()


def on_cirq(q_circuit, simulator_name, repetitions, api, operations):
    simulator = cirq.Simulator()
    if simulator_name == constants.DEFAULT_SIMULATOR:
        result = simulator.run(q_circuit, repetitions=repetitions)
        qubits_index = helper.measure_qubits_index(operations)
        return dict(result.multi_measurement_histogram(keys=qubits_index, fold_func=helper.bitstring) \
            if len(qubits_index) > 0 else result.histogram(key='result', fold_func=helper.bitstring))
    elif simulator_name == constants.STATEVECTOR_SIMULATOR:
        return simulator.simulate(q_circuit).final_state_vector()
