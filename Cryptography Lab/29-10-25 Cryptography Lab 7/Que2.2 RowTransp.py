import math

print("\nRow Transposition Cipher Program for Encryption & Decryption")

def get_key_order(key):
    key_order = sorted(list(set(key)))
    order = []
    for char in key:
        order.append(sorted(key).index(char) + 1)
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
    for num in sorted(set(key_order)):
        col = key_order.index(num)
        for r in range(rows):
            ciphertext += matrix[r][col]

    return ciphertext


def row_transposition_decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.upper()


    key_order = sorted(range(len(key)), key=lambda i: key[i])

    cols = len(key)
    rows = math.ceil(len(ciphertext) / cols)


    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    # Fill columns in order of the sorted key
    index = 0
    for col in key_order:
        for r in range(rows):
            if index < len(ciphertext):
                matrix[r][col] = ciphertext[index]
                index += 1

    # Read row by row to get plaintext
    plaintext = ''.join(''.join(row) for row in matrix)
    return plaintext.rstrip('X')



while True:
    choice = int(input("\nChoose: 1.Encryption  2.Decryption  3.Exit\n"))

    if choice == 1:
        plaintext = input("Enter the message: ")
        key = input("Enter the key (letters only): ")
        encrypted = row_transposition_encrypt(plaintext, key)
        print("Encrypted Message:", encrypted)

    elif choice == 2:
        ciphertext = input("Enter the encrypted message: ")
        key = input("Enter the key (letters only): ")
        decrypted = row_transposition_decrypt(ciphertext, key)
        print("Decrypted Message:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
