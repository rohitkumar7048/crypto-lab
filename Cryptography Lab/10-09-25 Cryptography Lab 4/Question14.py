import math

def is_prime(x):
    if x < 2:
        return False
    for d in range(2, int(math.isqrt(x)) + 1):
        if x % d == 0:
            return False
    return True

def prime_factors(n):
    """Return prime factors with multiplicity, e.g. 12 -> [2, 2, 3]."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2 
    if n > 1:
        factors.append(n)
    return factors

results = []

for n in range(1, 20):        
    value = 2**n - 1
    if value > 1_000_000:
        break
    facs = prime_factors(value)
    if len(facs) == 2:        
        results.append((n, value, facs))

print("n, 2^n - 1, prime factors:")
for item in results:
    print(item)
