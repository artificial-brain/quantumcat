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


class CCRCA:
    def __init__(self, circuit, arglist):
        super(CCRCA, self).__init__()
        # subcircuit defined for the controlled-controlled ripple-carry adder for 3 bits
        # (the sum is stored by overwriting the values of x)
        self.arglist = arglist
        self.sc = circuit
        self.sw = [self.arglist[0]]                                         # control qubits
        self.sa = [self.arglist[1], self.arglist[2], self.arglist[3]]       # ancilla qubits
        self.ss = [self.arglist[4]]                                         # carry 
        self.sx = [self.arglist[5], self.arglist[6], self.arglist[7]]       # summand x 
        self.sy = [self.arglist[8], self.arglist[9], self.arglist[10]]      # summand y


        self.sc.cx_gate(self.sw[0],self.sa[0])
        
        self.sc.ccx_gate(self.sa[0],self.sy[2],self.sx[2])
        self.sc.ccx_gate(self.sa[0],self.sy[2],self.ss[0])
        self.sc.ccx_gate(self.sa[0],self.ss[0],self.sa[1])
        self.sc.ccx_gate(self.sa[1],self.sx[2],self.sa[2])
        self.sc.ccx_gate(self.sa[1],self.sa[2],self.sy[2])
        # uncompute
        self.sc.ccx_gate(self.sa[1],self.sx[2],self.sa[2])
        self.sc.ccx_gate(self.sa[0],self.ss[0],self.sa[1])

        self.sc.ccx_gate(self.sa[0],self.sy[1],self.sx[1])
        self.sc.ccx_gate(self.sa[0],self.sy[1],self.sy[2])
        self.sc.ccx_gate(self.sa[0],self.sy[2],self.sa[1])
        self.sc.ccx_gate(self.sa[1],self.sx[1],self.sa[2])
        self.sc.ccx_gate(self.sa[1],self.sa[2],self.sy[1])
        # uncompute
        self.sc.ccx_gate(self.sa[1],self.sx[1],self.sa[2])
        self.sc.ccx_gate(self.sa[0],self.sy[2],self.sa[1])

        self.sc.ccx_gate(self.sa[0],self.sy[0],self.sx[0])
        self.sc.ccx_gate(self.sa[0],self.sy[0],self.sy[1])
        self.sc.ccx_gate(self.sa[0],self.sy[1],self.sa[1])
        self.sc.ccx_gate(self.sa[1],self.sx[0],self.sa[2])
        self.sc.ccx_gate(self.sa[1],self.sa[2],self.sy[0])
        # uncompute
        self.sc.ccx_gate(self.sa[1],self.sx[0],self.sa[2])
        self.sc.ccx_gate(self.sa[0],self.sy[1],self.sa[1])

        self.sc.ccx_gate(self.sa[0],self.sy[1],self.sa[1])
        self.sc.ccx_gate(self.sa[1],self.sx[0],self.sa[2])
        self.sc.ccx_gate(self.sa[1],self.sa[2],self.sy[0])
        # uncompute
        self.sc.ccx_gate(self.sa[1],self.sx[0],self.sa[2])
        self.sc.ccx_gate(self.sa[0],self.sy[1],self.sa[1])
        # continue
        self.sc.ccx_gate(self.sa[0],self.sy[0],self.sy[1])
        self.sc.ccx_gate(self.sa[0],self.sy[1],self.sx[0])

        self.sc.ccx_gate(self.sa[0],self.sy[2],self.sa[1])
        self.sc.ccx_gate(self.sa[1],self.sx[1],self.sa[2])
        self.sc.ccx_gate(self.sa[1],self.sa[2],self.sy[1])
        # uncompute
        self.sc.ccx_gate(self.sa[1],self.sx[1],self.sa[2])
        self.sc.ccx_gate(self.sa[0],self.sy[2],self.sa[1])
        # continue
        self.sc.ccx_gate(self.sa[0],self.sy[1],self.sy[2])
        self.sc.ccx_gate(self.sa[0],self.sy[2],self.sx[1])

        self.sc.ccx_gate(self.sa[0],self.ss[0],self.sa[1])
        self.sc.ccx_gate(self.sa[1],self.sx[2],self.sa[2])
        self.sc.ccx_gate(self.sa[1],self.sa[2],self.sy[2])
        # uncompute
        self.sc.ccx_gate(self.sa[1],self.sx[2],self.sa[2])
        self.sc.ccx_gate(self.sa[0],self.ss[0],self.sa[1])
        # continue
        self.sc.ccx_gate(self.sa[0],self.sy[2],self.ss[0])
        self.sc.ccx_gate(self.sa[0],self.ss[0],self.sx[2])

        self.sc.cx_gate(self.sw[0],self.sa[0])

        return