def count_divisors(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1
    return divisors

def numbers_with_n_divisors(a, b, n):
    count = 0
    for x in range(a, b + 1):
        if count_divisors(x) == n:
            nums.append(x)
            count += 1
    return count

nums = []
print(numbers_with_n_divisors(2, 49, 3))
print(nums)
