from functionsDictionary import function_list
from memory import *
from utils.conversions import twoBytesToInt

#writes in memory starting from location
def writeInMemory(contents: list, location: int):
    for i in len(contents):
        memory[location+i] = bytearray(contents[i])

#calls the function for the opcode
def decodeAndExecute(opcode: int):
    function_list[opcode]()


#fetch the byte stream 
with open('p1.txt') as f:
    byteString = f.read().split()

memoryIndex = twoBytesToInt(dataRegister['counter'].storedBytes)  #I assume dataRegister['counter'] holds the memory address which is currently 0
print(memoryIndex)
#writeInMemory(byteString, memoryIndex)
codeRegister['counter'] = memoryIndex


#the execution loop
def start():
    while(True):
        opcode = int(codeRegister['counter'])

        if(opcode == 243): #break the execution loop at opcode for END
            break
        decodeAndExecute(opcode)
        displayMemory()

displayMemory()

















    