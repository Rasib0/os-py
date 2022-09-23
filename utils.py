from memory import codeRegister

def updatePC(by_index: int):
    codeRegister['counter'] = codeRegister['counter'] + by_index
