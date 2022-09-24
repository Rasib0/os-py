import sys
sys.path.append('../OSproject')
from InstructionSet.operations import *


operatorsList = {
            16: mov,
            17: add,
            18: sub,
            #19:	mul,
            #20:	div,
            30: movi,
            31: addi,
            32: subi,
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

