from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
]