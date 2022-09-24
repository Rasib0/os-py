from Register import Register

addressSize = 16

memory = bytearray(2**addressSize)

#stack
stack= [0]*50

for i in range(50):
    stack[i]  = Register()

R= [0]*32

for i in range(32):
    R[i]  = Register()

#naming the registers
sRegister = R[16]

codeRegister = {"base": R[17],
               "limit": R[18],
               "counter": R[19]}

stackRegister = {"base": R[20],
               "limit": R[21],
               "counter":R[22]}

dataRegister = {"base": R[23],
               "counter": R[24]}

flagRegister = R[25]