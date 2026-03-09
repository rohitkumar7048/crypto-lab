import math

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


def find_solutions(limit):
    primes = [i for i in range(2, limit) if is_prime(i)]
    solutions = []

    for p in primes:
        for q in primes:
            s = p*(p+1) + q*(q+1)
            r = (-1 + math.isqrt(1 + 4*s)) / 2
            if r.is_integer() and is_prime(int(r)):
                solutions.append((p, q, int(r)))

    
    return solutions

limit = int(input("Check Primes upto ?: "))
print(find_solutions(limit))






# import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def find_solutions(limit):
#     primes = [i for i in range(2, limit) if is_prime(i)]
#     solutions = []

#     for p in primes:
#         for q in primes:
            
#             left_side = p * (p + 1) + q * (q + 1)

            
#             for r in primes:
#                 right_side = r * (r + 1)
#                 if left_side == right_side:
#                     solutions.append((p, q, r))
#                     break

#     return solutions


# limit = int(input("Check Primes up to: "))
# solutions = find_solutions(limit)


# print("Solutions found:", solutions)
