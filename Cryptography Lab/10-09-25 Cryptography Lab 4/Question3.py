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
 

def generate_primes(limit):
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    return primes

def find_primes_sum_and_difference(limit):
    primes = generate_primes(limit)
    prime_set = set(primes)
    result = set()
    
    for p in primes:
        sum_found = False
        diff_found = False
        pairSum = None
        pairDiff = None
        
        # Chek Sum
        for p1 in primes:
            p2 = p - p1
            if p2 in prime_set:
                sum_found = True
                break
        
        #check if p can be written as a difference of two primes
        for p3 in primes:
            p4 = p3 - p
            if p4 in prime_set:
                diff_found = True
                break
        
        if sum_found and diff_found:
            result.add(p)
    
    return sorted(result)

limit = int(input("Enter limit: "))
primes = find_primes_sum_and_difference(limit)
print("Primes that can be represented both as sums and differences of two primes:")
print(primes)





# def generate_primes(limit):
#     nums = []
#     for i in range (2 , limit +1):
#         if is_prime(i):
#             nums.append(i)
#     return nums

# def Sum_and_diff(limit):
#     primes = generate_primes(limit)
#     primes_set = set(primes)
#     result = set()

#     for p in primes:
#         sumFound = False
#         diffFound = False


#         for p1 in primes:
#             p2 = p - p1
#             if p2 in primes_set:
#                 sumFound = True
#                 break

#         for p3 in primes:
#             p4 = p3 - p
#             if p4 in primes_set:
#                 diffFound = True
#                 break

#         if sumFound and diffFound:
#             result.add(p)

#     return sorted(result)
    




# limit = int(input("Enter primes upto: "))
# print("Primes that can be represented both as sums and differences of two primes:")
# print(Sum_and_diff(limit))
