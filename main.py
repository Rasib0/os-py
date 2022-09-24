from Memory import *
from utilityFunctions.genericCounterOperations import pcIntValue, scIntValue, setPc
from FetchExecuteCycleFunctions import  decode, displayMemory, writeInMemory,  execute

#fetch the byte stream 
with open('p1.txt') as f:
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
        print("Opcode: ", opcode)
        count += 1

        #print("PC Value: ", pcIntValue())
        #print("SC Value: ", scIntValue())
        #print(stack)
        execute(opcode)
        
        displayMemory()

        if(opcode == 243): #break the execution loop at opcode for END
            print("END.")
            break
start()
















    