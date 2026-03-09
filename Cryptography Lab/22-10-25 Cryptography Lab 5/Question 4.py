import math
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n %2 == 0: return False
    for i in range(3, math.isqrt(n)+1):
        if(n % i == 0):
            return False
    return True
    
n = int(input("Enter a number: "))
if(is_prime(n)):
    print(f"{n} is Prime")
else: 
    print(f"{n} is not Prime")