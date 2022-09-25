import sys
sys.path.append('../OSproject')

from Register import Register
from base_conversions import twoBytesToInt
from Memory import R, memory, pc, sc, zeroRegister, stack


# PC/memory operations

def fetchRegister() -> Register: #fetches the register in memory currently and updates Pc
    error = False
    register_number =memory[pc.getInt()]

    if(register_number > 15 and register_number < 32):
        error = "Error: Cannot move to special purpose register R[" +str(register_number-16) +"]"
        return [zeroRegister, error] #register unchanged because error 

    elif(register_number >= 32):
        error = "Error: No such register R[" +str(register_number-16) +"]"
        return [zeroRegister, error] #register unchanged because error

    R1 = R[register_number]
    pc.inc()
    return [R1, error]

def fetchImmediate(): #fetches the 2 byte immediate value in memory currently and updates PC
    error = False
    temp = bytearray(2)
    temp[0]  = memory[pc.getInt()]
    pc.inc()
    temp[1] =  memory[pc.getInt()]
    immediate = twoBytesToInt(temp)
    pc.inc()
    return [immediate, error]


# stack/SC operations 

def popStack(): #fetches the 2 byte immediate value in stack currently and updates SC
    error = False
    temp = bytearray(2)

    if(sc.getInt() < 2):
        error = "Error: Stack underflow"
        return [0, error]
    temp[0]  = stack[sc.getInt()-2]
    temp[1] =  stack[sc.getInt()-1]
    stack[sc.getInt()-1] = 0
    stack[sc.getInt()-2] = 0
    sc.dec(2)
    value = twoBytesToInt(temp)
    return [value, error]
   
   
def pushStack(value: int):
    error = False
    temp = Register()
    temp.setInt(value)

    if(sc.getInt() >= 50):
        error = "Error: Stack overflow"
        return error

    stack[sc.getInt()] = temp.storedBytes[0]
    stack[sc.getInt()+1] = temp.storedBytes[1]
    sc.inc(2)
    return error
