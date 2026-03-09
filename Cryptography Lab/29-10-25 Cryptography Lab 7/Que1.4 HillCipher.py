import numpy as np

# Matrix inverse modulo 26
def matrix_mod_inv(matrix, mod):
    det = int(round(np.linalg.det(matrix))) % mod          
    det_inv = pow(det, -1, mod)                            
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int)  
    return (det_inv * adjugate) % mod                      


def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]


def numbers_to_text(numbers):
    return ''.join(chr(n % 26 + ord('A')) for n in numbers)

# Encryption
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    while len(plaintext) % len(key_matrix) != 0:
        plaintext += 'X'

    encrypted_text = ""
    for i in range(0, len(plaintext), len(key_matrix)):
        block = text_to_numbers(plaintext[i:i+len(key_matrix)])
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_text += numbers_to_text(encrypted_block)
    return encrypted_text



# Decryption
def hill_decrypt(ciphertext, key_matrix):
    inv_key_matrix = matrix_mod_inv(key_matrix, 26)
    decrypted_text = ""
    for i in range(0, len(ciphertext), len(key_matrix)):
        block = text_to_numbers(ciphertext[i:i+len(key_matrix)])
        decrypted_block = np.dot(inv_key_matrix, block) % 26
        decrypted_text += numbers_to_text(decrypted_block)
    return decrypted_text



# Main program
print("\nHill Cipher program for Encryption & Decryption")

while True:
    choice = int(input("\nChoose: 1.Encryption 2.Decryption 3.Exit\n"))

    if choice == 1:
        n = int(input("Enter size of key matrix: "))
        print("Enter key matrix values row-wise:")
        key_matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            key_matrix.append(row)
        key_matrix = np.array(key_matrix)

        plaintext = input("Enter the message: ")
        encrypted = hill_encrypt(plaintext, key_matrix)
        print("Encrypted message is:", encrypted)

    elif choice == 2:
        n = int(input("Enter size of key matrix (same as used in encryption): "))
        print("Enter key matrix values row-wise:")
        key_matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            key_matrix.append(row)
        key_matrix = np.array(key_matrix)

        ciphertext = input("Enter the encrypted message: ")
        decrypted = hill_decrypt(ciphertext, key_matrix)
        print("Decrypted message is:", decrypted)

    elif choice == 3:
        break

    else:
        print("Invalid choice!")
