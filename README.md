<h1 align="center">
  <img src="https://github.com/artificial-brain/quantumcat/blob/assets/quantumcat/logo/quantum_cat_logo.jpg?raw=true" alt="Quantum Cat Logo" width="250" height="250" />
</h1>


### Table of Contents

- [1. Introduction](#introduction)
  * [1.1 Purpose](#purpose)
  * [1.2 Problems with current QC Libraries](#problems-with-current-qc-libraries)
  * [1.3 Installation](#installation)
- [2. Platforms Supported](#platforms-supported)
- [3. Gates Supported](#gates-supported)
- [4. Examples](#examples)
  * [6.1 Circuit Creation](#circuit-creation)
  * [6.2 Single-Qubit Gate](#single-qubit-gate)
  * [6.3 Two-Qubit Gate](#two-qubit-gate)
  * [6.4 Multi-Qubit Gate](#multi-qubit-gate)
  * [6.5 Superposition](#superposition)
  * [6.6 Entanglement](#entanglement)
  * [6.7 Phase Kickback](#phase-kickback)    
  * [6.8 Draw Circuit](#draw-circuit)
  * [6.9 Execute on Simulator](#execute-on-simulator)
  * [6.10 Execute on real IBM device](#execute-on-real-ibm-device)
- [7. Applications](#applications)
   * [7.1 Random Number](#random-number-generator)
   * [7.2 Password](#password-generator)
   * [7.3 OTP](#otp-generator)
- [8. License](#license)


## Introduction
A cross-platform open-source high-level quantum computing library so that the quantum community could concentrate on building quantum applications without much effort.
## Purpose
**quantumcat** is a cross-platform library and is built on the principle of write once and execute any quantum provider. The purpose of this library is to help developers create cross-platform quantum applications in few lines of code.
## Problems with current QC Libraries
* **Platform dependent code**:
To execute code on platforms such as IBM, Google, and so on, Developers need to write code separately for each platform independently putting lots of efforts.
* **Basic Knowledge of quantum gates and circuits required**:
  Presently, It is very tough to create quantum applications given the fact that many available libraries are low-level libraries i.e. developers have to understand low-level concepts such as gates and circuits before they can actually start working on quantum applications. This is not natural to many developers who are accustomed to high-level concepts rather than worrying about gates and circuits.
## Installation
```shell
pip install quantumcat
```
## Platforms Supported
* Google Cirq
* IBM Qiskit
* Amazon Braket
* IonQ (Via Braket)
* Rigetti (Via Braket)
## Gates Supported
[Click here to view gates supported](https://drive.google.com/file/d/1XNCY2NyioTpqNII4dalm4plKE2-suKYB/view)

## Examples
### Circuit Creation
```python
from quantumcat.circuit import QCircuit

num_of_qubits = 3
qc = QCircuit(num_of_qubits)
```
### Single-Qubit Gate
```python
qc.x_gate(0) 
# applies X gate on qubit 0
```
### Two-Qubit Gate
```python
qc.cx_gate(0, 1) 
# control qubit, target qubit
```
### Multi-Qubit Gate
```python
qc.mct_gate([0, 1], 2) 
# control qubits array, target qubit
```
### Superposition
```python
qc.superposition(0) 
# puts qubit 0 in superposition
```
### Entanglement
```python
qc.entangle(0, 1) 
# entangles qubit 0 with qubit 1
```
### Phase Kickback
```python
qc.phase_kickback(0) 
# applies |-> to qubit 0
```
### Draw Circuit
```python
from quantumcat.utils import providers

qc.draw_circuit(provider=providers.GOOGLE_PROVIDER) 
# OR providers.IBM_PROVIDER / providers.AMAZON_PROVIDER 
```
### Execute on Simulators
```python
from quantumcat.utils import providers

results = qc.execute(provider=providers.GOOGLE_PROVIDER, repetitions=1024) 
# OR providers.IBM_PROVIDER / providers.AMAZON_PROVIDER
```
### Execute on real IBM device
```python
from quantumcat.utils import providers

results = qc.execute(provider=providers.IBM_PROVIDER, repetitions=1024, 
api='API KEY from IBM Quantum dashboard', device='IBM DEVICE NAME such as ibmq_manila or ibmq_quito')
# Copy API and Device name from https://quantum-computing.ibm.com/
```

## Applications
### Random Number Generator
```python
from quantumcat.utils import providers, constants
from quantumcat.applications.generator import RandomNumber

random_number = RandomNumber(length=2, output_type=constants.DECIMAL)\
        .execute(provider=providers.GOOGLE_PROVIDER)
# OR providers.IBM_PROVIDER / providers.AMAZON_PROVIDER
print(random_number)

# To generate random number on actual IBM device
random_number = RandomNumber(length=2, output_type=constants.DECIMAL)\
        .execute(provider=providers.IBM_PROVIDER, repetitions=1024, 
api='API KEY from IBM Quantum dashboard', device='IBM DEVICE NAME such as ibmq_manila or ibmq_quito')
print(random_number)
```
### Password Generator
```python
from quantumcat.applications.generator import Password

password = Password(8).generate()
print(password)
# Length should be between 5 - 20
# Password is generated in hexadecimal format using QRNG@ANU JSON API
```
### OTP Generator
```python
from quantumcat.applications.generator import OTP

otp = OTP().generate()
print(otp)
# 5 digits OTP is generated using QRNG@ANU JSON API
```

## License

[Apache License 2.0](LICENSE.txt)
