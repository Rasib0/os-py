import sys
sys.path.append('../OSproject')

from Controllers.memory_controller import *
from Controllers.flag_controller import *
from Controllers.stack_controller import *
from Architecture.Memory import memory, pc

#Instruction code which all follow the same format: 

#       set error to false
#       Deconstructing the operands and error from fetch operand functions
#       if there is no error: do something and perform flag test
#       return error (or interrupt in the case of end() )

def mov():
    error = False

    [R1, errorInR1, R2, errorInR2] = fetchRegister() + fetchRegister()

    if(errorInR1): error = errorInR1 + ' (Error at first operand)'
    elif(errorInR2): error = errorInR2 + ' (Error at second operand)'
    
    if(not error):
        R1.storedBytes = R2.storedBytes
    return error

def add():
    error = False
    [R1, errorInR1, R2, errorInR2] = fetchRegister() + fetchRegister()
    
    if(errorInR1): error = errorInR1 + ' (Error at first operand)'
    elif(errorInR2): error = errorInR2 + ' (Error at second operand)'
    
    if(not error):
        sum = R1.getInt() + R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum) 
    return error

def sub():
    error = False
    [R1, errorInR1, R2, errorInR2] = fetchRegister() + fetchRegister()
    
    if(errorInR1): error = errorInR1 + ' (Error at first operand)'
    elif(errorInR2): error = errorInR2 + ' (Error at second operand)'
    
    if(not error):
        sum = R1.getInt() - R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

def mul():
    error = False
    [R1, errorInR1, R2, errorInR2] = fetchRegister() + fetchRegister()
    
    if(errorInR1): error = errorInR1 + ' (Error at first operand)'
    elif(errorInR2): error = errorInR2 + ' (Error at second operand)'
    
    if(not error):
        sum = R1.getInt() * R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

def div():
    error = False
    [R1, errorInR1, R2, errorInR2] = fetchRegister() + fetchRegister()
    
    if(errorInR1): error = errorInR1 + ' (Error at first operand)'
    elif(errorInR2): error = errorInR2 + ' (Error at second operand)'
    
    if(not error):
        sum = R1.getInt() / R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

def and_():
    error = False
    [R1, errorInR1, R2, errorInR2] = fetchRegister() + fetchRegister()
        
    if(errorInR1): error = errorInR1 + ' (Error at first operand)'
    elif(errorInR2): error = errorInR2 + ' (Error at second operand)'
    
    if(not error):
        sum = R1.getInt() & R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

def or_():
    error = False
    [R1, errorInR1, R2, errorInR2] = fetchRegister() + fetchRegister()

    if(errorInR1): error = errorInR1 + ' (Error at first operand)'
    elif(errorInR2): error = errorInR2 + ' (Error at second operand)'
    
    if(not error):
        sum = R1.getInt() | R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

#------------------Register-Immediate Instructions------------------#

def movi():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    if(not error):
        R1.setInt(immediate)
    return error

def addi():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    if(not error):
        sum = R1.getInt() + immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum) 
    return error

def subi():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error

def muli():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error


def divi():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error

def andi():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error

def ori():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error

def bz():
    error = False
    [offset] = fetchImmediate()
    if(ZF() == 1): pc.setInt(offset)
    return error

def bnz():
    error = False
    [offset] = fetchImmediate()
    if(ZF() == 0): pc.setInt(offset)
    return error

def bc():
    error = False
    [offset] = fetchImmediate()
    if(CF() == 1): pc.setInt(offset)
    return error

def bs():
    error = False
    [offset] = fetchImmediate()
    if(SF() == 1): pc.setInt(offset)
    return error

def jmp():
    error = False
    [offset] = fetchImmediate()
    pc.setInt(offset)
    return error

def call():
    error = False
    [offset] = fetchImmediate()
    if(not error):
        pushStack(pc.getInt())
        pc.setInt(offset)
    return error

def act():
    error = False
    if(not error):
        print("Action is currently not Defined.")
    return error

#-----------Memory Instructions using immediate offset-------------#

def movl():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    R1.storedBytes[0] = memory[immediate]
    R1.storedBytes[1] = memory[immediate+1]
    return error


def movs():
    [R1, error, immediate] = fetchRegister() + fetchImmediate()
    memory[immediate] = R1.storedBytes[0]
    memory[immediate+1] = R1.storedBytes[1]
    return error


#------------------Single Operand Instructions-----------------#

def shl():
    [R1, error] = fetchRegister()
    if (not error):
        x = R1.getInt()
        result = x << 1
        R1.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def shr():
    [R1, error] = fetchRegister()
    if (not error):
        x = R1.getInt()
        result = x >> 1
        R1.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def rtl():
    [R1, error] = fetchRegister()
    if (not error):
        x = R1.getInt()
        result = 0x8000 | x >> 1 if x & 0x1 != 0 else x >> 1
        R1.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def rtr():
    [R1, error] = fetchRegister()
    if (not error):
        x = R1.getInt()
        result = (0x1 | x << 1) & 0xFFFF if x & 0x8000 != 0 else (x << 1) & 0xFFFF
        R1.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def inc():
    [R1, error] = fetchRegister()
    if (not error):
        R1.inc()
    return error

def dec():
    [R1, error] = fetchRegister()
    if (not error):
        R1.dec()
    return error

def push():
    [R1, error] = fetchRegister()
    if (not error):
        error = pushStack(R1.getInt())
    return error

def pop():
    [R1, error] = fetchRegister()
    if (not error):
        [value, error] = popStack()
        if(not error):
            R1.setInt(value)
    return error

#----------------No Operand Instructions-----------------#

def return_():
    [value, error] = popStack()
    if(not error):
        pc.setInt(value)
    return error

def noop():
    error = False
    return error

def end():
    error = "End interrupt."
    return error
