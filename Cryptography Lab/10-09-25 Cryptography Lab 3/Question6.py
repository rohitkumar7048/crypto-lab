a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if a > b:
    a, b = b, a

count = 0
nums = []

for num in range(a, b + 1):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        count += 1
        nums.append(num)


print(f"There are {count} numbers in between the entered numbers that are divisible by 2,3 or 5")
print(nums)
