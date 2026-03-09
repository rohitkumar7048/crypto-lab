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
factors = []
n = 2
while len(result) < 5:
    val = n**2 - 1
    facs = distinct_prime_factors(val)
    product = 1
    for f in facs:
        product *= f

    if len(facs) == 3 and product == val:
        result.append(n)
        factors.append(facs)
    n += 1



print("Result:", result)
for i in range(len(result)):
    n_val = result[i]
    print(f"n = {n_val} such that {n_val**2 - 1} = product of 3 different primes {sorted(factors[i])}")

