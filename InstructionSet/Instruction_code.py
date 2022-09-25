import sys
sys.path.append('../OSproject')

from controllers.memory_controller import *
from controllers.flag_controller import *
from Memory import memory, pc

#Instruction code which all follow the same format: 

#       set error to false
#       Deconstructing the operands and error (output from section 2)
#       if there is no error: do something and perform flag test
#       return error (or interrupt)

# At the bottom there are three functions that returns [operands..., error], using function from memory_controller which controls the memory and stack



def mov():
    [R1, R2, error] = getRegisterRegisterOperands()
    if(not error):
        R1.storedBytes = R2.storedBytes
    return error

def add():
    [R1, R2, error] = getRegisterRegisterOperands()
    if(not error):
        sum = R1.getInt() + R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum) 
    return error

def sub():
    [R1, R2, error] = getRegisterRegisterOperands()
    if(not error):
        sum = R1.getInt() - R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

def mul():
    [R1, R2, error] = getRegisterRegisterOperands()
    if(not error):
        sum = R1.getInt() * R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

def div():
    [R1, R2, error] = getRegisterRegisterOperands()
    if(not error):
        sum = R1.getInt() / R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

def and_():
    [R1, R2, error] = getRegisterRegisterOperands()
    if(not error):
        sum = R1.getInt() & R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

def or_():
    [R1, R2, error] = getRegisterRegisterOperands()
    if(not error):
        sum = R1.getInt() | R2.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), R2.getInt())
        R1.setInt(sum)
    return error

#------------------Register-Immediate Instructions------------------#

def movi():
    [R1, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        R1.setInt(immediate)
    return error

def addi():
    [R1, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = R1.getInt() + immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum) 
    return error

def subi():
    [R1, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error

def muli():
    [R1, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error


def divi():
    [R1, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error

def andi():
    [R1, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error

def ori():
    [R1, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = R1.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, R1.getInt(), immediate)
        R1.setInt(sum)
    return error

def bz():
    error = False
    offset = getSingleImmediateOperand()
    if(ZF() == 1): pc.setInt(offset)
    return error

def bnz():
    error = False
    offset = getSingleImmediateOperand()
    if(ZF() == 0): pc.setInt(offset)
    return error

def bc():
    error = False
    offset = getSingleImmediateOperand()
    if(CF() == 1): pc.setInt(offset)
    return error

def bs():
    error = False
    offset = getSingleImmediateOperand()
    if(SF() == 1): pc.setInt(offset)
    return error

def jmp():
    error = False
    offset = getSingleImmediateOperand()
    pc.setInt(offset)
    return error

def call():
    error = False
    offset = getSingleImmediateOperand()
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
    [R1, immediate, error] = getRegisterImmediateOperands()
    R1.storedBytes[0] = memory[immediate]
    R1.storedBytes[1] = memory[immediate+1]
    return error


def movs():
    [R1, immediate, error] = getRegisterImmediateOperands()
    memory[immediate] = R1.storedBytes[0]
    memory[immediate+1] = R1.storedBytes[1]
    return error


#------------------Single Operand Instructions-----------------#

def shl():
    [R1, error] = getSingleRegisterOperand()
    if (not error):
        x = R1.getInt()
        result = x << 1
        R1.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def shr():
    [R1, error] = getSingleRegisterOperand()
    if (not error):
        x = R1.getInt()
        result = x >> 1
        R1.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def rtl():
    [R1, error] = getSingleRegisterOperand()
    if (not error):
        x = R1.getInt()
        result = 0x8000 | x >> 1 if x & 0x1 != 0 else x >> 1
        R1.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def rtr():
    [R1, error] = getSingleRegisterOperand()
    if (not error):
        x = R1.getInt()
        result = (0x1 | x << 1) & 0xFFFF if x & 0x8000 != 0 else (x << 1) & 0xFFFF
        R1.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def inc():
    [R1, error] = getSingleRegisterOperand()
    if (not error):
        R1.inc()
    return error

def dec():
    [R1, error] = getSingleRegisterOperand()
    if (not error):
        R1.dec()
    return error

def push():
    [R1, error] = getSingleRegisterOperand()
    if (not error):
        error = pushStack(R1.getInt())
    return error

def pop():
    [R1, error] = getSingleRegisterOperand()
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


# ------------------------ section 2 ------------------------ #

# Description: Fetching the Operands and the error using functions from sections 3


def getRegisterRegisterOperands(): #returns 2 registers and updates PC
    error = False

    [R1, errorA] = fetchRegister()
    [R2, errorB] = fetchRegister()
    if(errorA != 0):
        error = errorA + ' (Error at first operand)'
    elif(errorB != 0):
        error = errorB + ' (Error at first operand)'
    return [R1, R2, error]

def getRegisterImmediateOperands(): #returns 1 registers and 1 immediate value and updates PC

    error = False
    [R1, errorA] = fetchRegister()
    [mem, errorB] = fetchImmediate()

    if(errorA != 0):
        error = errorA + ' (Error at first operand)'
    elif(errorB != 0):
        error = errorB + ' (Error at second operand)'

    return [R1, mem, error]

def getSingleRegisterOperand(): #returns 1 register and updates PC
    [R1, error] = fetchRegister()
    return [R1, error]

def getSingleImmediateOperand(): #returns 1 immediate value and updates PC
    [mem, error] = fetchImmediate()
    return [mem, error]

