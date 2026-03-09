import re
from math import gcd
from functools import reduce

def kasiski_examination(ciphertext):
    print("\n--- Kasiski Examination ---")
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())  # keep only letters
    seq_spacings = {}
    
    # Find repeated sequences of 3 letters (trigrams)
    for i in range(len(ciphertext) - 2):
        seq = ciphertext[i:i+3]
        for j in range(i + 3, len(ciphertext) - 2):
            if ciphertext[j:j+3] == seq:
                if seq not in seq_spacings:
                    seq_spacings[seq] = []
                seq_spacings[seq].append(j - i)
    
    if not seq_spacings:
        print("No repeating sequences of length 3 found.")
        return
    
    print("\nRepeated sequences and their spacings:")
    for seq, spaces in seq_spacings.items():
        print(f"{seq}: {spaces}")
    
    # Compute GCD of all spacings
    spacings = [space for spaces in seq_spacings.values() for space in spaces]
    key_length_guess = reduce(gcd, spacings)
    
    print(f"\nEstimated Key Length (GCD of spacings): {key_length_guess}")
    return key_length_guess


# Example usage
ciphertext = input("Enter the ciphertext (Vigenere Encrypted Message): ")
estimated_length = kasiski_examination(ciphertext)
