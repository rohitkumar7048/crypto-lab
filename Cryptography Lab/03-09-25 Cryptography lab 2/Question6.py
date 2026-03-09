def gcd_steps(a, b):
    steps = 0
    while b != 0:
        a, b = b, a % b
        steps += 1
    return steps


print("Steps for gcd(55, 34):", gcd_steps(55, 34))
print("Steps for gcd(98, 56):", gcd_steps(98, 56)) 
print("Steps for gcd(98, 56):", gcd_steps(85, 289)) 
