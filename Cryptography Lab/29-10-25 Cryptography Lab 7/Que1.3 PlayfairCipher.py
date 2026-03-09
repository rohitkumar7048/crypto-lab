print("\nPlayfair Cipher Program (Encryption & Decryption)")

# Generate Playfair Key Matrix
def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            used.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


# Find position of character
def find_position(matrix, char):
    if char == "J":
        char = "I"
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


# Prepare text into pairs
def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])
    prepared = ""
    i = 0
    while i < len(text):
        prepared += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared += "X"
        elif i + 1 < len(text):
            prepared += text[i + 1]
            i += 1
        i += 1

    if len(prepared) % 2 != 0:
        prepared += "X"

    return prepared



# Encryption

def playfair_encrypt(text, matrix):
    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # Same row
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        # Same column
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        # Rectangle rule
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext



#  Decryption

def playfair_decrypt(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        # Same row
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        # Same column
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        # Rectangle rule
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    return plaintext



#  Display Key Matrix
def print_matrix(matrix):
    print("\nKey Matrix:")
    for row in matrix:
        print(" ".join(row))



while True:
    choice = int(input("\nChoose: 1.Encryption  2.Decryption  3.Exit\n"))

    if choice == 1:
        key = input("Enter key: ")
        plaintext = input("Enter message to encrypt: ")

        key_matrix = generate_key_matrix(key)
        print_matrix(key_matrix)

        prepared_text = prepare_text(plaintext)
        encrypted = playfair_encrypt(prepared_text, key_matrix)

        print("\nPrepared Text:", prepared_text)
        print("Encrypted Message:", encrypted)

    elif choice == 2:
        key = input("Enter key: ")
        ciphertext = input("Enter message to decrypt: ").upper().replace(" ", "")

        key_matrix = generate_key_matrix(key)
        print_matrix(key_matrix)

        decrypted = playfair_decrypt(ciphertext, key_matrix)

        print("\nCiphertext:", ciphertext)
        print("Decrypted Message:", decrypted)

    elif choice == 3:
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
