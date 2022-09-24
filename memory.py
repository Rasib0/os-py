from Register import Register

addressSize = 16

memory = bytearray(2**addressSize)

#stack
stack= [0]*50

for i in range(50):
    stack[i]  = Register()

#General purpose registers
R= [0]*16

for i in range(16):
    R[i]  = Register()

#Special purpose registers
codeRegister = {"base": Register(),
               "limit": Register(),
               "counter": Register()}

stackRegister = {"base": Register(),
               "limit": Register(),
               "counter": Register()}

dataRegister = {"base": Register(),
               "counter": Register()}

flagRegister = [False]*16