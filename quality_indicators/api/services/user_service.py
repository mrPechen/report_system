from typing import Any

from quality_indicators.api.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    """
    Доступ к запросу на регистрацию пользователя.
    """
    def create_user(self, email: str, password: Any):
        return self.user_repository.create_user(email=email, password=password)
