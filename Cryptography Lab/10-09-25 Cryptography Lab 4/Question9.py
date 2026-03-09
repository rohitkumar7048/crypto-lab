import math
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


# p = a^4 + b^4
def find_primes(limit, count):
    primes_found = set()
    
    for a in range(1, limit):
        for b in range(1, limit):
            n = a**4 + b**4
            if is_prime(n):
                primes_found.add(n)
                if len(primes_found) == count:
                    return list(primes_found)
    return list(primes_found)


limit = int(input("Check for integers upto ?: "))
primes = find_primes(limit, 5)
print(primes)

