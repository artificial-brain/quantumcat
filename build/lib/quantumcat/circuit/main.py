from quantumcat.circuit import Circuit

if __name__ == '__main__':
    quantum_circuit = Circuit(2,2).create()
    print(quantum_circuit.draw())
