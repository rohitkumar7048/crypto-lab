def min_operations(A, B):
    steps = 0
    while A % 3 != 0 and B % 3 != 0:
        if A > B:
            A = abs(A - B)
        else:
            B = abs(A - B)
        steps += 1
    return steps


a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))


print("Min no of operations: " ,min_operations(a, b))  
