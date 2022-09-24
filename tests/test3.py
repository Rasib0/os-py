import sys
sys.path.append('../OSproject')
from utils.conversions import intToTwoBytes, twoBytesToHex, twoBytesToInt
from memory import flagRegister
from utils.flag_utils import *
x = bytearray(10)
x[0] = 31
x[2] = 31
print(x)
#print(twoBytesToHex(x))
#print(twoBytesToInt(x))
#print(intToTwoBytes(6422))

