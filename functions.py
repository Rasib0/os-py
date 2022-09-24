from memory import R
from utils.conversions import intToTwoBytes
from utils.systemOperations import currPcImmediateValue, currPcRegister

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
#Memory Instructions

#Single Operand Instructions

#No Operand Instructions

#Operands
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

