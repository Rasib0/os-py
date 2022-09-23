from operator import truediv
from functionsDictionary import function_list
from memory import *

#TBD the structure of this file

def writeInMemory(contents: list):
    # i assume this register holds the memory address
    memoryIndex = dataRegister['counter']
    for i in len(contents):
        memory[memoryIndex+i] = bytearray(contents[i])


def decode(index: int):
    return int(index)

def execute(opcode: int):
    function_list[opcode]()

with open('p1.txt') as f:
    contents = f.read().split() #array of all the bytes. We can do this line by line as well
    
#First we check if the byte is a opcode, then
nextByte = 1
#tbd
for byteStr in contents:
    opcode = decode()
    execute(opcode)











    