from quantumcat.circuit import QCircuit
from quantumcat.utils import providers


if __name__ == '__main__':
    circuit = QCircuit(3, 2)
    circuit.x_gate(0)
    circuit.h_gate(1)
    circuit.i_gate(1)
    #circuit.cx_gate(0, 1)
    #circuit.x_gate(2)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    circuit.draw_circuit(provider=providers.GOOGLE_PROVIDER)
    circuit.draw_circuit(provider=providers.IBM_PROVIDER)
    print(circuit.execute(provider=providers.GOOGLE_PROVIDER, repetitions=10))
    print(circuit.execute(provider=providers.IBM_PROVIDER, repetitions=1000))
