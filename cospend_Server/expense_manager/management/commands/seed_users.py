from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seeds the database with users'

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help='The number of fake users to create')

    def handle(self, *args, **options):
        num_users = options['num_users']
        for _ in range(num_users):
            username = f'user_{random.randint(1, 10000)}'
            email = f'{username}@example.com'
            # password = User.objects.make_random_password()
            password = 'azeqsd123'
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {username}'))
