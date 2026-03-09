import math
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, math.isqrt(n)+1, 2):
        if(n % i == 0):
            return False
    return True

def func(m):
    result = []
    n = 1
    while len(result) < m:
        val = n**2 + 1
        if is_prime(val):
            result.append(val)
        n += 1
    return result


m = int(input("How many primes to find?: "))
print(f"First {m} primes of the form n^2 + 1:")
print(func(m))
