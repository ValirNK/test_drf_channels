import random
from datetime import datetime
import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from market.models import Client, Product, Type
from django.forms.models import model_to_dict

MANUFACTURERS = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]

CURRENCY = [
    "rub",
    "eur",
    "usd"
]

TYPES = [
    "Notebooks",
    "Smartphones",
    "Tablets",
    "PC",
    "Television",
    "Microphones"
]


class Provider(faker.providers.BaseProvider):
    def manufacturers(self):
        return self.random_element(MANUFACTURERS)
    def currency(self):
        return self.random_element(CURRENCY)

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(["en_US"])
        fake.add_provider(Provider)

        for tp in TYPES:
            tps = Type.objects.filter(name=tp)
            if len(tps) == 0:
                Type.objects.create(name=tp)

        for _ in range(80):

            manufacture = fake.manufacturers()
            currency = fake.currency()
            name = fake.name()
            random_object = Type.objects.all()[random.randint(0, Type.objects.all().count() - 1)]
            Product.objects.create(
                name=name,
                price=random.randint(250, 2150),
                manufacturer=manufacture,
                currency=currency,
                in_stock=random.randint(5, 120),
                code=str(random.randint(1000000000, 100000000000)),
                date_update=datetime.now(),
                type_product=random_object,
                image="/Screenshot_from_2023-01-16_20-19-21_4KKhqQE.png"
            )


        self.stdout.write(self.style.SUCCESS(f"Number of products: {Product.objects.all().count()}"))