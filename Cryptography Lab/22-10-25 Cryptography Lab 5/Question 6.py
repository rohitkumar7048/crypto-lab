import math

def GCD(nums):
    ans = nums[0]
    for i in range(1, len(nums)):
        ans = math.gcd(ans, nums[i])
    return ans


nums = [int(x) for x in input("Enter numbers: ").split()]
print(f"GCD of {nums} = {GCD(nums)}")