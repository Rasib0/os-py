import sys
sys.path.append('../OSproject')
from utils.conversions import intToTwoBytes, twoBytesToHex, twoBytesToInt
from memory import flagRegister
from utils.flag_utils import *
x = bytearray(2)
x[0] = 25
x[1] = 22
#print(x)
#print(twoBytesToHex(x))
#print(twoBytesToInt(x))
#print(intToTwoBytes(6422))

flagRegister.insert(4639)
print(flagRegister.hexString())
print(flagRegister.binary())
print(OF())
clearOF()
print(OF())
print(flagRegister.hexString())
print(flagRegister.binary())
setOF()
print(OF())
print(flagRegister.hexString())
print(flagRegister.binary())
