import random
import string

print("\nOne-Time Pad Cipher Program for Encryption & Decryption")

def generate_key(length):

    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def otp_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    ciphertext = ""

    for p, k in zip(plaintext, key):
        c = ((ord(p) - 65) ^ (ord(k) - 65)) + 65  
        ciphertext += chr(c)
    return ciphertext

def otp_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper()
    plaintext = ""

    for c, k in zip(ciphertext, key):
        p = ((ord(c) - 65) ^ (ord(k) - 65)) + 65
        plaintext += chr(p)
    return plaintext


while True:
    choice = int(input("\nChoose: 1.Encryption  2.Decryption  3.Exit\n"))

    if choice == 1:
        plaintext = input("Enter the message (letters only): ").upper()
        key = generate_key(len(plaintext))
        encrypted = otp_encrypt(plaintext, key)
        print("\nGenerated One-Time Key:", key)
        print("Encrypted Message:", encrypted)

    elif choice == 2:
        ciphertext = input("Enter the encrypted message: ").upper()
        key = input("Enter the key (same length as message): ").upper()
        decrypted = otp_decrypt(ciphertext, key)
        print("Decrypted Message:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
