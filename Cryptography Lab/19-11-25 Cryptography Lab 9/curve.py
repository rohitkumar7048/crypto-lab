from tinyec import registry
import secrets
import random


def compress(publicKey):
    return hex(publicKey.x) + hex(publicKey.y % 2)[2:]

# Choose curve
curvePoint = registry.get_curve('brainpoolP256r1')

# Private keys
Na = secrets.randbelow(curvePoint.field.n)
Nb = secrets.randbelow(curvePoint.field.n)

# Public keys
Pa = Na * curvePoint.g
Pb = Nb * curvePoint.g

print("Public key for A: ", compress(Pa))
print("Public key for B: ", compress(Pb))


# Shared keys
A_SharedKey = Na * Pb
B_SharedKey = Nb * Pa


print("A shared key:", compress(A_SharedKey))
print("B shared key:", compress(B_SharedKey))
print("Equal shared keys:", A_SharedKey == B_SharedKey)



def Elliptic_encrypt(k, G, encoded, Pb):
    C1 = k * G
    S  = k * Pb
    C2 = encoded + S.x           # only using x-coordinate
    return (C1, C2)


def ecc_decrypt(Nb, C1, C2):
    S = Nb * C1
    m_int = C2 - S.x
    return (m_int)


message = input("Enter Message: ")


encoded = ""
for char in message:
    encoded += (str)(ord(char))

encoded = int(encoded)
print(encoded)



k = random.randint(1, 100)
C1, C2 = Elliptic_encrypt(k, curvePoint.g, encoded, Pb)
print("\nCiphertext:")
print("C1 =", compress(C1))
print("C2 =", C2)



# Encode by Split
encodedsplit = ""
for char in message:
    encodedsplit += str(ord(char)) + " "   # add space

encodedsplit = encodedsplit.strip()
print("Encoded:", encodedsplit)


#Decode
decoded = ""
parts = encodedsplit.split()

for p in parts:
    decoded += chr(int(p))



plain = ecc_decrypt(Nb, C1, C2)

print("Decoded:", plain)
print("\nDecrypted message:", decoded)









# sudo apt install python3.12-venv
# python3 -m venv venv
# source venv/bin/activate
# pip install tinyec
