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
from quantumcat.utils import providers
from quantumcat.applications.protein_folding import CCRCA, CCRCA_INVERSE

class ProteinFolding:

    def __init__(self, sequence):
        super(ProteinFolding, self).__init__()
        self.sequence = sequence

        self.length = 2

        # two's complements: 
        # 0 = 000, 1 = 001, 2 = 010, 3 = 011, -1 = 111, -2 = 110, -3 = 101 
        # (-4 = 100, not needed) 
        # For the purpose of this simplified validation we don't need the fixed 
        # coordinates of the first amino acid which are all 0

        # quantum register holding the x coordinates for x1, x2 etc. (x0 = 000 omitted)
        self.x = [0, 1, 2]
        # quantum register holding the y coordinates for y1, y2 etc. (y0 = 000 omitted)
        self.y = [3, 4, 5]
        # quantum register holding the y coordinates for z1, z2 etc. (z0 = 000 omitted)
        self.z = [6, 7, 8]
        # quantum register holding the controls w0, w1, etc.
        self.w = [9, 10, 11]
        # register holding the binary 1 (3 qubits)
        self.a = [12, 13, 14]

        # register holding the two's complement of 1 (3 qubits) not needed, 
        # can be replaced by a with the first 2 qubits negated.

        # register holding the carry bit for ripple-carry adder
        self.c = [15]
        # quantum register that holds the energy value for each conformation: if first and 
        # last amino acid are located diagonally # from each other, e = 1, otherwise e = 0. 
        # There are 4 conformations for which e = 1.
        self.e = [16]
        # ancilla qubits, at most three needed for the ccrca function
        self.anc = [17, 18, 19]
        
        self.circuit = QCircuit(20) 

        # encoding binary 1
        self.circuit.x_gate(self.a[2])
        # encoding the two's complement of 1
        #qc.x(t[0:length])

        # setting the state into superposition
        #qc.h_gate(w[0:3])
        
        for i in range(len(self.w)):
            self.circuit.h_gate(self.w[i])

        # setting energy qubit e into superposition on par with |w>
        self.circuit.h_gate(self.e[0])


        # global variable used in Subroutine 1 to navigate among the values of vector w
        self.b = 0
        self.arglist = []

        # Subroutine 1: Generating conformational space

        for d in range (2,self.length+1):
                        
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            # if w[0]=1 then x+1, if w[0]=0 then x-1
            self.arglist.append(self.w[self.b])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            #range [0,1,2] for d=2, range [3,4,5] for d=3
            for i in range(0,3): 
                self.arglist.append(self.x[i])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            #print(arglist)
            CCRCA(self.circuit, self.arglist)
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.circuit.x_gate(self.w[self.b])
            self.arglist.append(self.w[self.b])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            for i in range(0,3): 
                self.arglist.append(self.x[i])
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA(self.circuit, self.arglist)
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            self.circuit.x_gate(self.w[self.b])
            
            
            # if w[1]=1 then y+1, if w[1]=0 then y-1
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.arglist.append(self.w[self.b+1])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            #range [0,1,2] for d=2, range [3,4,5] for d=3
            for i in range(0,3): 
                self.arglist.append(self.y[i])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA(self.circuit, self.arglist)
            
            
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.circuit.x_gate(self.w[self.b+1])
            self.arglist.append(self.w[self.b+1])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            for i in range(0,3): 
                self.arglist.append(self.y[i])
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA(self.circuit, self.arglist)
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            self.circuit.x_gate(self.w[self.b+1])
            
            
            
            
            # if w[2]=1 then z+1, if w[2]=0 then z-1
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.arglist.append(self.w[self.b+2])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            #range [0,1,2] for d=2, range [3,4,5] for d=3
            for i in range(0,3): 
                self.arglist.append(self.z[i])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA(self.circuit, self.arglist)
            
            
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.circuit.x_gate(self.w[self.b+2])
            self.arglist.append(self.w[self.b+2])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            for i in range(0,3): 
                self.arglist.append(self.z[i])
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA(self.circuit, self.arglist)
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            self.circuit.x_gate(self.w[self.b+2])
            
            #b = b+3
            
        # Subroutine 2: Finding an arbitrary conformation, e.g. |w>=|110> which is 
        # a transition downwards out of the page. 
        # There are a total of 8 conformations for a sequence of length L=2.
        # For this conformation, the energy value will be |e>=|1>, otherwise it will be |0>. 
        self.circuit.h_gate(self.e[0])
        self.circuit.x_gate(self.w[2])
        self.circuit.ccx_gate(self.w[0],self.w[1],self.anc[0])
        self.circuit.ccx_gate(self.anc[0],self.w[2],self.e[0])

        # uncomputing

        self.circuit.ccx_gate(self.w[0],self.w[1],self.anc[0])
        self.circuit.x_gate(self.w[2])
        self.circuit.h_gate(self.e[0])



        # Subroutine 3: Uncomputation of coordinates by running Subroutine 1 in reverse
        self.b = 0

        for d in range (self.length,1,-1):
            
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            
            # if w[0]=1 then x+1, if w[0]=0 then x-1
            self.arglist.append(self.w[self.b])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            #range [0,1,2] for d=2, range [3,4,5] for d=3
            for i in range(0,3): 
                self.arglist.append(self.x[i])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA_INVERSE(self.circuit, self.arglist)
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.circuit.x_gate(self.w[self.b])
            self.arglist.append(self.w[self.b])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            for i in range(0,3): 
                self.arglist.append(self.x[i])
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA_INVERSE(self.circuit, self.arglist)
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            self.circuit.x_gate(self.w[self.b])
            
            
            # if w[1]=1 then y+a, if w[1]=0 then y-a
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.arglist.append(self.w[self.b+1])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            #range [0,1,2] for d=2, range [3,4,5] for d=3
            for i in range(0,3): 
                self.arglist.append(self.y[i])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA_INVERSE(self.circuit, self.arglist)
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.circuit.x_gate(self.w[self.b+1])
            self.arglist.append(self.w[self.b+1])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            for i in range(0,3): 
                self.arglist.append(self.y[i])
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA_INVERSE(self.circuit, self.arglist)
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            self.circuit.x_gate(self.w[self.b+1])
            
            
            
            
            # if w[2]=1 then z+1, if w[2]=0 then z-1
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.arglist.append(self.w[self.b+2])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            #range [0,1,2] for d=2, range [3,4,5] for d=3
            for i in range(0,3): 
                self.arglist.append(self.z[i])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA_INVERSE(self.circuit, self.arglist)
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            self.circuit.x_gate(self.w[self.b+2])
            self.arglist.append(self.w[self.b+2])
            for i in range(0,3):
                self.arglist.append(self.anc[i])
            self.arglist.append(self.c[0])
            for i in range(0,3): 
                self.arglist.append(self.z[i])
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            for i in range(0,3):
                self.arglist.append(self.a[i])
            CCRCA_INVERSE(self.circuit, self.arglist)
            self.circuit.x_gate(self.a[0])
            self.circuit.x_gate(self.a[1])
            self.circuit.x_gate(self.w[self.b+2])
            
            for i in range(len(self.arglist)-1,-1,-1):
                self.arglist.pop(i)
            
            #b = b-3

        return

    def run(self, provider):
        self.provider = provider

        # Subroutine 4: Finding conformation with e = 1 among 8. This can be done with 
        # Grover's search algorithm. Grover diffusion operator has to be executed 
        # pi/4 * sqrt(N/M) where N = 16 (all conformations) and M = 1 (solution). 
        # This is equal to ca. 3. Thus executing the search algorithm three times 
        # suffices to find a solution. 
        # The oracle has to mark the state 110. 


        # Grover's iteration
        for j in range(0,3):
            # the oracle, selects 110 (this oracle is correct, so is the diffusion operator)
            self.circuit.h_gate(self.w[1])
            self.circuit.x_gate(self.w[2])
            self.circuit.ccx_gate(self.w[0],self.w[2],self.anc[0])
            self.circuit.ccx_gate(self.anc[0],self.e[0],self.w[1])
            # uncomputing
            self.circuit.ccx_gate(self.w[0],self.w[2],self.anc[0])
            self.circuit.x_gate(self.w[2])
            self.circuit.h_gate(self.w[1])


            # The diffusion operator
            for i in range(0,3):
                self.circuit.h_gate(self.w[i])
                self.circuit.x_gate(self.w[i])  
            self.circuit.h_gate(self.e[0])
            self.circuit.x_gate(self.e[0])
            
            self.circuit.ccx_gate(self.e[0],self.w[0],self.anc[0])
            self.circuit.h_gate(self.w[2])
            self.circuit.ccx_gate(self.anc[0],self.w[1],self.w[2])

            # uncompute
            self.circuit.h_gate(self.w[2])
            self.circuit.ccx_gate(self.e[0],self.w[0],self.anc[0])
            
            for i in range(0,3):
                self.circuit.x_gate(self.w[i])
                self.circuit.h_gate(self.w[i])  
            self.circuit.x_gate(self.e[0])
            self.circuit.h_gate(self.e[0])

        # Measuring the conformation
        for i in range(0,3): 
            self.circuit.measure(self.w[i])
        
        return self.circuit.execute(provider=self.provider, repetitions=1024)