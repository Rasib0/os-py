from memory import Register
from memory import memory, codeRegister
from utils import updatePC


def mov(A: Register, B: bytearray):
    A.storedBytes = B.storedBytes
    updatePC(3)

def add(A: Register, B: bytearray):
    sum = A.value() + B.value()
    A.insert(sum) 
    updatePC(4)

def sub(A: Register, B: bytearray):
    sum = A.value() - B.value()
    A.insert(sum)
    updatePC(4)

