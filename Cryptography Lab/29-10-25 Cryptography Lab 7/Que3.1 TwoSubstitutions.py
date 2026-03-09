print("\nProduct Cipher Program (Two Substitution Ciphers: Caesar + Affine)")


def caesar_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plaintext, a, b):
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

def affine_decrypt(ciphertext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    a_inv = mod_inverse(a, 26)
    result = ""
    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr(((a_inv * ((ord(char) - offset - b)) % 26) + offset))
        else:
            result += char
    return result



while True:
    choice = int(input("\nChoose: 1.Encryption  2.Decryption  3.Exit\n"))

    if choice == 1:
        plaintext = input("Enter the message: ")
        caesar_key = int(input("Enter Caesar cipher shift key: "))
        a, b = map(int, input("Enter Affine cipher keys a, b (a must be coprime with 26): ").split())


        step1 = caesar_encrypt(plaintext, caesar_key)

        final_cipher = affine_encrypt(step1, a, b)

        print("\nAfter Caesar Encryption :", step1)
        print("After Affine Encryption Final Ciphertext:", final_cipher)


    elif choice == 2:
        ciphertext = input("Enter the encrypted message: ")
        caesar_key = int(input("Enter Caesar cipher shift key: "))
        a, b = map(int, input("Enter Affine cipher keys a, b (a must be coprime with 26): ").split())

        step1 = affine_decrypt(ciphertext, a, b)

        final_plain = caesar_decrypt(step1, caesar_key)

        print("\nAfter Affine Decryption :", step1)
        print("After Caesar Decryption Final Plaintext:", final_plain)
 

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
