from functionsDictionary import function_list
from memory import memory

#writes in memory starting from location
def writeInMemory(contents: list, location: int):
    for i in len(contents):
        memory[location+i] = bytearray(contents[i])

#calls the function for the opcode
def decodeAndExecute(opcode: int):
    function_list[opcode]()

