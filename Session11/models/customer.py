
#desgin data base
from mongoengine import *
class Customer(Document):
    name = StringField()
    gender = IntField()
    email = EmailField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()

class Service(Document):
    name = StringField()
    yob = IntField()
    height = IntField()
    image = StringField()
    description = StringField()
    measurements = ListField()

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()


# new_service = Service(
#     name = "KennyZ",
#     yob = 1992,
#     gender = 0,
#     height = 165,
#     phone = "098583712",
#     address = "Aus",
#     status = True
# )

# new_service.save()
