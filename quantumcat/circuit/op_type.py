from enum import Enum


class OpType(Enum):
    """docstring for OpType."""

    x_gate = 1
    y_gate = 2
    z_gate = 3
    measure = 100
