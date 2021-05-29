## Protein Structure Prediction
This project contains a specific application of the protein folding algorithm mentioned in the paper "Quantum Speedup for Protein Structure Prediction" by Renata Wong and Weng-Long Chang. The paper can be found [here](https://pubmed.ncbi.nlm.nih.gov/33690123/).

In this specific code of the algorithm represented in the paper, a sequence |a> = |11> was assumed implicitly, while the arbitrary chose conformation was |w> = |110>

This project consists of the following files:
* **proteinfolding.py** - contains the subroutines for the protein folding algorithm
    - subroutine 1 - Calculating three-dimensional cartesian coordinates |x>, |y> and |z> for each conformation
    - subroutine 2 - Calculating the energy values of each conformation
    - subroutine 3 - Uncomputation of the coordinates of all conformations by running subroutine 1 in reverse
    - subroutine 4 - Applying Grover's Algorithm
* **ccrca.py** - contains the code for controlled-controlled ripple carry adder, required for implementation of the algorithm. This is a slightly modified version of what is suggested in "A new quantum ripple-carry addition circuit" by Cuccaro et al [[Link to the paper](https://arxiv.org/abs/quant-ph/0410184)]. The controls involve just additional qubits that have been incorporated into the adder. The carry bit in the code (z in Fig. 6 of the paper) is skipped as it was not needed for the application. The general idea is that, for 2 control qubits, we have to use a Toffoli gate with these 2 control qubits and an ancilla qubit as the target. Then, each operation in the adder given in Cuccaro has to be made dependent on this ancilla qubit. Please compare figure 6 in Cuccaro with the modified circuit.
* **ccrca_inverse.py** - contain the inversed version of the controlled-controlled ripple carry adder.

## Executing the algorithm
The application can be executed in the following manner:-

- Importing the application
```python
from quantumcat.applications import ProteinFolding
```

- Running the application
```python
job = ProteinFolding(11)                    # 11 is currently dummy, placed parameter for future improvements on code
result = job.run(providers.GOOGLE_PROVIDER) # IBM_PROVIDER for executing the file using IBM
print(result)
```
- Understanding the results
```
{'111': 12, '011': 934, '010': 18, '000': 17, '100': 10, '110': 15, '001': 7, '101': 11}
```
    
The above dictionary is the result after one execution of the code. It shows the number of times each state is counted (to be read from right to left). Clearly, the most number of counts is with the state 110 (our expected state) which is 934.

## Further improvements (suggested)
The code currently is hard-coded for only one particular output state. Also, due to the limitation of the number of qubits, the length of the input sequence is taken to be 2. However, real world protein sequences are very much longer than that. The 11 in the ```ProteinFolding(11)``` function is a dummy, intended to be replaced with the actual user input sequence once we have a more generalised version of the code. The output is also currently the 110 state, and can be further generalised to figure out the conformation with the lowest energy among all the conformational states.