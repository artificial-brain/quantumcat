from enum import Enum


class OpType(Enum):
    """docstring for OpType."""

    x_gate = 1
    y_gate = 2
    z_gate = 3
    cx_gate = 4
    ccx_gate = 5
    mct_gate = 6
    rzz_gate = 42
    rzx_gate = 43
    ecr_gate = 44
    s_gate = 45
    sdg_gate = 46
    swap_gate = 47
    iswap_gate = 48
    sx_gate = 49
    sxd_gate = 50
    t_gate = 51
    td_gate = 52
    u_gate = 53
    u1_gate = 54
    u2_gate = 55
    u3_gate = 56
    measure = 100
