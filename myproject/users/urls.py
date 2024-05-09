from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.display_users),
    path('register',views.register_user),
]
