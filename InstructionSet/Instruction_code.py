import sys
sys.path.append('../OSproject')

from Register import Register
from utilityFunctions.base_conversions import twoBytesToInt
from utilityFunctions.flag_operations import *
from Memory import R, memory, pc, sc, zeroRegister, stack

# This file is divided into 3 sections

# Section 1: instruction code which all follow the same format: 

#       set error to false
#       Deconstructing the operands and error (output from section 2)
#       if there is no error: do something and perform flag test
#       return error (or interrupt)

# Section 2: three functions that returns [operands..., error]

# Section 3: the implementation of memory/PC and stack/SC operations which fetch register/immediate value from memory/stack and update PC/SC


# ------------------------ section 1 ------------------------ #
#Register-register Instructions

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
        push(pc.getInt())
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
        R1.setInt()
    return error

def pop():
    [R1, error] = getSingleRegisterOperand()
    if (not error):
        [value, error] = pop()
        R1.setInt(value)
    return error

#----------------No Operand Instructions-----------------#

def return_():
    [value, error] = pop()
    if(not error):
        pc.setInt(value)
    #popPcFromStack()
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


# stack operations 

def pop(): #fetches the 2 byte immediate value in stack currently and updates SC
    error = False
    temp = bytearray(2)

    if(sc < 2):
        error = "Error: Stack underflow"
        return [0, error]
    temp[0]  = stack[sc.getInt()-2]
    temp[1] =  stack[sc.getInt()-1]
    stack[sc.getInt()-1] = 0
    stack[sc.getInt()-2] = 0
    sc.dec(2)
    value = twoBytesToInt(temp)
    return [value, error]
   
   
def push(value: int):
    error = False
    temp = Register()
    temp.setInt(value)

    if(sc >= 50):
        error = "Error: Stack overflow"
        return error

    stack[sc] = temp.storedBytes[0]
    stack[sc+1] = temp.storedBytes[1]
    sc.inc(2)
    return error
