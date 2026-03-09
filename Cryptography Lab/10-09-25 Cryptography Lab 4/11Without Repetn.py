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

def distinct_prime_factors(n):
    factors = set()
    d = 2
    while n > 1:
        if n % d == 0 and is_prime(d):
            factors.add(d)
            while n % d == 0:
                n //= d
        else:
            d += 1
    return factors

result = []
n = 2
while len(result) < 5:
    facs = distinct_prime_factors(n**2 - 1)
    # check exactly 3 distinct primes and each appears once
    val = n**2 - 1
    # check stricter condition: val equals product of primes
    product = 1
    for f in facs:
        product *= f
    if len(facs) == 3 and product == val:
        result.append(n)
    n += 1

print(result)
