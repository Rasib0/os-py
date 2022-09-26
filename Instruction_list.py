import sys
sys.path.append('../OSproject')
from InstructionSet.Instruction_code import *


InstructionList = {
        # Register-register Instructions
            22: mov,
            23: add,
            24: sub,
            25:	mul,
            26:	div,
            27: and_,
            28: or_,

        # Register-Immediate Instructions
            48: movi,
            49: addi,
            50: subi,
            51: muli,
            52: divi,
            53: andi,
            54: ori,
            55: bz,
            56: bnz,
            57: bc,
            58: bs,
            59: jmp,
            60: call,
            61: act,

        # Memory Instructions
            81: movl,
            82: movs,
            113: shl,
            114: shr,
            115: rtl,
            116: rtr,
            117: inc,
            118: dec,
            119: push,
            120: pop,
            241:return_,
            242:noop,
            243:end
            }

