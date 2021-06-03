Setting up a Circuit
=====================

Initializing a quantum circuit
------------------------------

For creating a quantum circuit and executing it, we need to need to import the QCircuit class from the quantumcat directory.

>>> from quantumcat.circuit import QCircuit

This command initializes the QCircuit class in quantumcat, which contains all the methods you need to create a quantum circuit. It also contains methods that can help to visualize the current state of the circuit.

>>> num_of_qubits = 3
>>> num_of_cbits = 3
>>> qc = QCircuit(num_of_qubits, num_of_bits)

This set of commands initializes a quantum circuit, inside the variable name **qc**, which contains 3 qubits and 3 classical bits.
By default, the qubits when initialized are set to the |0> state.
