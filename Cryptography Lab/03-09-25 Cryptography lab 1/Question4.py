def gcd(a, b):
    a, b = abs(a), abs(b)
    gcd = 1
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd

a = int(input("Enter value of a: " ))
b = int(input("Enter value of b: " ))

print(f"GCD of({a}, {b}) = {gcd(a, b)}")
