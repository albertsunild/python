for i in range(1, 13):
    print(f" 5 X {i} = {5 * i} ")
    if (i == 10):
        break # exits

for i in range(1, 12):
    if (i == 10):
        print(f" we are skipping the iteration")
        continue # breaking out of the iteration// skips it
    print(f"6 X {i} = {6 * i}")

