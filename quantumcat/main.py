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

from quantumcat.circuit import QCircuit
from quantumcat.utils import providers, constants
from quantumcat.algorithms import GroversAlgorithm

#from qiskit import *
from quantumcat.applications.protein_folding import CCRCA, CCRCA_INVERSE

from quantumcat.applications.generator import RandomNumber
from qiskit import IBMQ



def create_circuit_demo():
    circuit = QCircuit(2)
    circuit.x_gate(0)
    circuit.measure_all()
    # circuit.measure(0)
    # circuit.measure(1)
    # # circuit.measure(2)
    circuit.draw_circuit(provider=providers.IBM_PROVIDER)
    print(circuit.execute(provider=providers.IBM_PROVIDER, repetitions=10,
                          simulator_name=constants.STATEVECTOR_SIMULATOR))


def grovers_demo():
    clause_list_sudoku = [[0, 1], [0, 2], [1, 3], [2, 3]]
    clause_list_light_board = [[0, 1, 3], [1, 0, 2, 4], [2, 1, 5], [3, 0, 4, 6],
                               [4, 1, 3, 5, 7], [5, 2, 4, 8], [6, 3, 7], [7, 4, 6, 8],
                               [8, 5, 7]]

    input_arr = [0, 0, 0, 1, 0, 1, 1, 1, 0]

    grovers_algorithm_unknown_solution = GroversAlgorithm(clause_list=clause_list_light_board, input_arr=input_arr,
                                                          flip_output=True, solution_known='N')

    grovers_algorithm_known_solution = GroversAlgorithm(solution_known='Y', search_keyword=101)

    results = grovers_algorithm_unknown_solution.execute(repetitions=10, provider=providers.IBM_PROVIDER)

    # grovers_algorithm_unknown_solution.draw_grovers_circuit()

    print(results)



