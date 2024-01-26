from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seeds the database with predefined users'

    def handle(self, *args, **options):
        usernames = ['Kevin', 'Alice', 'John', 'Emma', 'Michael', 'Sarah']  # Add the desired usernames here
        password = 'azeqsd123'  # Common password for all users

        for username in usernames:
            email = f'{username.lower()}@example.com'
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {username}'))
