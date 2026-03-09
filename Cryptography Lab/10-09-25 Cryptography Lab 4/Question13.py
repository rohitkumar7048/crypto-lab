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

def two_prime_factors(n):
    factors = set()
    d = 2
    while n > 1 and d <= n:
        if n % d == 0 and is_prime(d):
            factors.add(d)
            n //= d
        else:
            d += 1
    return len(factors) == 2  

result = []
n = 2
while len(result) < 5:
    if two_prime_factors(n) and two_prime_factors(n+1) and two_prime_factors(n+2):
        result.append(n)
    n += 1

print("The five least positive integers are:", result)
