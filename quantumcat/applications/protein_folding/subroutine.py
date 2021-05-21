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

class Subroutine:
    """
    Subroutines for finding best conformation
    """

    def __init__(self, x, y, z, w, a, c, e, anc):
        super(Subroutine, self).__init__()

        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.a = a
        self.c = c
        self.e = e
        self.anc = anc

        print(self.anc)

    def subroutine01(self, circuit, length):
        pass

    def subroutine02(self):
        pass

    def subroutine03(self):
        pass