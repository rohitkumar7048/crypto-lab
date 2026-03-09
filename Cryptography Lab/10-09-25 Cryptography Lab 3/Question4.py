N = int(input("Enter the number of elements: "))


A = list(map(int, input("Enter the elements separated by space: ").split()))


if len(A) != N:
    print(f"Please enter exactly {N} elements.")
else:

    last_digits = [str(num % 10) for num in A]
    formed_number_str = ''.join(last_digits)
    

    formed_number = int(formed_number_str)

    if formed_number % 10 == 0:
        result = "is divisible by 10."
    else:
        result = "is not divisible by 10."
    

    print(f"Last digits: {last_digits}")
    print(f"Formed number: {formed_number}")
    print(f"The formed number {result}")






# nums = [str(int(num)%10) for num in input("Enter numbers: ").split()]
# formed_no_str = ''.join(nums)
# joined_no = int(formed_no_str)


# print(nums)
# print(formed_no_str)

# if(joined_no % 10 ==0):
#     print("Divisible")
# else:
#     print("Not divisible")
