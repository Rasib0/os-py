import sys
sys.path.append('../OSproject')
from memory import memory
from functionsDictionary import function_list

#writes in memory starting from location
def writeInMemory(contents: list, location: int):
    for i in range(len(contents)):
        memory[location+i] = int(contents[i])

#calls the function for the opcode
def decodeAndExecute(opcode: int):
    function_list[opcode]()

