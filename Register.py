class Register:
    storedBytes = bytearray(2)
    binary = 0

    def __init__(self):
        self.storedBytes = bytearray(2)

    def value(self):
        return (self.storedBytes[0] << 4) + self.storedBytes[1]


    #when given a 16 bit value insert in the register
    def insert(self, value):
        if( value >= 256):
            self.storedBytes[0] = value & 0b1111
            self.storedBytes[1] = value >> 4


        else:
            self.storedBytes[0] = 0
            self.storedBytes[1] = value

    def binary(self):
        return bin(self.value())

