<h1 align="center">
  <img src="https://github.com/artificial-brain/quantumcat/blob/assets/quantum_cat_logo.jpg?raw=true" alt="Quantum Cat Logo" width="400" height="400" />
</h1>

### Table of Contents

- [1. Introduction](#introduction)
  * [1.1 Purpose](#purpose)
  * [1.2 Current Problems](#current-problems)
  * [1.2 Solutions](#solutions)
- [2. Platforms Supported](#platforms-supported)
- [3. Gates Supported](#gates-supported)
- [4. Algorithms](#algorithms)
- [5. Examples](#examples)
  * [5.1 Circuit Creation](#circuit-creation)
  * [5.2 Single Qubit Gate](#single-qubit-gate)
  * [5.3 Multi Qubit Gate](#multi-qubit-gate)
- [6. Applications](#applications)


## Introduction
A cross platform high-level quantum computing library so that you could concentrate on building Quantum applications faster.
## Purpose
## Current Problems
## Solutions
## Platforms Supported
* IBM Qiskit
* Google Cirq
## Gates Supported
[Click here to view gates supported](https://sheet.zoho.com/sheet/published/nvlfe4b782cabaa524276ab9a44e270d800b2?mode=html)
## Algorithms
## Examples
## Circuit Creation
```python
from quantumcat.circuit import QCircuit
num_of_qubits = 3
num_of_bits = 3
qc = QCircuit(num_of_qubits, num_of_bits)
```
## Single Qubit Gate
```python
qc.x_gate(0) # qubit number
```
## Multi Qubit Gate
```python
qc.cx_gate(0, 1) # qubit number
```
## Applications
