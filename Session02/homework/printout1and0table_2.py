n = int(input("enter your number:"))

a = 1
b = 0

if n % 2 == 0:
    for k in range(n // 2):
        for i in range(n // 2):
            print(a, b, end = " ")
        print()
        for j in range(n // 2):
            print(b, a, end = " ")
        print()
else:
    for k in range(n // 2):
        for i in range(n // 2):
            print(a, b, end = " ")
        print(1)
        for j in range(n // 2):
            print(b, a, end = " ")
        print(0)
    for m in range(n // 2):
        print(a, b, end = " ")
    print(1)
