import sys
sys.path.append('../OSproject')
from InstructionSet.InstructionList import InstructionList
from utilityFunctions.genericCounterOperations import memoryAtPc, updatePc
from Memory import memory, R, flagRegister
from utilityFunctions.FlagOperations import CF, ZF, SF, OF

def decode(): #decode the opcode
    opcode = memoryAtPc()
    updatePc()
    return opcode

def execute(opcode: int): #calls the function for the opcode
    InstructionList[opcode]()

def writeInMemory(contents: list, location: int): #writes in memory starting from location
    for i in range(len(contents)):
        memory[location+i] = int(contents[i])

def displayMemory(): #Display all the registers as a formated string
    gString = "General purpose registers:\n"
    sString = "Special purpose registers:\n"

    for i in range(0, 16):
        gString += R[i].hexString() + " "
    for i in range(16, 32):
        sString += R[i].hexString() + " "
    
    print(gString)
    print(sString)
    print(flagRegister.hexString())
    print('Flags:', 'CF =', CF(), 'ZF =', ZF(), 'SF =', SF(), 'OF =', OF(), '\n')

