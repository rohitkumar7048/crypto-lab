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

def odd_prime_factors(n):
    factors = set()
    d = 3 
    while n > 1 and d <= n:
        if n % d == 0 and is_prime(d):
            factors.add(d)
            n //= d
        else:
            d += 2
    return factors

n = 1
while True:
    x = n**2 + 1
    factors = odd_prime_factors(x)
    if len(factors) == 3:
        print("n =", n, "gives n^2 + 1 =", x, "with factors", factors)
        break
    n += 1
