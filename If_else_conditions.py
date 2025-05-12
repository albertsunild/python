my_num = int(input("Enter your age: "))
print(f"your age is {my_num}")

# conditional operators ==; !=; <=; >=; >; <
print(my_num == 18)
print(my_num != 18)
print(my_num <= 18)
print(my_num >= 18)
print(my_num > 18)
print(my_num < 18)

if (my_num < 0):
    print(f"{my_num} is a negative number")
elif (my_num > 0):
    if my_num <= 10:
        print(f"{my_num} is between 1 - 10")
    elif (my_num >= 10 and my_num <= 20):
        print(f"{my_num} is between 11 - 20")
    else:
        print(f"{my_num} is greater than 20")
else:
    print(f"{my_num} is more than zero")