from memory import *
from utils.conversions import twoBytesToInt, intToTwoBytes

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
    A.storedBytes = immediate

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

#fetches the register in memory currently and updates PC
def currPcRegister() -> Register:
    A = R[pcMemValue()]
    updatePC(1)
    return A

#fetches the immediate value in memory currently and updates PC
def currPcImmediateValue() -> int:
    temp = bytearray(2)
    temp[0]  = pcMemValue()
    updatePC(1)
    temp[1] =  pcMemValue()
    mem = twoBytesToInt(temp)
    updatePC(1)
    return mem

def pcMemValue():
    return int(memory[codeRegister['count'].intValue])

def updatePC(by_index: int):
    codeRegister['counter'] = codeRegister['counter'] + by_index
