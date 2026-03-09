def is_two_distinct_primes(n):
    count = 0
    d = 2
    while d*d <= n:
        if n % d == 0:
            count += 1
            n //= d
            if n % d == 0:  # repeated factor
                return False
        d += 1
    if n > 1:
        count += 1
    return count == 2

results = []
n = 2
while len(results) < 5:
    if all(is_two_distinct_primes(n+i) for i in range(3)):
        results.append(n)
    n += 1

print("Five least positive integers n are:", results)
