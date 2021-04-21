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

from quantumcat.gates.custom_gates.cirq import UGate, U1Gate, U2Gate, U3Gate, SXGate, IGate, RXXGate, SXDGate, SDGGate, SXGate, TDGate


def is_custom_class(obj):
    if isinstance(obj, UGate) or isinstance(obj, U1Gate) or isinstance(obj, U2Gate) or isinstance(obj, U3Gate) or \
            isinstance(obj, SXGate) or isinstance(obj, IGate) or isinstance(obj, RXXGate) or isinstance(obj, SXDGate) or \
            isinstance(obj, SDGGate) or isinstance(obj, SXGate) or isinstance(obj, TDGate):
        return True
    else:
        return False
