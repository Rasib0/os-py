import sys
from xmlrpc.client import boolean
sys.path.append('../OSproject')
from Memory import flagRegister

def checkBit(num: int, position: int) -> int:
   return (num >> position) & 1

def CF():
    return checkBit(flagRegister.intValue(), 0)
def ZF():
    return checkBit(flagRegister.intValue(), 1)
def SF():
    return checkBit(flagRegister.intValue(), 2)
def OF():
    return checkBit(flagRegister.intValue(), 3)

#set flags
def setCF():
    flagRegister.insert(flagRegister.intValue() | 0x1)

def setZF():
    flagRegister.insert(flagRegister.intValue() | 0x2)

def setSF():
    flagRegister.insert(flagRegister.intValue() | 0x4)

def setOF():
    flagRegister.insert(flagRegister.intValue() | 0x8)

#clear flags
def clearCF():
    flagRegister.insert(flagRegister.intValue() & 0xFFFE)

def clearZF():
    flagRegister.insert(flagRegister.intValue() & 0xFFFD)

def clearSF():
    flagRegister.insert(flagRegister.intValue() & 0xFFFB)

def clearOF():
    flagRegister.insert(flagRegister.intValue() & 0xFFF7)


def ArithmeticLogicalFlagTest(sum: int, num1: int, num2: int):
    if(sum == 0): setZF() #when the results is 0
    if(sum > 0x8000): setSF() #when the most significant bit is 1
    if((num1^sum)&(num2^sum)&0x8000): setOF() #when sign of both inputs is different from the sign of the result

def shiftRotateFlagTest(before: int, after: int): 
    if(after == 0): setZF() #when the results is 0
    if(before > 0x8000): setCF() #when the most significant bit is 1 before operation
    if(after > 0x8000): setSF() #when the most significant bit is 1 after operation
    pass



