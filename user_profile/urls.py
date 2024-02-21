from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_post, name='user_profile'),
]