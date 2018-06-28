n = int(input("enter your number:"))

if n % 2 == 0:
    for i in range(n // 2):
        i = 1
        print(i, end = " ")
        for k in range(n // 2):
            k = 0
        print(k, end = " ")
else:
    for i in range(n // 2):
        i = 1
        print(i, end = " ")
        for k in range((n // 2) - 1):
            k = 0
        print(k, end = " ")
