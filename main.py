from main_functions import  decode, displayMemory, writeInMemory,  execute

startingIndex = 0
writeInMemory('p1-test.txt', startingIndex) #write the byte stream in memory starting from startingIndex and sets pc to startingIndex

#the execution loop
def run():
    count = 0
    Running = True
    while(Running):
        print("Instruction Number", count)
        #decode the first byte
        opCode = decode()
        #execute the instruction of opcode
        Interrupt = execute(opCode)
        #
        if(Interrupt):  
            print(Interrupt)
            Running = False

        displayMemory()
        count += 1
        
run()











    