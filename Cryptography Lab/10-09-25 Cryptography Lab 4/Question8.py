def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_n(limit):
    valid_n = []
    for n in range(1, limit + 1):
        if all(is_prime(n + offset) for offset in [1, 3, 7, 9, 13, 15]):
            valid_n.append(n)
    return valid_n


limit = int(input("Check Primes upto ?: "))
solutions = find_n(limit)

print("All positive integers n such that n+1, n+3, n+7, n+9, n+13, and n+15 are prime:")
print(solutions)
