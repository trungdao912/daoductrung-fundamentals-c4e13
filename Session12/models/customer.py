import datetime
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

class User(Document):
    username = StringField()
    password = StringField()
    email = EmailField()

class Order(Document):
    service_id = ReferenceField(Service)
    is_accepted = BooleanField()
    user_id = ReferenceField(User)
    time = DateTimeField()

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
