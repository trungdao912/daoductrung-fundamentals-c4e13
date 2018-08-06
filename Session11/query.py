from models.customer import *
import mlab

mlab.connect()

id_to_find = "5b5f1528d7aadc29a4369fd5"

# customer = Customer.objects.get(id=id_to_find)
# customer = Service.objects.with_id("5b650621d7aadc2d40482945")
# all_service = Service.objects()

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







