a = int(input("Enter value of a: " ))
b = int(input("Enter value of b: " ))

if b == 0:
    print("Division by zero not allowed")

elif a % b == 0:
    print(str(b) + " divides " +  str(a))

else:
    print(str(b) + " Doesnt divides " +  str(a))