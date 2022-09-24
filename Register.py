from utils.conversions import twoBytesToInt, intToTwoBytes, twoBytesToHex

class Register:
    def __init__(self):
        self.storedBytes = bytearray(2)

    def insert(self, value: int):
        self.storedBytes = intToTwoBytes(value)

    def intValue(self):
        return twoBytesToInt(self.storedBytes)

    def hexString(self):
        return twoBytesToHex(self.storedBytes)

    def binary(self):
        return bin(self.intValue())
    


    

