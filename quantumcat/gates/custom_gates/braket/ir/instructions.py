from enum import Enum

from quantumcat.gates.custom_gates.braket.ir.shared_models import (
    Angle,
    DoubleControl,
    DoubleTarget,
    MultiTarget,
    SingleControl,
    SingleTarget,
    TwoDimensionalMatrix,
)


class CHGate(SingleControl, SingleTarget):
    """
    Controlled not gate. Also known as the CX gate.

    Attributes:
        type (str): The instruction type. default = "cnot". (type) is optional.
            This should be unique among all instruction types.
        control (int): The control qubit. This is an int >= 0.
        target (int): The target qubit. This is an int >= 0.

    Examples:
         CNot(control=0, target=1)
    """

    class Type(str, Enum):
        ch_gate = "ch_gate"

    type = Type.ch_gate
