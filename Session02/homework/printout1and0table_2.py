n = int(input("enter your number:"))

if n % 2 == 0:
    for k in range(n // 2):
        for i in range(n // 2):
            a = 1
            b = 0
            print(a, b, end = " ")
        print()
        for j in range(n // 2):
            a = 1
            b = 0
            print(b, a, end = " ")
        print()
else:
    for k in range(n // 2):
        for i in range(n // 2):
            a = 1
            b = 0
            print(a, b, end = " ")
        print(1)
        for j in range(n // 2):
            a = 1
            b = 0
            print(b, a, end = " ")
        print(0)