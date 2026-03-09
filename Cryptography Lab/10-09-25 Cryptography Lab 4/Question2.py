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

def pair_gcd_1(n):
    if n <= 6 or n % 2 != 0:
        print("Invalid input. n must be even and greater than 6.")
        return

    for p in range(2, n + 1):
        if is_prime(p):
            q = n - p
            if is_prime(q):
                gcd_value = math.gcd(n - p, n - q)
                if gcd_value == 1:
                    print(f"p = {p}, q = {q}, gcd({n-p}, {n-q}) = {gcd_value}")
                    return
    
    print(-1)


n = int(input("Enter an even number greater than 6: "))
pair_gcd_1(n)


