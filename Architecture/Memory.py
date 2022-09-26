import sys
sys.path.append('../OSproject')
from Architecture.Register import Register
addressSize = 16

#Setting up a memory with 64k bytes
memory = bytearray(2**addressSize)

#Setting up a stack with 50 bytes
stack= bytearray(50)


#Setting up thirty-two 16 bit Register
R= [0]*32

for i in range(32):
    R[i]  = Register()


#Giving the special purpose registers aliases for easy access
zeroRegister: Register = R[16]

codeRegister = {"base": R[17],
               "limit": R[18],
               "counter": R[19]}

stackRegister = {"base": R[20],
               "limit": R[21],
               "counter":R[22]}

dataRegister = {"base": R[23],
               "counter": R[24]}

flagRegister: Register = R[25]

pc: Register = codeRegister['counter']
sc: Register = stackRegister['counter']

#Giving the flags purpose registers aliases for easy access
def CF():
    return checkBit(flagRegister.getInt(), 0)
def ZF():
    return checkBit(flagRegister.getInt(), 1)
def SF():
    return checkBit(flagRegister.getInt(), 2)
def OF():
    return checkBit(flagRegister.getInt(), 3)

def checkBit(num: int, position: int) -> int:
   return (num >> position) & 1