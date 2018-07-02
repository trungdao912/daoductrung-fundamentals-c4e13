# 2.1
ship_size = [5, 7, 300, 90, 24, 50, 75]
default_size = 8
print("Hello, my name is Trung and these are my ship size \n",ship_size)
print("Now my biggest sheep has size {0} let's shear it".format(max(ship_size)))
ship_size[ship_size.index(max(ship_size))] = default_size
print("After shearing, here is my flock \n",ship_size)
