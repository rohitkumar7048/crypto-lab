def count_divisors(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1
    return divisors

def k_divisors(a, b, k):
    count = 0
    for num in range(a, b + 1):
        if count_divisors(num) == k:
            count += 1
            nums.append(num)

    return count

nums = []
a = int(input("Enter value of a: " ))
b = int(input("Enter value of b: " ))
k = int(input("Enter value of k: " ))

print(f"Between {a} and {b}, there are {k_divisors(a, b,k)} numbers with {k} divisors")
print(nums)
