from quality_indicators.api.services.user_service import UserService
from rest_framework.decorators import api_view
from rest_framework.response import Response

"""
Эндпоинт для регистрации нового пользователя.
"""


@api_view(['POST'])
def register_user(request):
    email = request.data['email']
    password = request.data['password']
    UserService().create_user(email=email, password=password)
    return Response({"ok": "ok"})
