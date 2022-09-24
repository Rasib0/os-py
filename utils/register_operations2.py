from pc_operations import currPcImmediateValue, currPcRegister

def registerRegisterOperands():
    A = currPcRegister()
    B = currPcRegister()
    return [A, B]

def registerImmediateOperands():
    A = currPcRegister()
    mem = currPcImmediateValue()
    return [A, mem]
    
def singleOperands():
    A = currPcRegister()
    return A