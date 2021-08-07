

<h1 align="center">  
  <img src="https://github.com/artificial-brain/quantumcat/blob/assets/quantumcat/logo/quantum_cat_logo.jpg?raw=true" alt="Quantum Cat Logo" width="250" height="250" />  
</h1>  
  
  
## Introduction  
quantumcat is a platform-independent, open-source, high-level quantum computing library, which allows the quantum community to focus on developing platform-independent quantum applications without much effort.
## It is based on two principles:
1) Write once and execute on any supported quantum provider using one syntax

2) quantumcat should enable researchers and developers to create quantum applications using high-level programming in the future so that they can focus on developing quantum applications instead of learning low-level concepts such as gates and circuits

### Write once
```python  
from quantumcat.utils import providers  
num_of_qubits = 2
qc = QCircuit(num_of_qubits)
qc.h_gate(0)
qc.cx_gate(0, 1)

# To execute on Google Cirq
result = qc.execute(provider=providers.GOOGLE_PROVIDER, repetitions=1024) 
```  
```python  
# To execute on IBM Qiskit
result = qc.execute(provider=providers.IBM_PROVIDER, repetitions=1024)
```  
```python  
# To execute on Amazon Braket
result = qc.execute(provider=providers.AMAZON_PROVIDER, repetitions=1024)
```

### Compare the results of all the supported providers with a single line of code

```python  
# Execute on All providers in one go
circuit.compare_results(plot=True)
```
<h1 align="center">  
  <img src="https://github.com/artificial-brain/quantumcat/blob/assets/quantumcat/screenshots/compare-histogram.png?raw=true" alt="Compare Results" width="400" height="300" />  
</h1>  

### Execute on real IBM quantum hardware with quantumcat
```python  
from quantumcat.utils import providers  
  
result = qc.execute(provider=providers.IBM_PROVIDER,
api='API KEY from IBM Quantum dashboard', 
device='IBM DEVICE NAME such as ibmq_manila or ibmq_quito')  
# Copy API and Device name from https://quantum-computing.ibm.com/  
```
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
qc.x_gate(0) # applies X gate on qubit 0  
```  
### Two-Qubit Gate  
```python  
qc.cx_gate(0, 1) # control qubit, target qubit  
```  
### Multi-Qubit Gate  
```python  
qc.mct_gate([0, 1], 2) # control qubits array, target qubit  
```  
### Draw Circuit  
```python  
from quantumcat.utils import providers  
  
qc.draw_circuit(provider=providers.GOOGLE_PROVIDER)
```  
## High-Level Functions  

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
## High-Level Applications  

### Random Number Generator  
```python  
from quantumcat.utils import providers, constants  
from quantumcat.applications.generator import RandomNumber  
  
random_number = RandomNumber(length=2, output_type=constants.DECIMAL).execute(provider=providers.GOOGLE_PROVIDER)
print(random_number)  

# To generate random number on actual IBM device  
random_number = RandomNumber(length=2, output_type=constants.DECIMAL)
	.execute(provider=providers.IBM_PROVIDER, repetitions=1024, api='API KEY from IBM Quantum dashboard'
		 device='IBM DEVICE NAME such as ibmq_manila or ibmq_quito')
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

## Visualization  
### Histogram
```python  
circuit = QCircuit(1)
circuit.superposition(0)
counts = circuit.execute(provider=providers.GOOGLE_PROVIDER, repetitions=1024)
circuit.histogram(counts) 
```
<h1 align="center">  
  <img src="https://github.com/artificial-brain/quantumcat/blob/assets/quantumcat/screenshots/single-histogram.png?raw=true" alt="Histogram" width=400" height="300"/>  
</h1>

### Bloch Multivector
```python  
circuit = QCircuit(1)
circuit.superposition(0)
state = circuit.execute(provider=providers.GOOGLE_PROVIDER, 
			simulator_name=constants.STATEVECTOR_SIMULATOR)
circuit.bloch_multivector(state) 
```

<h1 align="center">  
  <img src="https://github.com/artificial-brain/quantumcat/blob/assets/quantumcat/screenshots/bloch.png?raw=true" alt="Bloch Multivector" width="300" height="300" />  
</h1>

### QSphere
```python  
circuit = QCircuit(1)
circuit.superposition(0)
state = circuit.execute(provider=providers.GOOGLE_PROVIDER, 
			simulator_name=constants.STATEVECTOR_SIMULATOR)
circuit.state_qsphere(state) 
```

<h1 align="center">  
  <img src="https://github.com/artificial-brain/quantumcat/blob/assets/quantumcat/screenshots/qsphere.png?raw=true" alt="QSphere" width="300" height="300" />  
</h1>

## License  
  
[Apache License 2.0](LICENSE.txt)
