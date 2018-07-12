month = int(input("enter numbers of month:"))
def F(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    elif n == 2:
        return 2
    else: 
        return F(n - 1) + F(n - 2)

for i in range(month):
    print("Month {0}: {1} pair(s) of rabbit".format(i, F(i + 1)))
