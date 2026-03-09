import math

print("\nProduct Cipher Program (Rail Fence + Row Transposition)")


def rail_fence_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
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

    # Read zigzag
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



def get_key_order(key):
    sorted_key = sorted(list(enumerate(key)), key=lambda x: (x[1], x[0]))
    order = [0] * len(key)
    for idx, (orig_pos, _) in enumerate(sorted_key):
        order[orig_pos] = idx + 1
    return order


def row_transposition_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    key_order = get_key_order(key)

    columns = len(key)
    rows = math.ceil(len(plaintext) / columns)

    # Fill matrix row by row
    matrix = [['X' for _ in range(columns)] for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(columns):
            if index < len(plaintext):
                matrix[r][c] = plaintext[index]
                index += 1

    # Read columns according to key order
    ciphertext = ""
    for num in sorted(key_order):
        col = key_order.index(num)
        for r in range(rows):
            ciphertext += matrix[r][col]

    return ciphertext


def row_transposition_decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.upper()
    key_order = get_key_order(key)

    columns = len(key)
    rows = math.ceil(len(ciphertext) / columns)

    # Create empty matrix
    matrix = [['' for _ in range(columns)] for _ in range(rows)]

    # Fill columns according to key order
    index = 0
    for num in sorted(key_order):
        col = key_order.index(num)
        for r in range(rows):
            if index < len(ciphertext):
                matrix[r][col] = ciphertext[index]
                index += 1

    # Read row by row to reconstruct plaintext
    plaintext = ""
    for r in range(rows):
        for c in range(columns):
            plaintext += matrix[r][c]

    return plaintext.rstrip('X')



while True:
    choice = int(input("\nChoose: 1.Encryption  2.Decryption  3.Exit\n"))

    if choice == 1:
        plaintext = input("Enter the message: ")
        rail_key = int(input("Enter Rail Fence key (number of rails): "))
        row_key = input("Enter Row Transposition key (letters only): ")

   
        step1 = rail_fence_encrypt(plaintext, rail_key)
   
        final_cipher = row_transposition_encrypt(step1, row_key)

        print("\nAfter Rail Fence Encryption :", step1)
        print("After Row Transposition Encryption Final Ciphertext:", final_cipher)

    elif choice == 2:
        ciphertext = input("Enter the encrypted message: ")
        rail_key = int(input("Enter Rail Fence key (number of rails): "))
        row_key = input("Enter Row Transposition key (letters only): ")


        step1 = row_transposition_decrypt(ciphertext, row_key)
  
        final_plain = rail_fence_decrypt(step1, rail_key)

        print("\nAfter Row Transposition Decryption :", step1)
        print("After Rail Fence Decryption Final Plaintext:", final_plain)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
