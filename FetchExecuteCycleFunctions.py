import string
import sys
sys.path.append('../OSproject')
from InstructionSet.Instruction_list import InstructionList
from utilityFunctions.counter_operations import incPc, pc
from Memory import memory, R, flagRegister
from utilityFunctions.flag_operations import CF, ZF, SF, OF



def fetch():
    pass

def decode(): #decode the opcode
    opcode = memory[pc()]
    incPc()
    print("Opcode: ", opcode)
    return opcode

def execute(opcode: int): #calls the function for the opcode
    error = InstructionList[opcode]()
    return error

def writeInMemory(path: string, location: int): #writes in memory starting from location
    with open('p1.txt') as f:
        byteString = f.read().split()
    for i in range(len(byteString)):
        memory[location+i] = int(byteString[i])

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

