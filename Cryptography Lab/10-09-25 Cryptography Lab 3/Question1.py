def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y

def find_solutions(a, b, c, num_solutions=5):
    d, x1, y1 = extended_gcd(a, b)
    print(f"\nSolving equation: {a}x + {b}y = {c}")
    print(f"GCD({a}, {b}) = {d}")
    
    if c % d != 0:
        print("No integer solutions exist because GCD does not divide c.")
        return
    
    factor = c // d
    x0 = x1 * factor
    y0 = y1 * factor
    
    a1 = a // d
    b1 = b // d
    
    print(f"Particular solution: x = {x0}, y = {y0}")
    print(f"First {num_solutions} solutions:")
    
    for t in range(num_solutions):
        x = x0 + b1 * t
        y = y0 - a1 * t
        print(f"t = {t}: x = {x}, y = {y}")

find_solutions(56, 72, 40)
find_solutions(24, 138, 18)