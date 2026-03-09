def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range (3, int(n**0.5)+1, 2 ):
        if n % i == 0:
            return False
    return True


def find_prime_pair(number):
    for a in range(2, number +1):
        b = number - a
        if is_prime(a) and is_prime(b):
            print(f"{a}, {b}")
            return
    print(-1)


n = int(input("Enter a number greater than 2: "))
find_prime_pair(n)
