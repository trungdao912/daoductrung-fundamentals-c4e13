from models.customer import Service
import mlab
from faker import Faker
from random import randint, choice

fake = Faker()

mlab.connect()
for i in range(50):
    print(i+1)
    new_service = Service(
        name = fake.name(),
        yob = randint(1990, 2000),
        height = randint(150, 190),
        description = "Ngoan Hien Le Phep",
        image = "http://images6.fanpop.com/image/photos/40800000/jennie-black-pink-40840931-375-500.jpg",
        measurements = [90,60,90]
    )
    new_service.save()
new_service.save()
