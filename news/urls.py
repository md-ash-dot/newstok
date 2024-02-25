from . import views
from django.urls import path

urlpatterns = [
     path('', views.ArticleList.as_view(), name='home'),
     path('<slug:slug>/', views.article_detail, name='article_detail'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
          views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
          views.comment_delete, name='comment_delete'),
     path('article', views.new_article, name='new_article'),
     path('<slug:slug>/upvote/', views.upvote_article, name='upvote_article'),
     path('<slug:slug>/downvote/', views.downvote_article, name='downvote_article'),
     path('category/general', views.ArticleListByGeneral.as_view(), name='general'),
     path('category/business', views.ArticleListByBusiness.as_view(), name='business'),
     path('category/technology', views.ArticleListByTechnology.as_view(), name='technology'),
     path('category/science', views.ArticleListByScience.as_view(), name='science'),
]
