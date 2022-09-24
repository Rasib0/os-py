import sys
sys.path.append('../OSproject')
from Register import Register
from utils.conversions import twoBytesToInt
from utils.counter_utils import *
from memory  import R


#-----------fetching register and immediate values from memory at PC and updating PC ------------#

def currPcRegister() -> Register: #fetches the register in memory currently and updates Pc
    A = R[memoryAtPc()]
    updatePc()
    return A

def currPcImmediateValue() -> int: #fetches the 2 byte immediate value in memory currently and updates Pc
    temp = bytearray(2)
    temp[0]  = memoryAtPc()
    updatePc()
    temp[1] =  memoryAtPc()
    mem = twoBytesToInt(temp)
    updatePc()
    return mem

def currScImmediateValue() -> int: #fetches the 2 byte immediate value in stack currently and updates SC
    temp = bytearray(2)
    temp[0]  = memoryAtSc()
    updateSc()
    temp[1] =  memoryAtSc()
    mem = twoBytesToInt(temp)
    updateSc()
    return mem


#-----------fetching counter and immediate values from stack at SC and updating SC ------------#


def popStack(R: Register) -> int:
    R.storedBytes[1] = stack[scIntValue()-1]
    R.storedBytes[0] = stack[scIntValue()-2]
    stack[scIntValue()-1] = 0
    stack[scIntValue()-2] = 0
    updateSc(-2)

def pushStack(R: Register):
    stack[scIntValue()] = R.storedBytes[0]
    stack[scIntValue()+1] = R.storedBytes[1]
    updateSc(2)

def returnPcFromSc(): #sets PC to the value of stack at SC
    temp = twoBytesToInt(bytearray([stack[scIntValue()-1],
                                    stack[scIntValue()-2]]))
    updateSc(-2)
    setPc(temp)

