def euclid_GCD(a, b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return abs(a)


a = int(input("Enter value of a: " ))
b = int(input("Enter value of b: " ))

print(f"GCD of({a}, {b}) using Euclid's Algorithm = {euclid_GCD(a, b)}")
