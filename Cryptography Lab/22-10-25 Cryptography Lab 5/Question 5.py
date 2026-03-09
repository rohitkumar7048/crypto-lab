def Euclid(a,b):
    while(b !=0):
        a,b = b, a%b
    return a


a = int(input("Enter value of a: " ))
b = int(input("Enter value of b: " ))

print(f"GCD of({a}, {b}) using Euclid's Algorithm = {Euclid(a, b)}")
