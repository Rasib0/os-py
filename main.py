from memory import *
from utils.counter_utils import pcIntValue, scIntValue, setPc
from utils.execution_functions import  decode, displayMemory, writeInMemory,  execute

#fetch the byte stream 
with open('p1-test.txt') as f:
    byteString = f.read().split()

writeInMemory(byteString, 0)
setPc(0)

#the execution loop

Running = True

def start():
    count = 0
    while(Running):
        opcode = decode()
        print("Instruction Number", count)
        count += 1
        if(opcode == 243): #break the execution loop at opcode for END
            print("END OF PROCESS.")
            break
        #print("PC Value: ", pcIntValue())
        #print("SC Value: ", scIntValue())
        #print("Opcode: ", opcode)
        #print(stack)
        displayMemory()
        execute(opcode)

start()
















    