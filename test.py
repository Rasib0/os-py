#testing subtraction using bytearray
from Register import Register

from Register import Register
from utils.conversions import twoBytesToInt

newR = Register()
newR.storedBytes[0] = 2
newR.storedBytes[1] = 3
print(newR.binary(), newR.hexString())
newR.insert(256)
print(newR.intValue())
print(newR.hexString())
print(newR.binary())

#testing division using byte array
#testing addition using byte array