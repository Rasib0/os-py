from Storage.Memory import pc
from main_functions import  decode, displayMemory, writeInMemory,  execute

startingIndex = 0
writeInMemory('p1.txt', startingIndex) #write the byte stream in memory starting from startingIndex and sets pc to startingIndex

#the execution loop
def run():
    count = 0
    while(True):
        print("Instruction Number", count)

        opCode = decode()
        Interrupt = execute(opCode)
        
        if(Interrupt):  
            print(Interrupt)
            break;
        #print(stack)
        displayMemory()
        count += 1
        
run()











    