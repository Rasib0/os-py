import sys
sys.path.append('../OSproject')
from utilityFunctions.FlagOperations import *
from utilityFunctions.genericCounterOperations import setPc
from utilityFunctions.counterMemoryOperations import popStackToRegister, pushRegisterToStack, returnPcFromSc, pushPcToSc, fetchImmediateFromPc, fetchRegisterFromPc
from InstructionSet.getInstructionOperands import getRegisterImmediateOperands, getRegisterRegisterOperands, getSingleImmediateOperand, getSingleRegisterOperand
from Memory import memory

#------------------Register-register Instructions-------------------#
def mov():
    [A, B] = getRegisterRegisterOperands()

    A.storedBytes = B.storedBytes

def add():
    [A, B] = getRegisterRegisterOperands()

    sum = A.intValue() + B.intValue()
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), B.intValue())
    A.insert(sum) 
    

def sub():
    [A, B] = getRegisterRegisterOperands()

    sum = A.intValue() - B.intValue()
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), B.intValue())
    A.insert(sum)

def mul():
    [A, B] = getRegisterRegisterOperands()
    sum = A.intValue() * B.intValue()
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), B.intValue())
    A.insert(sum)

def div():
    [A, B] = getRegisterRegisterOperands()
    sum = A.intValue() / B.intValue()
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), B.intValue())
    A.insert(sum)

def and_():
    [A, B] = getRegisterRegisterOperands()
    sum = A.intValue() & B.intValue()
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), B.intValue())
    A.insert(sum)

def or_():
    [A, B] = getRegisterRegisterOperands()
    sum = A.intValue() | B.intValue()
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), B.intValue())
    A.insert(sum)

#------------------Register-Immediate Instructions------------------#

def movi():
    [A, immediate] = getRegisterImmediateOperands()
    A.insert(immediate)

def addi():
    [A, immediate] = getRegisterImmediateOperands()

    sum = A.intValue() + immediate
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), immediate)
    A.insert(sum) 

def subi():
    [A, immediate] = getRegisterImmediateOperands()

    sum = A.intValue() - immediate
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), immediate)
    A.insert(sum)

def muli():
    [A, immediate] = getRegisterImmediateOperands()
    
    sum = A.intValue() - immediate
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), immediate)
    A.insert(sum)

def divi():
    [A, immediate] = getRegisterImmediateOperands()
    
    sum = A.intValue() - immediate
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), immediate)
    A.insert(sum)

def andi():
    [A, immediate] = getRegisterImmediateOperands()

    sum = A.intValue() - immediate
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), immediate)
    A.insert(sum)

def ori():
    [A, immediate] = getRegisterImmediateOperands()

    sum = A.intValue() - immediate
    sum = sum & 0xFFFF
    ArithmeticLogicalFlagTest(sum, A.intValue(), immediate)
    A.insert(sum)


def bz():
    offset = getSingleImmediateOperand()
    if(ZF() == 1): setPc(offset)

def bnz():
    offset = getSingleImmediateOperand()
    if(ZF() == 0): setPc(offset)

def bc():
    offset = getSingleImmediateOperand()
    if(CF() == 1): setPc(offset)

def bs():
    offset = getSingleImmediateOperand()
    if(SF() == 1): setPc(offset)

def jmp():
    offset = getSingleImmediateOperand()
    setPc(offset)

def call():
    offset = getSingleImmediateOperand()
    pushPcToSc()
    setPc(offset)

def act():
    pass

#-----------Memory Instructions using immediate offset-------------#
def movl():
    [A, immediate] = getRegisterImmediateOperands()

    A.storedBytes[0] = memory[immediate]
    A.storedBytes[1] = memory[immediate+1]


def movs():
    [A, immediate] = getRegisterImmediateOperands()

    memory[immediate] = A.storedBytes[0]
    memory[immediate+1] = A.storedBytes[1]


#------------------Single Operand Instructions-----------------#
def shl():
    A = getSingleRegisterOperand()
    x = A.intValue()
    result = x << 1
    A.insert(result)
    shiftRotateFlagTest(x, result)

def shr():
    A = getSingleRegisterOperand()
    x = A.intValue()
    result = x >> 1
    A.insert(result)
    shiftRotateFlagTest(x, result)

def rtl():
    A = getSingleRegisterOperand()
    x = A.intValue()
    result = 0x8000 | x >> 1 if x & 0x1 != 0 else x >> 1
    A.insert(result)
    shiftRotateFlagTest(x, result)

def rtr():
    A = getSingleRegisterOperand()
    x = A.intValue()
    result = (0x1 | x << 1) & 0xFFFF if x & 0x8000 != 0 else (x << 1) & 0xFFFF
    A.insert(result)
    shiftRotateFlagTest(x, result)

def inc():
    A = getSingleRegisterOperand()

    A.insert(A.intValue() + 1)


def dec():
    A = getSingleRegisterOperand()

    A.insert(A.intValue() - 1)

def push():
    A = getSingleRegisterOperand()
    pushRegisterToStack(A)

def pop():
    A = getSingleRegisterOperand()
    popStackToRegister(A)

#----------------No Operand Instructions-----------------#
def return_():
    returnPcFromSc()

def noop():
    pass

def end():
    pass
    


#----------------fetching the operands-------------------#

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