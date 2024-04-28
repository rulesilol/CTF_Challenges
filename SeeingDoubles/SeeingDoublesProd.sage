from secret import KEY, FLAG
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from sage.all import *
import random

p = random_prime(2^128)
F = GF(p)
pt = KEY
g = F.primitive_element()

a = random.randint(1, p-1)
A = pow(g, a, p)

k = random.randint(2, 2^128)

c_1 = pow(g, k, p)
c_2 = ((pt % p) * pow(A, k, p)) % p

iv = b'Almost there!!!!'
cipher = AES.new(long_to_bytes(KEY), AES.MODE_EAX, iv)
ct = cipher.encrypt(FLAG)

with open('output.txt', 'w') as f:
    f.write(f'p = {p}\nA = {A}\ng = {g}\nc1 = {c_1}\nc2 = {c_2}\nct = {ct}')