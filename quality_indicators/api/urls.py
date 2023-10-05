from django.urls import path

from quality_indicators.api.views import login_view, register_user_view, objects_view


urlpatterns = [
    path('login', login_view.login, name="login"),
    path('registration', register_user_view.register_user),
    path('report/<str:date>', objects_view.show_report),
    path('add', objects_view.add_objects),
]
