print("\nProduct Cipher Program: Substitution + Transposition")

# Caesar Cipher
def substitution_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result


def substitution_decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result



def rail_fence_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    rail = ['' for _ in range(key)]
    direction_down = False
    row = 0

    for char in plaintext:
        rail[row] += char
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    return ''.join(rail)


def rail_fence_decrypt(ciphertext, key):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        result.append(rail[row][col])
        col += 1
        row += 1 if direction_down else -1

    return ''.join(result)



while True:
    choice = int(input("\nChoose: 1.Encryption  2.Decryption  3.Exit\n"))

    if choice == 1:
        plaintext = input("Enter the message: ")
        sub_key = int(input("Enter substitution key (Caesar key): "))
        trans_key = int(input("Enter transposition key (number of rails): "))

        step1 = substitution_encrypt(plaintext, sub_key)
        encrypted = rail_fence_encrypt(step1, trans_key)

        print("\n--- Encryption Process ---")
        print("After Substitution:", step1)
        print("After Transposition:", encrypted)
        print("Final Encrypted Message:", encrypted)

    elif choice == 2:
        ciphertext = input("Enter the encrypted message: ")
        sub_key = int(input("Enter substitution key (Caesar key): "))
        trans_key = int(input("Enter transposition key (number of rails): "))

        step1 = rail_fence_decrypt(ciphertext, trans_key)
        decrypted = substitution_decrypt(step1, sub_key)

        print("\n--- Decryption Process ---")
        print("After Transposition:", step1)
        print("After Substitution:", decrypted)
        print("Final Decrypted Message:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
