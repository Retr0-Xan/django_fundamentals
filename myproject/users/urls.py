from django.urls import path,include
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.display_users),
    path('register',views.register_user, name="register"),
]
