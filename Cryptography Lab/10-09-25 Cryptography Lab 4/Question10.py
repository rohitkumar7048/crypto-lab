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

def non_twin_primes(limit):
    results = []
    prev = 7
    for n in range(11, limit + 1):
        if is_prime(n):
            if n - prev > 2:    
                results.append((prev, n))
            prev = n
    return results


limit = int(input("Check for integers upto ?: "))
print(non_twin_primes(limit))
