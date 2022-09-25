from ftplib import error_perm
import sys
sys.path.append('../OSproject')
from utilityFunctions.flag_operations import *
from utilityFunctions.counter_operations import popStackToRegister, pushRegisterToStack, returnPcFromSc, pushPcToSc, fetchImmediateFromPc, fetchRegisterFromPc, setPc
from Memory import memory

#------------------Register-register Instructions-------------------#

def mov():
    [A, B, error] = getRegisterRegisterOperands()
    if(not error):
        A.storedBytes = B.storedBytes
    return error

def add():
    [A, B, error] = getRegisterRegisterOperands()
    if(not error):
        sum = A.getInt() + B.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), B.getInt())
        A.setInt(sum) 
    return error

def sub():
    [A, B, error] = getRegisterRegisterOperands()
    if(not error):
        sum = A.getInt() - B.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), B.getInt())
        A.setInt(sum)
    return error

def mul():
    [A, B, error] = getRegisterRegisterOperands()
    if(not error):
        sum = A.getInt() * B.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), B.getInt())
        A.setInt(sum)
    return error

def div():
    [A, B, error] = getRegisterRegisterOperands()
    if(not error):
        sum = A.getInt() / B.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), B.getInt())
        A.setInt(sum)
    return error

def and_():
    [A, B, error] = getRegisterRegisterOperands()
    if(not error):
        sum = A.getInt() & B.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), B.getInt())
        A.setInt(sum)
    return error_perm

def or_():
    [A, B, error] = getRegisterRegisterOperands()
    if(not error):
        sum = A.getInt() | B.getInt()
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), B.getInt())
        A.setInt(sum)
    return error

#------------------Register-Immediate Instructions------------------#

def movi():
    [A, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        A.setInt(immediate)
    return error

def addi():
    [A, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = A.getInt() + immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), immediate)
        A.setInt(sum) 
    return error

def subi():
    [A, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = A.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), immediate)
        A.setInt(sum)
    return error

def muli():
    [A, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = A.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), immediate)
        A.setInt(sum)
    return error


def divi():
    [A, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = A.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), immediate)
        A.setInt(sum)
    return error

def andi():
    [A, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = A.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), immediate)
        A.setInt(sum)
    return error

def ori():
    [A, immediate, error] = getRegisterImmediateOperands()
    if(not error):
        sum = A.getInt() - immediate
        sum = sum & 0xFFFF
        ArithmeticLogicalFlagTest(sum, A.getInt(), immediate)
        A.setInt(sum)
    return error

def bz():
    error = False
    offset = getSingleImmediateOperand()
    if(ZF() == 1): setPc(offset)
    return error

def bnz():
    error = False
    offset = getSingleImmediateOperand()
    if(ZF() == 0): setPc(offset)
    return error

def bc():
    error = False
    offset = getSingleImmediateOperand()
    if(CF() == 1): setPc(offset)
    return error

def bs():
    error = False
    offset = getSingleImmediateOperand()
    if(SF() == 1): setPc(offset)
    return error

def jmp():
    error = False
    offset = getSingleImmediateOperand()
    setPc(offset)
    return error

def call():
    error = False
    offset = getSingleImmediateOperand()
    pushPcToSc()
    setPc(offset)
    return error

def act():
    error = False
    return error

#-----------Memory Instructions using immediate offset-------------#

def movl():
    [A, immediate, error] = getRegisterImmediateOperands()
    A.storedBytes[0] = memory[immediate]
    A.storedBytes[1] = memory[immediate+1]
    return error


def movs():
    [A, immediate, error] = getRegisterImmediateOperands()
    memory[immediate] = A.storedBytes[0]
    memory[immediate+1] = A.storedBytes[1]
    return error


#------------------Single Operand Instructions-----------------#

def shl():
    [A, error] = getSingleRegisterOperand()
    if (not error):
        x = A.getInt()
        result = x << 1
        A.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def shr():
    [A, error] = getSingleRegisterOperand()
    if (not error):
        x = A.getInt()
        result = x >> 1
        A.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def rtl():
    [A, error] = getSingleRegisterOperand()
    if (not error):
        x = A.getInt()
        result = 0x8000 | x >> 1 if x & 0x1 != 0 else x >> 1
        A.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def rtr():
    [A, error] = getSingleRegisterOperand()
    if (not error):
        x = A.getInt()
        result = (0x1 | x << 1) & 0xFFFF if x & 0x8000 != 0 else (x << 1) & 0xFFFF
        A.setInt(result)
        shiftRotateFlagTest(x, result)
    return error

def inc():
    [A, error] = getSingleRegisterOperand()
    if (not error):
        A.setInt(A.getInt() + 1)
    return error

def dec():
    [A, error] = getSingleRegisterOperand()
    if (not error):
        A.setInt(A.getInt() - 1)
    return error

def push():
    [A, error] = getSingleRegisterOperand()
    if (not error):
        pushRegisterToStack(A)
    return error

def pop():
    [A, error] = getSingleRegisterOperand()
    if (not error):
        popStackToRegister(A)
    return error

#----------------No Operand Instructions-----------------#

def return_():
    error = returnPcFromSc()
    return error

def noop():
    error = False
    return error

def end():
    error = "End interrupt."
    return error


#----------------Fetching the Operands-------------------#

#returns 2 registers and updates PC

def getRegisterRegisterOperands():
    error = False

    [A, errorA] = fetchRegisterFromPc()
    [B, errorB] = fetchRegisterFromPc()
    if(errorA != 0):
        error = errorA + ' (Error at first operand)'
    elif(errorB != 0):
        error = errorB + ' (Error at first operand)'
    return [A, B, error]

#returns 1 registers and 1 immediate value and updates PC
def getRegisterImmediateOperands():
    error = False
    [A, errorA] = fetchRegisterFromPc()
    [mem, errorB] = fetchImmediateFromPc()

    if(errorA != 0):
        error = errorA + ' (Error at first operand)'
    elif(errorB != 0):
        error = errorB + ' (Error at second operand)'

    return [A, mem, error]

#returns 1 register and updates PC
def getSingleRegisterOperand():
    [A, error] = fetchRegisterFromPc()
    return [A, error]

#returns 1 immediate value and updates PC
def getSingleImmediateOperand():
    [mem, error] = fetchImmediateFromPc()
    return [mem, error]

