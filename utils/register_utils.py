import sys
sys.path.append('../OSproject')
from utils.pc_utils import currPcImmediateValue, currPcRegister

#return Operands register
def registerRegisterOperands():
    A = currPcRegister()
    B = currPcRegister()
    return [A, B]

#returns The register and the 2 byte value next to it.
def registerImmediateOperands():
    A = currPcRegister()
    mem = currPcImmediateValue()
    return [A, mem]

def singleOperands():
    A = currPcRegister()
    return A