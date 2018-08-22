loop = True

while loop:
    bacteria_numer = int(input("how many bacteria are there:"))
    time = int(input("how long will we wait:"))
    print("after {0}, we would have {1} bacteria".format(time, bacteria_numer * ( 2 ** int(time / 2))))
    print("continue(Y/N)")
    a = input().lower()
    if a == "y":
        continue
    else:
        break