def protein_folding_demo():

    length = 2
    x = [0, 1, 2]
    y = [3, 4, 5]
    z = [6, 7, 8]
    w = [9, 10, 11]
    a = [12, 13, 14]
    c = [15]
    e = [16]
    anc = [17, 18, 19]
    # classical register
    #out = ClassicalRegister(3,'out')
    # quantum circuit consisting of all quantum and classical registers
    qc = QCircuit(20) 

    # encoding binary 1
    qc.x_gate(a[2])
    # encoding the two's complement of 1
    #qc.x(t[0:length])

    # setting the state into superposition
    #qc.h_gate(w[0:3])
    
    for i in range(len(w)):
        qc.h_gate(w[i])

    # setting energy qubit e into superposition on par with |w>
    qc.h_gate(e[0])


    # global variable used in Subroutine 1 to navigate among the values of vector w
    b = 0
    arglist = []

    # Subroutine 1: Generating conformational space

    for d in range (2,length+1):
        
        
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        # if w[0]=1 then x+1, if w[0]=0 then x-1
        arglist.append(w[b])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        #range [0,1,2] for d=2, range [3,4,5] for d=3
        for i in range(0,3): 
            arglist.append(x[i])
        for i in range(0,3):
            arglist.append(a[i])
        #print(arglist)
        CCRCA(qc, arglist)
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        qc.x_gate(w[b])
        arglist.append(w[b])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        for i in range(0,3): 
            arglist.append(x[i])
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA(qc, arglist)
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        qc.x_gate(w[b])
        
        
        # if w[1]=1 then y+1, if w[1]=0 then y-1
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        arglist.append(w[b+1])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        #range [0,1,2] for d=2, range [3,4,5] for d=3
        for i in range(0,3): 
            arglist.append(y[i])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA(qc, arglist)
        
        
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        qc.x_gate(w[b+1])
        arglist.append(w[b+1])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        for i in range(0,3): 
            arglist.append(y[i])
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA(qc, arglist)
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        qc.x_gate(w[b+1])
        
        
        
        
        # if w[2]=1 then z+1, if w[2]=0 then z-1
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        arglist.append(w[b+2])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        #range [0,1,2] for d=2, range [3,4,5] for d=3
        for i in range(0,3): 
            arglist.append(z[i])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA(qc, arglist)
        
        
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        qc.x_gate(w[b+2])
        arglist.append(w[b+2])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        for i in range(0,3): 
            arglist.append(z[i])
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA(qc, arglist)
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        qc.x_gate(w[b+2])
        
        #b = b+3
        
    # Subroutine 2: Finding an arbitrary conformation, e.g. |w>=|110> which is 
    # a transition downwards out of the page. 
    # There are a total of 8 conformations for a sequence of length L=2.
    # For this conformation, the energy value will be |e>=|1>, otherwise it will be |0>. 
    qc.h_gate(e[0])
    qc.x_gate(w[2])
    qc.ccx_gate(w[0],w[1],anc[0])
    qc.ccx_gate(anc[0],w[2],e[0])

    # uncomputing

    qc.ccx_gate(w[0],w[1],anc[0])
    qc.x_gate(w[2])
    qc.h_gate(e[0])






    # Subroutine 3: Uncomputation of coordinates by running Subroutine 1 in reverse
    b = 0

    for d in range (length,1,-1):
        
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        
        # if w[0]=1 then x+1, if w[0]=0 then x-1
        arglist.append(w[b])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        #range [0,1,2] for d=2, range [3,4,5] for d=3
        for i in range(0,3): 
            arglist.append(x[i])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA_INVERSE(qc, arglist)
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        qc.x_gate(w[b])
        arglist.append(w[b])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        for i in range(0,3): 
            arglist.append(x[i])
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA_INVERSE(qc, arglist)
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        qc.x_gate(w[b])
        
        
        # if w[1]=1 then y+a, if w[1]=0 then y-a
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        arglist.append(w[b+1])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        #range [0,1,2] for d=2, range [3,4,5] for d=3
        for i in range(0,3): 
            arglist.append(y[i])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA_INVERSE(qc, arglist)
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        qc.x_gate(w[b+1])
        arglist.append(w[b+1])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        for i in range(0,3): 
            arglist.append(y[i])
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA_INVERSE(qc, arglist)
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        qc.x_gate(w[b+1])
        
        
        
        
        # if w[2]=1 then z+1, if w[2]=0 then z-1
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        arglist.append(w[b+2])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        #range [0,1,2] for d=2, range [3,4,5] for d=3
        for i in range(0,3): 
            arglist.append(z[i])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA_INVERSE(qc, arglist)
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        qc.x_gate(w[b+2])
        arglist.append(w[b+2])
        for i in range(0,3):
            arglist.append(anc[i])
        arglist.append(c[0])
        for i in range(0,3): 
            arglist.append(z[i])
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        for i in range(0,3):
            arglist.append(a[i])
        CCRCA_INVERSE(qc, arglist)
        qc.x_gate(a[0])
        qc.x_gate(a[1])
        qc.x_gate(w[b+2])
        
        for i in range(len(arglist)-1,-1,-1):
            arglist.pop(i)
        
        #b = b-3






    # Subroutine 4: Finding conformation with e = 1 among 8. This can be done with 
    # Grover's search algorithm. Grover diffusion operator has to be executed 
    # pi/4 * sqrt(N/M) where N = 16 (all conformations) and M = 1 (solution). 
    # This is equal to ca. 3. Thus executing the search algorithm three times 
    # suffices to find a solution. 
    # The oracle has to mark the state 110. 


    # Grover's iteration
    for j in range(0,3):
        # the oracle, selects 110 (this oracle is correct, so is the diffusion operator)
        qc.h_gate(w[1])
        qc.x_gate(w[2])
        qc.ccx_gate(w[0],w[2],anc[0])
        qc.ccx_gate(anc[0],e[0],w[1])
        # uncomputing
        qc.ccx_gate(w[0],w[2],anc[0])
        qc.x_gate(w[2])
        qc.h_gate(w[1])


        # The diffusion operator
        for i in range(0,3):
            qc.h_gate(w[i])
            qc.x_gate(w[i])  
        qc.h_gate(e[0])
        qc.x_gate(e[0])
        
        qc.ccx_gate(e[0],w[0],anc[0])
        qc.h_gate(w[2])
        qc.ccx_gate(anc[0],w[1],w[2])

        # uncompute
        qc.h_gate(w[2])
        qc.ccx_gate(e[0],w[0],anc[0])
        
        for i in range(0,3):
            qc.x_gate(w[i])
            qc.h_gate(w[i])  
        qc.x_gate(e[0])
        qc.h_gate(e[0])

    #qc.draw_circuit(provider=providers.IBM_PROVIDER)
    for i in range(0,3): 
        qc.measure(w[i])
    qc.draw_circuit(provider=providers.IBM_PROVIDER)
    

    #result = qc.execute(provider=providers.IBM_PROVIDER)
    #print(result)
    

def random_number_demo():
    random_number = RandomNumber(length=4, output_type=constants.DECIMAL)\
        .execute(api=constants.IBM_API, device=constants.IBM_DEVICE_NAME)
    print(random_number)


def run_on_real_device():
    circuit = QCircuit(1)
    circuit.x_gate(0)
    circuit.measure_all()
    # circuit.draw_circuit(provider=providers.GOOGLE_PROVIDER)
    print(circuit.execute(provider=providers.IBM_PROVIDER, repetitions=10,
                          api=constants.IBM_API, device=constants.IBM_DEVICE_NAME))


def test_demo():
    a = [0, 1, 2]
    b = [3, 4, 5]
    qc = QCircuit(6)
    qc.x_gate(2)
    qc.x_gate(5)
    #qc.measure(0)
    qc.measure(2)
    #qc.measure_all()
    """for i in range(6):
        qc.measure(i)"""
    qc.draw_circuit(provider=providers.IBM_PROVIDER)

if __name__ == '__main__':
    test_demo()