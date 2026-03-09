import math

def check_property(m, n):
    if math.gcd(m, n) == 1:
        d = math.gcd(m + n, m - n)  
        return d
    return None


pairs = [(5, 2), (7, 3), (9, 4), (15, 8), (13, 5)]

for m, n in pairs:
    result = check_property(m, n)
    if result:
        print(f"(m, n) = ({m}, {n}), gcd(m, n) = 1 -> gcd(m+n, m-n) = {result}")
