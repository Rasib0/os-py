from utility.base_conversions import twoBytesToInt, intToTwoBytes, twoBytesToHex

class Register:
    def __init__(self):
        self.storedBytes = bytearray(2)


# setter and getter 

    def setInt(self, value: int): # input: 16 bit integer
        self.storedBytes = intToTwoBytes(value)

    def getInt(self) -> int:
        return twoBytesToInt(self.storedBytes)


#increase/decrease register value by a number
    def inc(self, by: int = 1):
        x = (self.getInt()+by) & 0xFFFF
        self.setInt(x)

    def dec(self, by: int = 1):
        x = (self.getInt()-by) & 0xFFFF
        self.setInt(x)

# Cosmetic functions for displaying the byte as a hexadecimal or binary
    
    def getHex(self) -> str:
        return twoBytesToHex(self.storedBytes)

    def getBin(self) -> str:
        return bin(self.getInt())
    


    

