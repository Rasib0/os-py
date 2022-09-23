import sys
sys.path.append('../OSproject')
from memory import memory, codeRegister

#writes in memory starting from location
def writeInMemory(contents: list, location: int):
    for i in range(len(contents)):
        memory[location+i] = int(contents[i])




#returns the int value of memory at pc
def memoryAtPc():
    return int(memory[pcIntValue()])

#returns the pc value as an int
def pcIntValue():
    return codeRegister['counter'].intValue()

#updates PC by the index value
def updatePC(by_index: int):
    codeRegister['counter'].insert(codeRegister['counter'].intValue() + by_index)
