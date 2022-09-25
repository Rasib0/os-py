
from InstructionSet.Instruction_list import InstructionList
from Storage.Memory import memory, R, flagRegister, pc
from Storage.controllers.flag_controller import CF, ZF, SF, OF

def writeInMemory(path: str, location: int): #writes in memory starting from location
    with open(path) as f:
        byteString = f.read().split()
    for i in range(len(byteString)):
        memory[location+i] = int(byteString[i])

def decode(): #decode the opcode
    opcode = memory[pc.getInt()]
    pc.inc()
    print("Opcode: ", opcode)
    return opcode

def execute(opcode: int): #calls the function for the opcode and returns if an interrupt occurred during the execution
    interrupt = InstructionList[opcode]()
    return interrupt

def displayMemory(): #Display all the registers as a formated string
    gString = "General purpose registers:\n"
    sString = "Special purpose registers:\n"

    for i in range(0, 16):
        gString += R[i].getHex() + " "
    for i in range(16, 32):
        sString += R[i].getHex() + " "
    
    print(gString)
    print(sString)
    print(flagRegister.getHex())
    print('Flags:', 'CF =', CF(), 'ZF =', ZF(), 'SF =', SF(), 'OF =', OF(), '\n')

