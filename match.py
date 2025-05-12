x = int(input("Enter any number: "))

# x is the variable to match
match x:
    #if x is equal to 0
    case 0:
        print(x, "is equal to zero!")
    case 4 if x % 2 == 0:
        print(x, "is equal to 4")
    # this is default match and if there not case found by default it picks up this case
    case _:
        print(x)