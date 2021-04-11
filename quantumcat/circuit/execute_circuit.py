from quantumcat.utils import constants
from qiskit import Aer
from qiskit import execute
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


