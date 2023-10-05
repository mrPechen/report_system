from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from quality_indicators.root import settings

"""
Проверка csrf токена
"""


def enforce_csrf(request):
    check = CSRFCheck(request)
    check.process_request(request)
    reason = check.process_view(request, None, (), {})
    if reason:
        raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)


"""
Обновление истекшего access jwt токена.
"""


def refresh(token):
    result = TokenRefreshSerializer().validate({'refresh': f'{token}'})
    return result['access']


"""
Проверка аутентификации.
"""


class CustomAuthentication(JWTAuthentication):

    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        try:
            validated_token = self.get_validated_token(raw_token)
            enforce_csrf(request)
            return self.get_user(validated_token), validated_token
        except Exception:
            refresh_token = request.COOKIES.get('refresh')
            request.COOKIES['access_token'] = refresh(refresh_token)
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
            validated_token = self.get_validated_token(raw_token)
            enforce_csrf(request)
            return self.get_user(validated_token), validated_token
