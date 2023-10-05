from typing import Any

from quality_indicators.api.models import User


class UserRepository:
    def __init__(self):
        self.user_model = User

    """
    Запрос для регистрации пользователя.
    """

    def create_user(self, email: str, password: Any):
        user = self.user_model.objects.create(email=email)
        user.set_password(password)
        user.save()
        return user
