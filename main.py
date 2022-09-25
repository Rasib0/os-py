from Memory import *
from utilityFunctions.counter_operations import setPc
from cycle_functions import  decode, displayMemory, writeInMemory,  execute

#write the byte stream in memory starting from starting index
startingIndex = 0
writeInMemory('p1.txt', startingIndex)
setPc(startingIndex)

#the execution loop
def start():
    count = 0
    while(True):
        print("Instruction Number", count)

        opCode = decode()
        Interrupt = execute(opCode)
        
        if(Interrupt):  
            print(Interrupt)
            break;
            
        displayMemory()
        count += 1

start()
















    