from django.core.management.base import BaseCommand
from userauths.models import User, UserToken
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Generate UserTokens for existing users who do not have one'

    def handle(self, *args, **kwargs):
        users_without_token = User.objects.filter(token__isnull=True)
        for user in users_without_token:
            UserToken.objects.create(user=user, token=get_random_string(length=64))
        self.stdout.write(self.style.SUCCESS('Successfully generated UserTokens for existing users'))
