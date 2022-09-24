#return Operands register
from utilityFunctions.counterMemoryOperations import fetchImmediateFromPc, fetchRegisterFromPc

#returns 2 registers and updates PC
def getRegisterRegisterOperands():
    A = fetchRegisterFromPc()
    B = fetchRegisterFromPc()
    return [A, B]

#returns 1 registers and 1 immediate value and updates PC
def getRegisterImmediateOperands():
    A = fetchRegisterFromPc()
    mem = fetchImmediateFromPc()
    return [A, mem]

#returns 1 register and updates PC
def getSingleRegisterOperand():
    A = fetchRegisterFromPc()
    return A

#returns 1 immediate value and updates PC
def getSingleImmediateOperand():
    mem = fetchImmediateFromPc()
    return mem