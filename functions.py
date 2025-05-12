#Finds geometry mean of the two value
def calculateGmean(a,b):
    result = (a*b)/(a+b)
    return result

my_result = calculateGmean(6,9)
print(my_result)


#checks which number is greater than other
def isGreater(a,b):
    if (a>b):
        print(f"{a} is greater than {b} which is the first number")
    elif (a<b):
        print(f"{b} is greater than {a} which is the second number")
    else:
        print(f"{a} is equal to {b}")

isGreater(8,9)