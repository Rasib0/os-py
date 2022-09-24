import sys
sys.path.append('../OSproject')
from operation_dict import operations_list
from utils.pc_utils import memoryAtPc, updatePC
from memory import *
from utils.flag_utils import CF, ZF, SF, OF

def decode():
    opcode = memoryAtPc()
    updatePC(1)
    return opcode

#calls the function for the opcode
def execute(opcode: int):
    operations_list[opcode]()

#writes in memory starting from location
def writeInMemory(contents: list, location: int):
    for i in range(len(contents)):
        memory[location+i] = int(contents[i])

#Display all the registers as a formated string
def displayMemory():
    gString = "General purpose registers:\n"
    sString = "Special purpose registers:\n"

    for i in range(0, 16):
        gString += R[i].hexString() + " "
    for i in range(16, 32):
        sString += R[i].hexString() + " "
    
    print(gString)
    print(sString)
    print(flagRegister.hexString())
    print('Flags:', 'CF =', CF(), 'ZF =', ZF(), 'SF =', SF(), 'OF =', OF())

