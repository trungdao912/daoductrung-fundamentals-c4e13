n = int(input("Enter your number:"))

if n % 2 == 0:
    for i in range(n // 2):
        print(1, end = " ")
        print(0, end = " ")
else:
    for k in range(n // 2):
        print(1, end = " ")
        print(0, end = " ")
    print(1)