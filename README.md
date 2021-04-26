<h1 align="center">
  <img src="https://github.com/artificial-brain/quantumcat/blob/assets/quantumcat/logo/quantum_cat_logo.jpg?raw=true" alt="Quantum Cat Logo" width="400" height="400" />
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
  * [5.3 Two Qubit Gate](#two-qubit-gate)
  * [5.4 Multi Qubit Gate](#multi-qubit-gate)
  * [5.5 Draw Circuit](#draw-circuit)
  * [5.6 Execute](#execute)
  * [5.7 Grovers Algorithm](#grovers-algorithm)
    + [Unknown Solution](#unknown-solution)
    + [Known Solution](#known-solution)
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
qc.x_gate(0) # apply X gate on qubit 0
```
### Two Qubit Gate
```python
qc.cx_gate(0, 1) # control qubit, target qubit
```
## Multi Qubit Gate
```python
qc.mct_gate([0, 1], 2) # control qubits array, target qubit
```
## Draw Circuit
```python
from quantumcat.utils import providers

qc.draw_circuit(provider=providers.GOOGLE_PROVIDER) # OR provider=providers.IBM_PROVIDER, For IBM Qiskit
```
## Execute
```python
results = qc.execute(provider=providers.GOOGLE_PROVIDER, repetitions=1024) # OR provider=providers.IBM_PROVIDER, For IBM Qiskit
```
## Grovers Algorithm
### Unknown Solution
```python
# Finding solution for sudoku
clause_list_sudoku = [[0, 1], [0, 2], [1, 3], [2, 3]]
grovers_algorithm_unknown_solution = GroversAlgorithm(clause_list=clause_list_sudoku, flip_output=True, solution_known='N')
result = grovers_algorithm_unknown_solution.execute(repetitions=2, provider=providers.GOOGLE_PROVIDER) # OR provider=providers.IBM_PROVIDER, For IBM Qiskit
print(results) # solutions are 1001 and 0110

q0=10
q1=01
q2=01
q3=10
```

### Known Solution
```python

# Unstructured search
grovers_algorithm_known_solution = GroversAlgorithm(solution_known='Y', search_keyword=101)
result = grovers_algorithm_known_solution.execute(repetitions=1, provider=providers.GOOGLE_PROVIDER) # OR provider=providers.IBM_PROVIDER, For IBM Qiskit
print(results)

q0=1
q1=0
q2=1
```
## Applications
