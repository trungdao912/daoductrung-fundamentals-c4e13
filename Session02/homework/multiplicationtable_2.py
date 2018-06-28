number = int(input("Enter your number:"))

for k in range(1,number + 1):
    for i in range(1,number + 1):
        print(i * k, end = "\t")
    print()