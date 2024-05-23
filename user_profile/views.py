from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from news.models import Article, Comment
from news.forms import CommentForm


# Create your views here.
class ArticleList(generic.ListView):
    """
    Displays User profile Articles in a List View from
    :model:`news.Article`.

    **Context**

    ``queryset``
        Two filters of Article with satus 1 published
        and author logged in user.
    ``paginate_by``
        Pagination by a value of 6.
    **TEMPLATE**

    :template:`user_profile/user_profile_posts.html`
    """
    template_name = "user_profile/user_profile_posts.html"
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class CommentList(generic.ListView):
    """
    Displays User profile Comments in a List View from
    :model:`news.Comment`.

    **Context**

    ``queryset``
        A filter of testimonial with author logged in user.
    ``paginate_by``
        Pagination by a value of 6.
    **TEMPLATE**

    :template:`user_profile/user_profile_comments.html`
    """
    template_name = "user_profile/user_profile_comments.html"
    paginate_by = 6

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
