from quantumcat.circuit import QCircuit

if __name__ == '__main__':
    circuit = QCircuit(2, 2)
    circuit.x_gate(1)
    circuit.y_gate(0)
    circuit.z_gate(1)
    circuit.x_gate(1)
    circuit.draw_circuit()
