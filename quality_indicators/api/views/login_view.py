from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from rest_framework.decorators import api_view

from quality_indicators.root import settings

"""
Функция получения пары токенов JWT.
"""
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

"""
Эндпоинт для аутентификации пользователя. Принимает на вход {"email": "email", "password": "12345"}, выдает JWT токены
и записывает их в cookies.
"""
@api_view(['POST'])
def login(request, format=None):
    data = request.data
    response = Response()
    email = data.get('email', None)
    password = data.get('password', None)
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            data = get_tokens_for_user(user)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=data["access"],
                max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.set_cookie(
                key='refresh',
                value=data['refresh'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            )
            csrf.get_token(request)
            response.data = {"Success": "Login successfully", "data": data}

            return response
        else:
            return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"Invalid": "Invalid email or password!!"}, status=status.HTTP_404_NOT_FOUND)

