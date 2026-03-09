print("\nAutokey Cipher Program for Encryption & Decryption")

def autokey_encrypt(plaintext, key):
    plaintext = plaintext.lower().replace(" ", "")
    key = key.lower().replace(" ", "")
    
    # Extend key with plaintext itself
    key += plaintext
    key = key[:len(plaintext)]

    encrypted = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            p = ord(plaintext[i]) - ord('a')
            k = ord(key[i]) - ord('a')
            c = (p + k) % 26
            encrypted += chr(c + ord('a'))
        else:
            encrypted += plaintext[i]
    return encrypted


def autokey_decrypt(ciphertext, key):
    ciphertext = ciphertext.lower().replace(" ", "")
    key = key.lower().replace(" ", "")

    decrypted = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            c = ord(ciphertext[i]) - ord('a')
            k = ord(key[i]) - ord('a')
            p = (c - k + 26) % 26
            decrypted_char = chr(p + ord('a'))
            decrypted += decrypted_char
            key += decrypted_char  # Extend key with decrypted text dynamically
        else:
            decrypted += ciphertext[i]
    return decrypted


while True:
    choice = int(input("\nChoose: 1.Encryption  2.Decryption  3.Exit\n"))

    if choice == 1:
        plaintext = input("Enter the message: ")
        key = input("Enter the key (letters only): ")
        encrypted = autokey_encrypt(plaintext, key)
        print("Encrypted message is:", encrypted)

    elif choice == 2:
        ciphertext = input("Enter the encrypted message: ")
        key = input("Enter the key (same as used for encryption): ")
        decrypted = autokey_decrypt(ciphertext, key)
        print("Decrypted message is:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
