def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular inverse does not exist.")

def affine_encrypt(plaintext, a, b):  # E(x) = (a*x + b) mod 26
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")

    result = ""
    for char in plaintext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr(((a * (ord(char) - offset) + b) % 26) + offset)
        else:
            result += char
    return result

def affine_decrypt(ciphertext, a, b):  # D(x) = a_inv * (x - b) mod 26
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")

    a_inv = mod_inverse(a, 26)
    result = ""
    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr(((a_inv * ((ord(char) - offset) - b)) % 26) + offset)
        else:
            result += char
    return result


print("\nAffine Cipher Program for Encryption & Decryption")

while True:
    choice = int(input("\nChoose: 1.Encryption 2.Decryption 3.Exit\n"))

    if choice == 1:
        a, b = map(int, input("Enter two keys a, b (a must be coprime with 26): ").split())
        plaintext = input("Enter the message: ")
        encrypted = affine_encrypt(plaintext, a, b)
        print("Encrypted message is:", encrypted)

    elif choice == 2:
        a, b = map(int, input("Enter two keys a, b (same as used for encryption): ").split())
        ciphertext = input("Enter the encrypted message: ")
        decrypted = affine_decrypt(ciphertext, a, b)
        print("Decrypted message is:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
