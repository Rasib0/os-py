import sys
sys.path.append('../OSproject')
from memory import memory, codeRegister, R
from Register import Register
from utils.conversions import twoBytesToInt

#returns the int value of memory at pc
def memoryAtPc():
    return int(memory[pcIntValue()])

#returns the pc value as an int
def pcIntValue():
    return codeRegister['counter'].intValue()

def setPc(value: int):
    codeRegister['counter'].insert(value)
    
#updates PC by the index value
def updatePC(by_index: int):
    codeRegister['counter'].insert(codeRegister['counter'].intValue() + by_index)

#fetches the register in memory currently and updates PC
def currPcRegister() -> Register:
    A = R[memoryAtPc()]
    updatePC(1)
    return A

#fetches the immediate value in memory currently and updates PC
def currPcImmediateValue() -> int:
    temp = bytearray(2)
    temp[0]  = memoryAtPc()
    updatePC(1)
    temp[1] =  memoryAtPc()
    mem = twoBytesToInt(temp)
    updatePC(1)
    return mem

