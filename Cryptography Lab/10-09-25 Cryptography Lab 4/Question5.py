def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def find_solutions():
    solutions = []
    p = 2
    while len(solutions) < 4:
        if is_prime(p):
            target = p**2 + 1
            
            for q in range(2, target):
                if is_prime(q):
                    for r in range(2, target):
                        if is_prime(r) and q <= r:
                            if q**2 + r**2 == target:
                                solutions.append((p, q, r))
                                break
                    else:
                        continue
                    break
        p += 1
    return solutions


solutions = find_solutions()
print(solutions)
print("Four solutions for p^2 + 1 = q^2 + r^2 with primes p, q, r:")
for sol in solutions:
    print(f"p = {sol[0]}, q = {sol[1]}, r = {sol[2]}")
