Standard set of Gates
======================
Quantum Gates are operations that are applied to qubits, in order to effect a change in the state of qubit.
Gates are the building blocks of any quantum circuit, and it with gates that every possible utilities of quantum computers are exploited. Quantum Gates are primarily of two types
	
	1. Single qubit Gates - Gates that operate only on a single qubit
	2. Multi-qubit Gates - Gates that operate on more than one qubit.

QuantumCat supports wide array of standard gate including single qubit gates and multi-qubit gates. All the standard gates are available in IBM Qiskit, Google Cirq and AWS braket are also included in the QuantumCat platform.

QuantumCat provides the following gates as standard gates that can be imported from the QCircuit class.

Single Qubit Operations
-------------------------

Now that the quantum circuit is setup, we can move forward and start performing operations on the circuit.
The fundamental operations on any quantum circuits are single qubit gates. Here, we will demonstrate the application of an X gate to a qubit of the **qc** quantum circuit.

>>> qc.x_gate(0)

The above command applies the X gate to the qubit at index 0, which is the first qubit of our circuit.
Since the qubit was in the |0> state, the application of the X gate has set it to the |1> state.
Similarly other single qubits gates can be applied to any of the qubits in the circuit, by varying the name of the gate and also the required index of the qubit. For details about single qubit gates, refer to QuantumCat API documentation.

Multi-Qubit Operations
-----------------------

QuantumCat supports multi-qubit operations on qubits. Multi-qubit operations are the key elements of any practical quantum algorithms and circuits. These are operations that are applied on more than 1 qubits.
We will show you a simple CX Gate application here.

>>> qc.cx_gate(0,1)

This command applies the CX gate to the qubits at index 0 and 1, implying that the control qubit for the CX gate, will be the qubit at index 0 and the tatget qubit will be the qubit at index 1.
QuantumCat supports a wide range of multi-qubit gates. You can check them out at QuantumCat API docuemntation.