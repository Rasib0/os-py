from memory import memory
from utils.conversions import intToTwoBytes
from utils.register_utils import registerImmediateOperands, registerRegisterOperands

#Register-register Instructions
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

#Register-Immediate Instructions
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
#Memory Instructions using immediate offset
def movl():
    [A, immediate] = registerImmediateOperands()
    A.storedBytes[0] = memory[immediate]
    A.storedBytes[1] = memory[immediate+1]


def movs():
    [A, immediate] = registerImmediateOperands()
    memory[immediate] = A.storedBytes[0]
    memory[immediate+1] = A.storedBytes[1]


#Single Operand Instructions

#No Operand Instructions

