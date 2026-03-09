def Euclids_GCD(a,b):
    if b == 0:
        return a,1,0
    else:
        d, x1, y1 = Euclids_GCD(b , a%b)
        x = y1
        y = x1 - (a//b)*y1
        return d,x,y
    
a = 85
b = 289

d,x,y = Euclids_GCD(a,b)

print(f"GCD of {a} and {b} = {d}")
print(f"x = {x} and y = {y} such that {a}*({x}) + {b}*({y}) = {d}")