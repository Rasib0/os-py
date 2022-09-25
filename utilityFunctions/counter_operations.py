import sys
sys.path.append('../OSproject')
from Register import Register
from utilityFunctions.base_conversions import twoBytesToInt
from Memory import memory, R, stack, codeRegister, stackRegister

#----------- PC ------------#

def pc(): #returns the pc value as an int
    return codeRegister['counter'].intValue()

def setPc(value: int): #set the PC to the int value
    codeRegister['counter'].insert(value)
    
def incPc(by_index: int = 1): #updates PC by the index value
    codeRegister['counter'].insert(pc() + by_index)


#----------- SC -------------#
def sc():
    return stackRegister['counter'].intValue()

def setSc(value: int):
    stackRegister['counter'].insert(value)
    
def incSc(by_index: int = 1): #updates SC by the index value
    stackRegister['counter'].insert(sc() + by_index)




#-----------fetching register and immediate values from memory at PC and updating PC ------------#

def fetchRegisterFromPc() -> Register: #fetches the register in memory currently and updates Pc
    error = False
    register_number =memory[pc()]

    if(register_number > 15 and register_number < 32):
        error = "Error: Cannot move to special purpose register R[" +str(register_number-16) +"]"
        return [R[16], error]

    elif(register_number >= 32):
        error = "Error: No such register R[" +str(register_number-16) +"]"
        return [R[16], error]

    A = R[register_number]
    incPc()
    return [A, error]

def fetchImmediateFromPc() -> int: #fetches the 2 byte immediate value in memory currently and updates Pc
    error = False
    temp = bytearray(2)
    temp[0]  = memory[pc()]
    incPc()
    temp[1] =  memory[pc()]
    immediate = twoBytesToInt(temp)
    incPc()
    return [immediate, error]


#-----------fetching counter and immediate values from stack at SC and updating SC ------------#

def fetchImmediateFromSc() -> int: #fetches the 2 byte immediate value in stack currently and updates SC
    error = False
    temp = bytearray(2)
    temp[0]  = stack[sc()]
    incSc()
    temp[1] =  stack[sc()]
    immediate = twoBytesToInt(temp)
    incSc()
    return [immediate, error]
    


def popStackToRegister(R: Register) -> int:
    error = False
    sc = sc()

    if(sc < 2):
        error = "Error: Stack underflow"
        return error

    R.storedBytes[0] = stack[sc-2]
    R.storedBytes[1] = stack[sc-1]
    stack[sc-1] = 0
    stack[sc-2] = 0
    incSc(-2)
    return error

def pushRegisterToStack(R: Register):
    error = False
    sc = sc()

    if(sc >= 50):
        error = "Error: Stack overflow"
        return error

    stack[sc] = R.storedBytes[0]
    stack[sc+1] = R.storedBytes[1]
    incSc(2)
    return error

def pushPcToSc():
    error = False
    sc = sc()

    if(sc >= 50):
        error = "Error: Stack overflow"
        return error

    stack[sc] = codeRegister['counter'].storedBytes[0]
    stack[sc+1] = codeRegister['counter'].storedBytes[1]
    return error

def returnPcFromSc(): #sets PC to the value of stack at SC
    error = False
    sc = sc()

    if(sc < 2):
        error = "Error: Stack underflow"
        return error
    temp = twoBytesToInt(bytearray([stack[sc-2],
                                    stack[sc-1]]))
    incSc(-2)
    setPc(temp)
    return error

def action():
    error = False
    print("Action is currently not Defined.")
    return error