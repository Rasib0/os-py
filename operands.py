#return Operands register
from utils.counter_memory_utils import currPcImmediateValue, currPcRegister

#returns 2 registers and updates PC
def registerRegisterOperands():
    A = currPcRegister()
    B = currPcRegister()
    return [A, B]

#returns 1 registers and 1 immediate value and updates PC
def registerImmediateOperands():
    A = currPcRegister()
    mem = currPcImmediateValue()
    return [A, mem]

#returns 1 immediate value and updates PC
def singleOperands():
    A = currPcRegister()
    return A