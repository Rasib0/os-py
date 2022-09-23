from memory import Register
from memory import memory, codeRegister



def mov(A: Register, B: bytearray):
    A.storedBytes = B.storedBytes
    codeRegister['counter'] = codeRegister['counter'] + 3

def sub(A: Register, B: bytearray):
    A = A - B
    codeRegister['counter'] = codeRegister['counter'] + 4

def add(A: Register, B: bytearray):
    A = A - B
    codeRegister['counter'] = codeRegister['counter'] + 4

