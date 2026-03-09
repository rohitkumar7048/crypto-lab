print("\nCaesar Cipher program for encryption & Decryption")
while(1):

    choice = int(input("\nChoose: 1.Encryption 2.Decryption 3.Exit\n"))

    if choice == 1:
        key = int(input("Enter the key: "))
        plaintext = input("Enter the message: ")

        encrypted = ""
        for char in plaintext:
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + key) % 26 + base)
        print("Encrypted message is:", encrypted)


    elif choice == 2:
        key = int(input("Enter the key: "))
        ciphertext = input("Enter the encrypted message: ")

        decrypted = ""
        for char in ciphertext:
                base = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - base - key) % 26 + base)
        print("Decrypted message is:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!.")
