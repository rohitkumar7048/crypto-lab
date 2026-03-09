print("\nVigenere Cipher Program for Encryption & Decryption")

def vigenere_encrypt(plaintext, key):
    encrypted = ""
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            k = ord(key[key_index % len(key)]) - 97
            encrypted += chr((ord(char) - offset + k) % 26 + offset)
            key_index += 1
        else:
            encrypted += char
    return encrypted


def vigenere_decrypt(ciphertext, key):
    decrypted = ""
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            k = ord(key[key_index % len(key)]) - 97
            decrypted += chr((ord(char) - offset - k) % 26 + offset)
            key_index += 1
        else:
            decrypted += char
    return decrypted


while True:
    choice = int(input("\nChoose: 1.Encryption  2.Decryption  3.Exit\n"))

    if choice == 1:
        plaintext = input("Enter the message: ")
        key = input("Enter the key (letters only): ")
        encrypted = vigenere_encrypt(plaintext, key)
        print("Encrypted message is:", encrypted)

    elif choice == 2:
        ciphertext = input("Enter the encrypted message: ")
        key = input("Enter the key (same as used for encryption): ")
        decrypted = vigenere_decrypt(ciphertext, key)
        print("Decrypted message is:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
