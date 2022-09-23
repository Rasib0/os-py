from memory import Register, memory, codeRegister
from utils.conversions import twoBytesToInt, intToTwoBytes

#Register-register Instructions
def mov(A: Register, B: Register):
    A.storedBytes = B.storedBytes
    updatePC(3)

def add(A: Register, B: Register):
    sum = A.intValue() + B.intValue()
    A.insert(sum) 
    updatePC(4)

def sub(A: Register, B: Register):
    sum = A.intValue() - B.intValue()
    A.insert(sum)
    updatePC(4)

#Register-Immediate Instructions
def movi(A: Register, immediate: bytearray):
    A.storedBytes = immediate

def addi(A: Register, immediate: bytearray):
    sum = A.intValue() + twoBytesToInt(immediate)
    A.insert(sum) 
    updatePC(4)

def subi(A: Register, immediate: bytearray):
    sum = A.intValue() - twoBytesToInt(immediate)
    A.insert(sum)
    updatePC(4)
#Memory Instructions

#Single Operand Instructions

#No Operand Instructions

#utility
def updatePC(by_index: int):
    codeRegister['counter'] = codeRegister['counter'] + by_index
