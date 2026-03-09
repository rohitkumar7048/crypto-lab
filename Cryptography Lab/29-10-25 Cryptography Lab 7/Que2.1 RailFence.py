print("\nRail Fence Cipher Program for Encryption & Decryption")

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
        key = int(input("Enter the key (number of rails): "))
        encrypted = rail_fence_encrypt(plaintext, key)
        print("Encrypted Message:", encrypted)

    elif choice == 2:
        ciphertext = input("Enter the encrypted message: ")
        key = int(input("Enter the key (number of rails): "))
        decrypted = rail_fence_decrypt(ciphertext, key)
        print("Decrypted Message:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
