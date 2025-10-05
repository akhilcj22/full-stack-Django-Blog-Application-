from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Delete a user by username'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username to delete')

    def handle(self, *args, **options):
        username = options['username']
        
        try:
            user = User.objects.get(username=username)
            user.delete()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully deleted user: {username}')
            )
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'User "{username}" does not exist')
            )
