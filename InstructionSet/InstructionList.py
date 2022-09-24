import sys
sys.path.append('../OSproject')
from InstructionSet.InstructionCode import *


InstructionList = {
        # Register-register Instructions
            16: mov,
            17: add,
            18: sub,
            19:	mul,
            20:	div,
            21: and_,
            22: or_,

        # Register-Immediate Instructions
            30: movi,
            31: addi,
            32: subi,
            33: muli,
            34: divi,
            35: andi,
            36: ori,
            37: bz,
            38: bnz,
            39: bc,
            40: bs,
            41: jmp,
            42: call,
            43: act,

        # Memory Instructions
            51: movl,
            52: movs,
            71: shl,
            72: shr,
            73: rtl,
            74: rtr,
            75: inc,
            76: dec,
            77: push,
            78: pop,
            241:return_,
            242:noop,
            243:end
            }

