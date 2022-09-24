from memory import *
from utils.pc_operations import setPc
from utils.execution_operations import  decode, displayMemory, writeInMemory,  execute

#fetch the byte stream 
with open('p1-test.txt') as f:
    byteString = f.read().split()

memoryIndex = 0
writeInMemory(byteString, memoryIndex)
setPc(memoryIndex)

#the execution loop
def start():
    while(True):
        opcode = decode()

        if(opcode == 243): #break the execution loop at opcode for END
            print("END OF PROCESS.")
            break
    
        execute(opcode)
        displayMemory()
        print()

start()
















    