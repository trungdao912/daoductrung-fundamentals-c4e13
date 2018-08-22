# read
item = ["tshirt", "sweater"]

print(*item, sep = ", ")

# create
new = input("enter your new item:")

item.append(new) 
print(*item, sep = ", ")

# update position

new_item = input("enter your item:")
pos = int(input("enter your pos you want to replace:"))

item [pos - 1] = new_item

for i,k in enumerate(item, 1):
    print(*item, sep = ", ")

# delete

new_item = ["tshirt", "sweater", "skirt"]

pos = int(input("enter pos you want to delete:"))

del new_item[pos]

print(*new_item, sep =", ")
