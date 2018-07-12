numbers = [1, 6, 8, 1, 2, 1, 5, 6]
 
d = {}
loop = True

for i in numbers:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

while loop:
    number = int(input("enter your number"))
    if number not in numbers:
        break
    print("{0} appear {1} in my list".format(number, d[number]))
