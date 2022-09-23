#input: bytearray size 2, output: int value
def twoBytesToInt(input: bytearray) -> int:
    return (input[0] << 4) + input[1]

def twoBytesToHex(input: bytearray) -> str:
    return hex((input[0] << 4) + input[1])

#input: 16 bit int, output: bytearray size 2 
def intToTwoBytes(value: int) -> bytearray:
    output = bytearray(2)

    if( value >= 256):
        output[0] = value & 0b1111
        output[1] = value >> 4
    else:
        output[0] = 0
        output[1] = value
    
    return output

    