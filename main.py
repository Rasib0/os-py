from functions import updatePC
from memory import *
from utils.conversions import twoBytesToInt
from utils.systemOperations import decodeAndExecute, writeInMemory

#fetch the byte stream 
with open('p1-test.txt') as f:
    byteString = f.read().split()

memoryIndex = twoBytesToInt(dataRegister['counter'].storedBytes)  #Assuming dataRegister['counter'] holds the memory address which is currently 0
writeInMemory(byteString, memoryIndex)
codeRegister['counter'].insert(memoryIndex)

#the execution loop
def start():
    while(True):
        opcode = int(memory[codeRegister['counter']])

        if(opcode == 243): #break the execution loop at opcode for END
            break
        print("Opcode: ", opcode)

        updatePC(1) #this should be in decode

        decodeAndExecute(opcode)
        displayMemory()

start()
















    