import math

def gcd(a, h):
    while h:
        a, h = h, a % h
    return a


p = 23
q = 29
n = p * q
phi = (p - 1) * (q - 1)


e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1


k = 1
while (1 + k * phi) % e != 0:
    k += 1
d = (1 + k * phi) // e  # integer division

print("Public Key: (", e, ",", n, ")")
print("Private Key: (", d, ",", n, ")")



msg = int(input("Enter Message (integer only): "))
print("Message data =", msg)


c = pow(msg, e, n)
print("Encrypted data =", c)


m = pow(c, d, n)
print("Decrypted (original) Message =", m)
