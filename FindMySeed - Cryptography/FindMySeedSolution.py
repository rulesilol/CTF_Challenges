from z3 import *

def myprng(seedA, seedB, seedC):
    a = (seedA << 13) * 11
    a = a & 0xFFFFFFFF
    
    b = (seedB >> 12) ^ (seedC << 22) + 852145
    b = b & 0xFFFFFFFF
    
    c = (seedA << 3 | seedC >> 18)
    c = c & 0xFFFFFFFF
    
    r = (((a ^ b) * 7) ^ c) & 0xFFFFFFFF 
    seedA = (b ^ c) & 0xFFFFFFFF
    seedB = (a ^ c) & 0xFFFFFFFF
    seedC = (a ^ b) & 0xFFFFFFFF
    
    return r, (seedA, seedB, seedC)

a,b,c = z3.BitVecs("a b c", 32)
xrand1, state = myprng(a,b,c)
xrand2, state = myprng(*state)
xrand3, state = myprng(*state)
xrand4, state = myprng(*state)

rand1 = 1001996967
rand2 = 640617042
rand3 = -96945703
rand4 = 1418336210

z3.solve(
    xrand1 == rand1,
    xrand2 == rand2,
    xrand3 == rand3,
    xrand4 == rand4
)