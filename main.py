from memory import *
from utils.pc_utils import setPc
from utils.execution_utils import  decode, displayMemory, writeInMemory,  execute

#fetch the byte stream 
with open('p1-test.txt') as f:
    byteString = f.read().split()

writeInMemory(byteString, 0)
setPc(0)

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
















    