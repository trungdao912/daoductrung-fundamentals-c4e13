from models.service import Service, Customer
import mlab

mlab.connect()

all_service = Service.objects()
all_customer = Customer.objects()

# print(all_customer[0]["id"])

Customer.objects(id="5b5f1527d7aadc29a4369fd1").delete()