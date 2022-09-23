from memory import *
from utils.conversions import twoBytesToInt
from utils.systemOperations import decodeAndExecute, writeInMemory

#fetch the byte stream 
with open('p1.txt') as f:
    byteString = f.read().split()

memoryIndex = twoBytesToInt(dataRegister['counter'].storedBytes)  #Assuming dataRegister['counter'] holds the memory address which is currently 0
writeInMemory(byteString, memoryIndex)
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

















    