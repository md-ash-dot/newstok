from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm, ArticleForm

# Create your views here.


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1)
    template_name = "news/index.html"
    paginate_by = 6
"""     context_object_name = 'lists'

    def get_queryset(self):
        myset = {
            "general": Article.objects.filter(category=0),
            "technology": Article.objects.filter(category=1),
        } """


def article_detail(request, slug):
    """
    Display an individual :model:`article.Post`.

    **Context**

    ``article``
        An instance of :model:`article.Post`.

    **Template:**

    :template:`news/article_detail.html`
    """

    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comments = article.comments.all().order_by("-created_on")
    comment_count = article.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "news/article_detail.html",
        {
            "article": article,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def upvote_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    if not article.has_user_upvoted(request.user):
        article.upvotes += 1
        article.upvoted_users.add(request.user)
        article.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def downvote_article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if not article.has_user_downvoted(request.user):
        article.downvotes += 1
        article.downvoted_users.add(request.user)
        article.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user and request.user.is_authenticated:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    

def new_article(request):
    """
    view to delete comment
    """
    if request.method == "POST":
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            
    article_form = ArticleForm()

    return render(
        request,
        "news/new_article.html",
        {   
            "new_article": new_article,
            "article_form": article_form
        },
    )
