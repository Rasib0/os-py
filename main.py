from memory import *
from utils.conversions import twoBytesToInt
from functionsDictionary import function_list
from utils.systemOperations import memoryAtPc, writeInMemory, updatePC

#fetch the byte stream 
with open('p1-test.txt') as f:
    byteString = f.read().split()

memoryIndex = twoBytesToInt(dataRegister['counter'].storedBytes)  #Assuming dataRegister['counter'] holds the memory address which is currently 0
writeInMemory(byteString, memoryIndex)
codeRegister['counter'].insert(memoryIndex)


#calls the function for the opcode
def decodeAndExecute(opcode: int):
    function_list[opcode]()


#the execution loop
def start():
    while(True):
        opcode = memoryAtPc()

        if(opcode == 243): #break the execution loop at opcode for END
            break
        print("Opcode: ", opcode)

        updatePC(1) #this should be in decode

        decodeAndExecute(opcode)
        displayMemory()
start()
















    