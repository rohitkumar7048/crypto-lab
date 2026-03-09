import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def find_ap_solutions(limit):
    primes = [i for i in range(2, limit) if is_prime(i)]
    solutions = []

    for p in primes:
        for q in primes:
            for r in primes:
                if p < q < r:
                    if 2 * q * (q + 1) == p * (p + 1) + r * (r + 1):
                        solutions.append((p, q, r))
    return solutions


limit = int(input("Check Primes upto ?: "))
print("Prime solutions (p, q, r):", find_ap_solutions(limit))
