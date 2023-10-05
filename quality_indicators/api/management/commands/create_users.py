from django.core.management.base import BaseCommand
from quality_indicators.api.services.user_service import UserService


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        UserService().create_user(email='test1@test.ru', password='12345')
        UserService().create_user(email='test2@test.ru', password='12345')
        self.stdout.write('Users created')
