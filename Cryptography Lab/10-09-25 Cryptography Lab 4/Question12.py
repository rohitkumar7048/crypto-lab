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
factors_list = []
n = 1
while len(result) < 5:
    val = n**2 + 1
    facs = distinct_prime_factors(val)
    product = 1
    for f in facs:
        product *= f
    if len(facs) == 3 and product == val:
        result.append(n)
        factors_list.append(facs)
    n += 1

print("Five least n for which n^2 + 1 = product of 3 different primes:")
for i in range(len(result)):
    n_val = result[i]
    print(f"n = {n_val}, n^2+1 = {n_val**2 + 1}, primes = {sorted(factors_list[i])}")



# 2. Find a positive n where n^2 + 1 = product of 3 different odd primes
odd_result = None
n = 1
while odd_result is None:
    val = n**2 + 1
    facs = distinct_prime_factors(val)
    product = 1
    for f in facs:
        product *= f
    if len(facs) == 3 and product == val and all(p % 2 == 1 for p in facs):
        odd_result = (n, val, facs)
        break
    n += 1

print("\nA positive n where n^2 + 1 = product of 3 different odd primes:")
n_val, val, facs = odd_result
print(f"n = {n_val}, n^2+1 = {val}, primes = {sorted(facs)}")

