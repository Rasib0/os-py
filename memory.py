from Register import Register


addressSize = 16

memory = bytearray(2**addressSize)

#General purpose registers
R= [Register()]*16

#Special purpose registers

codeRegister = {"base": Register(),
               "limit": Register(),
               "counter": Register()}


stackRegister = {"base": Register(),
               "limit": Register(),
               "counter": Register()}

dataRegister = {"base": Register(),
               "limit": Register(),
               "counter": Register()}

flagRegister = [False] * 16


print(dataRegister)


