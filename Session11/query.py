from models.customer import *
import mlab

mlab.connect()

id_to_find = "5b5f1528d7aadc29a4369fd5"

# customer = Customer.objects.get(id=id_to_find)
# customer = Service.objects.with_id("5b650621d7aadc2d40482945")

# print(customer.name)
# print(customer.to_mongo())

# Delete
# if customer is not None:
#     customer.delete()
#     print("Deleted")
# else:
#     print("Not found")

# Update

# print(customer.to_mongo())

# customer.update(set__name="Trung")
# customer.reload()

# print(customer.to_mongo())

# print(len(all_customer))

# #EX 8
# all_river = River.objects(continent = "Africa")
# for river in all_river:
#     print(river["name"])

#EX 9
# Sriver = River.objects(continent = "S. America")
# for river in Sriver:
#     if river["length"] >= 1000:
#         continue
#     print(river["name"])





