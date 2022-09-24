import sys
sys.path.append('../OSproject')
from Memory import memory
from utilityFunctions.baseConversions import intToTwoBytes
from utilityFunctions.counterMemoryOperations import popStack, pushStack, returnPcFromSc
from InstructionSet.getInstructionOperands import getRegisterImmediateOperands, getRegisterRegisterOperands, getSingleOperand

#------------------Register-register Instructions-------------------#
def mov():
    [A, B] = getRegisterRegisterOperands()

    A.storedBytes = B.storedBytes

def add():
    [A, B] = getRegisterRegisterOperands()

    sum = A.intValue() + B.intValue()
    A.insert(sum) 

def sub():
    [A, B] = getRegisterRegisterOperands()

    sum = A.intValue() - B.intValue()
    A.insert(sum)

#-----------------Register-Immediate Instructions-------------------#

def movi():
    [A, immediate] = getRegisterImmediateOperands()

    A.storedBytes = intToTwoBytes(immediate)

def addi():
    [A, immediate] = getRegisterImmediateOperands()

    sum = A.intValue() + immediate
    A.insert(sum) 

def subi():
    [A, immediate] = getRegisterImmediateOperands()

    sum = A.intValue() - immediate
    A.insert(sum)

#-----------Memory Instructions using immediate offset-------------#
def movl():
    [A, immediate] = getRegisterImmediateOperands()

    A.storedBytes[0] = memory[immediate]
    A.storedBytes[1] = memory[immediate+1]


def movs():
    [A, immediate] = getRegisterImmediateOperands()

    memory[immediate] = A.storedBytes[0]
    memory[immediate+1] = A.storedBytes[1]


#-----------Single Operand Instructions-----------------#
def shl():
    A = getSingleOperand()
    A.insert(A.intValue() << 1)
def shr():
    A = getSingleOperand()
    A.insert(A.intValue() >> 1)

def rtl():
    A = getSingleOperand()
    x = A.intValue()
    A.insert(0x8000 | x >> 1 if x & 0x1 != 0 else x >> 1)

def rtr():
    A = getSingleOperand()
    x = (0x1 | x << 1) & 0xFFFF if x & 0x8000 != 0 else (x << 1) & 0xFFFF
    A.insert(x)

def inc():
    A = getSingleOperand()
    A.insert(A.intValue() + 1)


def dec():
    A = getSingleOperand()
    A.insert(A.intValue() - 1)


def push():
    A = getSingleOperand()
    pushStack(A)

def pop():
    A = getSingleOperand()
    popStack(A)


#---------------No Operand Instructions-----------------#
def return_():
    returnPcFromSc()

def noop():
    pass

def end():
    pass
    

