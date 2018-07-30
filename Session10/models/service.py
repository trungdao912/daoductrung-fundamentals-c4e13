from mongoengine import*
# design database


class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

class Customer(Document):
    name = StringField()
    gender = IntField()
    email = EmailField()
    contacted = BooleanField()
    job = StringField()
    company = StringField()
    phone = StringField()
    
    