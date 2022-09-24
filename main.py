from memory import *
from utils.conversions import twoBytesToInt
from functionsDictionary import function_list
from utils.systemOperations import memoryAtPc, pcIntValue, writeInMemory, updatePC

#fetch the byte stream 
with open('p1-test.txt') as f:
    byteString = f.read().split()

memoryIndex = twoBytesToInt(dataRegister['counter'].storedBytes)  #Assuming dataRegister['counter'] holds the memory address which is currently 0
writeInMemory(byteString, memoryIndex)
codeRegister['counter'].insert(memoryIndex)

#calls the function for the opcode
def decode():
    opcode = memoryAtPc()
    updatePC(1)
    return opcode

def execute(opcode: int):
    function_list[opcode]()


#the execution loop
def start():
    while(True):
        opcode = decode()
        if(opcode == 243): #break the execution loop at opcode for END
            print("END OF PROCESS. CURRENT PC: ", pcIntValue())
            break
        execute(opcode)
        displayMemory()

start()
















    