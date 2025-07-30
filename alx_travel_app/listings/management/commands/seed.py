from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            self.stdout.write(self.style.ERROR("No users exist. Please create a user first."))
            return

        host = User.objects.first()

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                price_per_night=random.randint(50, 300),
                location=fake.city(),
                host=host
            )

        self.stdout.write(self.style.SUCCESS("Seeded database with sample listings."))
