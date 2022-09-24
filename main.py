from memory import *
from utils.counter_utils import scIntValue, setPc
from utils.execution_functions import  decode, displayMemory, writeInMemory,  execute

#fetch the byte stream 
with open('p1-test.txt') as f:
    byteString = f.read().split()

writeInMemory(byteString, 0)
setPc(0)

#the execution loop

Running = True

def start():
    while(Running):
        opcode = decode()

        if(opcode == 243): #break the execution loop at opcode for END
            print("END OF PROCESS.")
            break

        #print(stack)
        #print(scIntValue())
        print("Opcode: ", opcode)
        execute(opcode)
        #print(stack)
        displayMemory()

start()
















    