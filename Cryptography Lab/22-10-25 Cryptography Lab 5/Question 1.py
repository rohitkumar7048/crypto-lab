import math
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, math.isqrt(n)+1, 2):
        if(n % i == 0):
            return False
    return True

def twinPrimes(n):
    nums = []
    for i in range(2, n - 1):
        if is_prime(i) and is_prime(i + 2):
            nums.append((i, i + 2))
    return nums


n = int(input("Enter the number: "))
print(f"Twin primes less than {n}:")
print(twinPrimes(n))
