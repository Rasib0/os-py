def twoBytesToInt(input: bytearray) -> int: #input: bytearray size 2, output: int value
    return (input[0] << 8) + input[1]

def twoBytesToHex(input: bytearray) -> str: #input: bytearray size 2 , output: hex string 
    lower = hex(input[1])
    lower = lower[2:len(lower)]
    upper = hex(input[0])
    upper = upper[2:len(upper)]

    if(len(lower)==1):
        lower = '0' + lower

    if(len(upper)==1):
        upper = '0' + upper
        
    return  upper + lower


def intToTwoBytes(value: int) -> bytearray: #input: 16 bit int, output: bytearray size 2 
    output = bytearray(2)
    if( value >= 256):
        output[0] = value >> 8 #skip the first 8 bits
        output[1] = value & 0b11111111 #only take the last 8 bits
    else:
        output[0] = 0
        output[1] = value
    return output


