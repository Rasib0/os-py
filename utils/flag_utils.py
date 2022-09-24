import sys
sys.path.append('../OSproject')
from memory import flagRegister

def checkBit(num: int, position: int) -> int:
   return (num >> position) & 1


def CF():
    return checkBit(flagRegister.intValue(), 0)
def ZF():
    return checkBit(flagRegister.intValue(), 1)
def SF():
    return checkBit(flagRegister.intValue(), 2)
def OF():
    return checkBit(flagRegister.intValue(), 3)

#set flags
def setCF():
    flagRegister.insert(flagRegister.intValue() | 0x1)

def setZF():
    flagRegister.insert(flagRegister.intValue() | 0x2)

def setSF():
    flagRegister.insert(flagRegister.intValue() | 0x4)

def setOF():
    flagRegister.insert(flagRegister.intValue() | 0x8)

#clear flags
def clearCF():
    flagRegister.insert(flagRegister.intValue() & 0xFFFE)

def clearZF():
    flagRegister.insert(flagRegister.intValue() & 0xFFFD)

def clearSF():
    flagRegister.insert(flagRegister.intValue() & 0xFFFB)

def clearOF():
    flagRegister.insert(flagRegister.intValue() & 0xFFF7)

