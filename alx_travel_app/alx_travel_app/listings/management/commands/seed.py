from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        host = User.objects.first()
        if not host:
            host = User.objects.create_user(username='hostuser', email='host@example.com', password='password123')

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                location=fake.city(),
                price_per_night=random.uniform(50, 500),
                host=host
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
