
for i in range(5):
    for k in range(5):
        if k < 5 - i - 1:
            print(" ", end = "")
        else:
            print("x ", end = "")

    print()