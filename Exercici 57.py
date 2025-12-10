linies = 4

for i in range(1, linies + 1):
    if i <= 3:
        print("*" * i)
    else:
        print("*" * (linies - i))
