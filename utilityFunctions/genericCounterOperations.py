import sys
sys.path.append('../OSproject')
from Memory import memory, stack, codeRegister, stackRegister

#----------- PC and memory utility ------------#

def memoryAtPc(): #returns the int value of memory at pc
    return int(memory[pcIntValue()])

def pcIntValue(): #returns the pc value as an int
    return codeRegister['counter'].intValue()

def setPc(value: int): #set the PC to the int value
    codeRegister['counter'].insert(value)
    
def updatePc(by_index: int = 1): #updates PC by the index value
    codeRegister['counter'].insert(pcIntValue() + by_index)


#----------- SC and memory utility ------------#

def memoryAtSc():
    return int(stack[scIntValue()])

def scIntValue():
    return stackRegister['counter'].intValue()

def setSc(value: int):
    stackRegister['counter'].insert(value)
    
def updateSc(by_index: int = 1): #updates SC by the index value
    stackRegister['counter'].insert(scIntValue() + by_index)


