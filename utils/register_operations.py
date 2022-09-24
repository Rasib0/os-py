import sys
sys.path.append('../OSproject')
from utils.pc_operations import currPcImmediateValue, currPcRegister

#return Operands
def registerRegisterOperands():
    A = currPcRegister()
    B = currPcRegister()
    return [A, B]

def registerImmediateOperands():
    A = currPcRegister()
    mem = currPcImmediateValue()
    return [A, mem]
    
def singleOperands():
    A = currPcRegister()
    return A