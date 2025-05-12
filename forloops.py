for i in range(10):
    print(i)

name = "Buuny"

for i in name:
    # instead of printing in new line it prints ends
    print(i,end=",")


colors = ["Blue", "Green", "Yellow", "Black"]
for color in colors:
    print(color)
    if color == "Blue":
        print(f"{color} Is my favorite color")

for color in colors:
    #Iterates against each item in the list
    print(color)
    #Now, the color is a string and it iterates against each letter
    for i in color:
        print(i)

for i in range(1, 10, 5):
    print(i)
    