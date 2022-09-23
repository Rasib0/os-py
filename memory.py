from Register import Register
from utils.conversions import twoBytesToHex

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

flagRegister = Register()


#Display all the registers as a formated string
def displayMemory():
    gString = "General purpose registers:\n"
    for r in R:
        gString += r.hexString() + " "

    sString = "Special purpose registers:\n"
    for r in codeRegister:
        sString += codeRegister[r].hexString() + " "
    
    for r in stackRegister:
        sString += stackRegister[r].hexString() + " "

    for r in dataRegister:
        sString += dataRegister[r].hexString() + " "
    print(gString)
    print(sString)