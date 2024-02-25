from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='user_profile_posts'),
    path('comments', views.CommentList.as_view(), name='user_profile_comments')
]
