from django.urls import path,include
from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.register_user, name="register"),
    path('login/',views.log_in, name="login"),
]
