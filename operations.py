from memory import memory, codeRegister
from utils.conversions import intToTwoBytes
from utils.counter_memory_utils import popStack, pushStack, returnPcFromSc
from operands import registerImmediateOperands, registerRegisterOperands, singleOperands

#------------------Register-register Instructions-------------------#
def mov():
    [A, B] = registerRegisterOperands()

    A.storedBytes = B.storedBytes

def add():
    [A, B] = registerRegisterOperands()

    sum = A.intValue() + B.intValue()
    A.insert(sum) 

def sub():
    [A, B] = registerRegisterOperands()

    sum = A.intValue() - B.intValue()
    A.insert(sum)

#-----------------Register-Immediate Instructions-------------------#

def movi():
    [A, immediate] = registerImmediateOperands()

    A.storedBytes = intToTwoBytes(immediate)

def addi():
    [A, immediate] = registerImmediateOperands()

    sum = A.intValue() + immediate
    A.insert(sum) 

def subi():
    [A, immediate] = registerImmediateOperands()

    sum = A.intValue() - immediate
    A.insert(sum)

#-----------Memory Instructions using immediate offset-------------#
def movl():
    [A, immediate] = registerImmediateOperands()

    A.storedBytes[0] = memory[immediate]
    A.storedBytes[1] = memory[immediate+1]


def movs():
    [A, immediate] = registerImmediateOperands()

    memory[immediate] = A.storedBytes[0]
    memory[immediate+1] = A.storedBytes[1]


#-----------Single Operand Instructions-----------------#
def shl():
    A = singleOperands()
    A.insert(A.intValue() << 1)
def shr():
    A = singleOperands()
    A.insert(A.intValue() >> 1)

def rtl():
    A = singleOperands()
    x = A.intValue()
    A.insert(0x8000 | x >> 1 if x & 0x1 != 0 else x >> 1)

def rtr():
    A = singleOperands()
    x = (0x1 | x << 1) & 0xFFFF if x & 0x8000 != 0 else (x << 1) & 0xFFFF
    A.insert(x)

def inc():
    A = singleOperands()
    A.insert(A.intValue() + 1)


def dec():
    A = singleOperands()
    A.insert(A.intValue() - 1)


def push():
    A = singleOperands()
    pushStack(A)

def pop():
    A = singleOperands()
    popStack(A)


#---------------No Operand Instructions-----------------#
def return_():
    returnPcFromSc()

def noop():
    pass

def end():
    pass
    
