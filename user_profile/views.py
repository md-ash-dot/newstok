from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from news.models import Article, Comment
from news.forms import CommentForm


class ArticleList(generic.ListView):
    template_name = "user_profile/user_profile_posts.html"
    paginate_by = 6
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

class CommentList(generic.ListView):
    template_name = "user_profile/user_profile_comments.html"
    paginate_by = 6
    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)





# Create your views here.
""" def user_profile(request):

    if request.user.is_authenticated:
        return render(
            request,
            "user_profile/user_profile.html"
        )
    else:
        return HttpResponseRedirect('../')
 """