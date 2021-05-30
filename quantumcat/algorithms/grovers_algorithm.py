# (C) Copyright Artificial Brain 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from quantumcat.utils import providers
from quantumcat.circuit import QCircuit
import numpy as np


class GroversAlgorithm:
    """
    The GroversAlgorithm class functions to enable all the requisites for the implemetation of Grover's Algorithm
    for the cases in which the solutions are known and unknown.
    """
    def __init__(self, clause_list=[], input_arr=[], search_keyword=None, solution_known='N', flip_output=False, num_of_iterations=None):
         """
        Initializes the GroversAlgorithm class and enable the smooth running of all the included
        operations.
        """
        super(GroversAlgorithm, self).__init__()
        self.clause_list = clause_list
        self.input_arr = input_arr
        self.search_keyword = search_keyword
        self.solution_known = solution_known
        self.flip_output = flip_output
        self.num_of_qubits = len(self.clause_list) if self.solution_known == 'N' else len(str(search_keyword))
        self.total_qubits = 0
        self.circuit = None
        self.provider = None
        if num_of_iterations is None:
            self.num_of_iterations = self.get_num_of_iterations()

    def initialize(self, provider):
    	"""
        Initialize function carries out the task of initializing the algorithm to solve the problem under consideration.
        """ 
        self.total_qubits = (2 * self.num_of_qubits) + 1 if self.solution_known == 'N' else (self.num_of_qubits + 1)
        self.circuit = QCircuit(self.total_qubits,  self.num_of_qubits)
        self.provider = provider

        # Initialise input qubits in superposition
        for qubit in range(self.num_of_qubits):
            self.circuit.h_gate(qubit)

        for index in range(len(self.input_arr)):
            if self.input_arr[index] == 1:
                self.circuit.x_gate(self.num_of_qubits + index)

        # Initialise output qubit in the |-⟩ state.
        self.circuit.x_gate(self.total_qubits - 1)
        self.circuit.h_gate(self.total_qubits - 1)

    def oracle_for_unknown_solution(self):
    	"""
        Creates the oracle for finding the solution, when the solution to the problem is not known
        beforehand.
        """
        output_qubit = self.total_qubits - 1
        clause_qubits = []

        for index in range(len(self.clause_list)):
            clause_qubit = self.num_of_qubits + index
            self.XOR(self.clause_list[index], clause_qubit)
            clause_qubits.append(clause_qubit)

        if self.flip_output:
            for index in range(len(clause_qubits)):
                self.circuit.x_gate(clause_qubits[index])

        # Flip 'output' bit if all clauses are satisfied
        self.circuit.mct_gate(clause_qubits, output_qubit)

        if self.flip_output:
            for index in range(len(clause_qubits)):
                self.circuit.x_gate(clause_qubits[index])

        for index in range(len(self.clause_list)):
            clause_qubit = self.num_of_qubits + index
            self.XOR(self.clause_list[index], clause_qubit)

    def oracle_for_known_solution(self):
    	"""
        Creates the oracle for the problem under consideration, when the solution is known beforehand.
        """
        output_qubit = self.total_qubits - 1
        input_qubits = []
        keyword = self.search_keyword
        for index in range(len(str(keyword))):
            if not int(str(keyword)[index]):
                self.circuit.x_gate(index)
            input_qubits.append(index)

        self.circuit.mct_gate(input_qubits, output_qubit)

        for index in range(len(str(keyword))):
            if not int(str(keyword)[index]):
                self.circuit.x_gate(index)

    def XOR(self, qubits, output_qubit):
    	"""
        Generates and XOR classical logic gate.
        Parameters:
        <qubits> - takes in list of qubit indices as input for XOR
        <coutput_qubit> - takes in the index of target qubit
        """
        for qubit in qubits:
            self.circuit.cx_gate(qubit, output_qubit)

    def diffuser(self):
    	"""
    	Creates the diffuser circuit for running the algorithm.
    	"""
        q_circuit = self.circuit
        qubits = self.num_of_qubits

        for qubit in range(qubits):
            q_circuit.h_gate(qubit)

        for qubit in range(qubits):
            q_circuit.x_gate(qubit)

        q_circuit.h_gate(qubits-1)
        q_circuit.mct_gate(list(range(qubits-1)), qubits-1)
        q_circuit.h_gate(qubits-1)

        for qubit in range(qubits):
            q_circuit.x_gate(qubit)

        for qubit in range(qubits):
            q_circuit.h_gate(qubit)

    def execute(self, provider=providers.DEFAULT_PROVIDER, repetitions=10):
    	"""
    	Executes the circuit by calling in the provider that executes the algorithm
    	
    	Parameters:
    	<provider> - takes in specified provider as a string input
    	<repetitions> - takes in the number of executions of the circuit
		
		Returns: Solution after executing the algorithm
    	"""
        self.initialize(provider)

        for _ in range(self.num_of_iterations):
            if self.solution_known == 'N':
                self.oracle_for_unknown_solution()
            else:
                self.oracle_for_known_solution()
            self.diffuser()

        for i in range(self.num_of_qubits):
            self.circuit.measure(i)

        return self.circuit.execute(provider=provider, repetitions=repetitions)

    def draw_grovers_circuit(self):
    	"""
    	Generates circuit diagram of the Grover's algorithm.

    	Returns: Schematic representation of circuit for the algorithm
    	"""
        return self.circuit.draw_circuit(provider=self.provider)

    def get_num_of_iterations(self):
        return int(0.5*(0.5*np.pi/np.arcsin(1/(np.sqrt(2 ** self.num_of_qubits)))-1))
