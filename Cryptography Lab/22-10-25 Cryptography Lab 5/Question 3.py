import math
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, math.isqrt(n)+1, 2):
        if(n % i == 0):
            return False
    return True

def smallest_prime_factor(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i):
            return i
    return num

for n in range(1, 21):
    value = math.factorial(n) + 1
    spf = smallest_prime_factor(value)
    print(f"n = {n}, n! + 1 = {value}, Smallest prime factor = {spf}")
