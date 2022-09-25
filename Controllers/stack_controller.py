import sys
sys.path.append('../OSproject')
from Architecture.Register import Register
from utilities.base_conversions import twoBytesToInt
from Architecture.Memory import  sc, stack


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
