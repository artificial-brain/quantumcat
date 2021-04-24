from quantumcat.gate import XGate
import cirq

if __name__ == '__main__':
    # qc = QuantumCircuit(1)
    qc = cirq.Circuit()
    # cirq.NamedQubit("a")
    # config.provider = 'Google'
    x_gate = XGate(qc,  cirq.NamedQubit("a"))
    print(x_gate.apply())
