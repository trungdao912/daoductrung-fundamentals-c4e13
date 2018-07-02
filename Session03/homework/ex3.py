ship_size = [5, 7, 300, 90, 24, 50, 75]
default_size = 8
print("Hello, my name is Trung and these are my ship size\n",ship_size)

for i in range(1,5):    
    print("Month",i)
    ship_size = [(x + 50) for x in ship_size]
    print("One month has passed, here is my new flock \n{0}".format(ship_size))
    ship_size[ship_size.index(max(ship_size))] = default_size
    print("After shearing, here is my flock \n",ship_size)
    total_money = sum(ship_size) * 2
    print("My flock has size in total {0}\n I would get {1} $".format(sum(ship_size), total_money))
    
