i = 0
while (i < 3): # this prints till i is less than 3
    print(i)
    i += 1

a = 0
while (a <= 3): # this prints till "a" is less than and equal to 3
    print(a)
    a += 1


myinput = int(input("Enter a number: "))
while myinput <= 69:
    print(myinput)
    myinput = int(input("Enter a number: "))
    if myinput >=70:
        print("loop exited")


my_num = 5
while (my_num > 0):
    print(my_num)
    my_num = my_num - 1
# else gets executed after the while loop is completed!
else:
    print(f"We are not outside the while loop and value of {my_num} is 0")


## Emulating Do while loop, Irrespective of condition the first iteration prints
i = 0
while True:
    print(i)
    i += 1
    if (i == 10):
        break
