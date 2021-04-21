from quantumcat.gates.custom_gates.cirq import RXXGate,RXGate,RCCXGate,RC3XGate,RGate,CYGate,PGate


def is_custom_class(obj):
    if isinstance(obj, RXXGate) or isinstance(obj,RXGate) or isinstance(obj,RCCXGate) or isinstance(obj,RC3XGate) or isinstance(obj,RGate) or isinstance(obj,CYGate) or isinstance(obj,PGate):
        return True
    else:
        return False