import sys
sys.path.append('../OSproject')
from functionsDictionary import function_list
from utils.pc_operations import memoryAtPc, updatePC
from memory import memory, codeRegister, stackRegister, dataRegister, R

#writes in memory starting from location
def writeInMemory(contents: list, location: int):
    for i in range(len(contents)):
        memory[location+i] = int(contents[i])

#Display all the registers as a formated string
def displayMemory():
    gString = "General purpose registers:\n"
    for r in R:
        gString += r.hexString() + " "

    sString = "Special purpose registers:\n"
    for r in codeRegister:
        sString += codeRegister[r].hexString() + " "
    
    for r in stackRegister:
        sString += stackRegister[r].hexString() + " "

    for r in dataRegister:
        sString += dataRegister[r].hexString() + " "
    print(gString)
    print(sString)

#calls the function for the opcode
def decode():
    opcode = memoryAtPc()
    updatePC(1)
    return opcode
    
def execute(opcode: int):
    function_list[opcode]()

