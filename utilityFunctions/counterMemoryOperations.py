import sys
sys.path.append('../OSproject')
from Register import Register
from utilityFunctions.baseConversions import twoBytesToInt
from utilityFunctions.genericCounterOperations import *
from Memory import R


#-----------fetching register and immediate values from memory at PC and updating PC ------------#

def fetchRegisterFromPc() -> Register: #fetches the register in memory currently and updates Pc
    A = R[memoryAtPc()]
    incrementPc()
    return A

def fetchImmediateFromPc() -> int: #fetches the 2 byte immediate value in memory currently and updates Pc
    temp = bytearray(2)
    temp[0]  = memoryAtPc()
    incrementPc()
    temp[1] =  memoryAtPc()
    mem = twoBytesToInt(temp)
    incrementPc()
    return mem

def fetchImmediateFromSc() -> int: #fetches the 2 byte immediate value in stack currently and updates SC
    temp = bytearray(2)
    temp[0]  = memoryAtSc()
    incrementSc()
    temp[1] =  memoryAtSc()
    mem = twoBytesToInt(temp)
    incrementSc()
    return mem
    

#-----------fetching counter and immediate values from stack at SC and updating SC ------------#

def popStackToRegister(R: Register) -> int:
    R.storedBytes[0] = stack[scIntValue()-2]
    R.storedBytes[1] = stack[scIntValue()-1]
    stack[scIntValue()-1] = 0
    stack[scIntValue()-2] = 0
    incrementSc(-2)

def pushRegisterToStack(R: Register):
    stack[scIntValue()] = R.storedBytes[0]
    stack[scIntValue()+1] = R.storedBytes[1]
    incrementSc(2)

def pushPcToSc():
    stack[scIntValue()] = R[19].storedBytes[0]
    stack[scIntValue()+1] = R[19].storedBytes[1]

def returnPcFromSc(): #sets PC to the value of stack at SC
    temp = twoBytesToInt(bytearray([stack[scIntValue()-2],
                                    stack[scIntValue()-1]]))
    incrementSc(-2)
    setPc(temp)
