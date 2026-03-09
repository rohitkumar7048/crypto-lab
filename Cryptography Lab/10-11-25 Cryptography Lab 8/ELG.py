import random
from math import gcd

# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a % c
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b //= 2
    return x % c


def gen_key(q):
    key = random.randint(10**20, q)
    while gcd(q, key) != 1:
        key = random.randint(10**20, q)
    return key


def encrypt(msg, q, h, g):
    en_msg = []
    k = gen_key(q)  # sender’s private key
    s = power(h, k, q)
    p = power(g, k, q)

    print("g^k used :", p)
    print("g^ak used :", s)

    for char in msg:
        en_msg.append((s * ord(char)) % q)
    return en_msg, p


def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    h_inv = pow(h, -1, q)  # modular inverse for division under mod q
    for val in en_msg:
        dr_msg.append(chr((val * h_inv) % q))
    return ''.join(dr_msg)


def main():
    msg = "encryption"
    print("Original Message:", msg)

    q = random.randint(10**20, 10**50)
    g = random.randint(2, q - 1)

    key = gen_key(q)  # receiver’s private key
    h = power(g, key, q)
    print("g used:", g)
    print("g^a used:", h)
    print("\n")

    en_msg, p = encrypt(msg, q, h, g)
    print("Encrypted Message:", en_msg)

    dmsg = decrypt(en_msg, p, key, q)
    print("Decrypted Message:", dmsg)

if __name__ == '__main__':
    main()
