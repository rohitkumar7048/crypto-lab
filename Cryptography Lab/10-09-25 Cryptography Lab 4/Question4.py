def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# first 3 values of n where there are no primes b/w n and n+10
def find_n():
    n_values = []
    n = 1
    while len(n_values) < 3:
        if all(not is_prime(i) for i in range(n, n + 11)):
            n_values.append(n)
        n += 1
    return n_values

def find_m():
    m_values = []
    m = 1
    while len(m_values) < 3:
        start = 10 * m
        end = 10 * (m + 1)
        if all(not is_prime(i) for i in range(start, end)):
            m_values.append(m)
        m += 1
    return m_values


print(find_n())
print( find_m())


