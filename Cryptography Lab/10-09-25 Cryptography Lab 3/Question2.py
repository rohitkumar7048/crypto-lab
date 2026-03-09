def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
