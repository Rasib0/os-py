import sys
sys.path.append('../OSproject')
from utils.conversions import intToTwoBytes, twoBytesToHex, twoBytesToInt

x = bytearray(2)
x[0] = 25
x[1] = 22
print(x)
print(twoBytesToHex(x))
print(twoBytesToInt(x))
print(intToTwoBytes(6422))