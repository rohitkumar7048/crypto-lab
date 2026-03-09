from math import gcd

def find_gcd_of_list(numbers):
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = gcd(current_gcd, num)
    return current_gcd


nums = list(map(int, input("Enter integers separated by space: ").split()))

if len(nums) < 2:
    print("Please enter at least two integers.")
else:
    result = find_gcd_of_list(nums)
    print(f"The GCD of {nums} is {result}")

