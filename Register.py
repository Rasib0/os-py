from tokenize import String
from utilityFunctions.base_conversions import twoBytesToInt, intToTwoBytes, twoBytesToHex

class Register:
    def __init__(self):
        self.storedBytes = bytearray(2)


# setter and getter using parameter expressing the two byte value as a single int (0 to 2^16)
    def setInt(self, value: int):
        self.storedBytes = intToTwoBytes(value)

    def getInt(self) -> int:
        return twoBytesToInt(self.storedBytes)

# -----functions for displaying the byte as a hexadecimal or binary -----#
    
    def getHex(self) -> str:
        return twoBytesToHex(self.storedBytes)

    def getBin(self) -> str:
        return bin(self.getInt())
    


    

