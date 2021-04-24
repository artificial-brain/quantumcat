from quantumcat import config
import cirq
from quantumcat.circuit import Circuit

if __name__ == '__main__':
    config.provider = 'IBM'
    quantum_circuit = Circuit(2,2)
    quantum_circuit.draw()
