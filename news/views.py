from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Article, Comment
from .forms import CommentForm, ArticleForm


# Create your views here.


class ArticleList(generic.ListView):
    """
    Displays Articles in a List View.

    **Context**

    ``queryset``
        A filter of articles with satus 1 published.
    ``paginate_by``
        Pagination by a value of 6.
    **Template:**

    :template:`news/index.html`
    """
    queryset = Article.objects.filter(status=1)
    template_name = "news/index.html"
    paginate_by = 6


class ArticleListByGeneral(generic.ListView):
    """
    Displays General Articles in a List View.

    **Context**

    ``queryset``
        Two filters of articles with satus 1 published and category 0.
    ``paginate_by``
        Pagination by a value of 6.
    **Template:**

    :template:`news/index.html`
    """
    queryset = Article.objects.filter(status=1).filter(category=0)
    template_name = "news/index.html"
    paginate_by = 6


class ArticleListByTechnology(generic.ListView):
    """
    Displays Technology Articles in a List View.

    **Context**

    ``queryset``
        Two filters of articles with satus 1 published and category 1.
    ``paginate_by``
        Pagination by a value of 6.
    **Template:**

    :template:`news/index.html`
    """
    queryset = Article.objects.filter(status=1).filter(category=1)
    template_name = "news/index.html"
    paginate_by = 6


class ArticleListByBusiness(generic.ListView):
    """
    Displays Business Articles in a List View.

    **Context**

    ``queryset``
        Two filters of articles with satus 1 published and category 2.
    ``paginate_by``
        Pagination by a value of 6.
    **Template:**

    :template:`news/index.html`
    """
    queryset = Article.objects.filter(status=1).filter(category=2)
    template_name = "news/index.html"
    paginate_by = 6


class ArticleListByScience(generic.ListView):
    """
    Displays Science Articles in a List View.

    **Context**

    ``queryset``
        Two filters of articles with satus 1 published and category 3.
    ``paginate_by``
        Pagination by a value of 6.
    **Template:**

    :template:`news/index.html`
    """
    queryset = Article.objects.filter(status=1).filter(category=3)
    template_name = "news/index.html"
    paginate_by = 6


def article_detail(request, slug):
    """
    Display an individual :model:`news.Article`.

    **Context**

    ``article``
        An instance of :model:`news.Article`.
    ``comments``
       All comments related to the article, ordered by creation date.
    ``comment_count``
        A count of approved comments related to the article.
    ``comment_form``
        An instance of :form:`news.CommentForm`.

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

@login_required
def upvote_article(request, slug):
    """
    Up-vote an individual article.

    **Context**

    ``article``
        An instance of :model:`news.Article`.
    """
    article = get_object_or_404(Article, slug=slug)

    if request.user in article.upvoted_users.all():
        """ If the user has already upvoted, remove the upvote """
        article.upvotes -= 1
        article.upvoted_users.remove(request.user)
    else:
        """ If the user hasn't upvoted, add the upvote """
        article.upvotes += 1
        article.upvoted_users.add(request.user)
        """ If the user had previously downvoted, remove the downvote """
        if request.user in article.downvoted_users.all():
            article.downvotes -= 1
            article.downvoted_users.remove(request.user)

    article.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def downvote_article(request, slug):
    """
    Down-vote an individual article.

    **Context**

    ``article``
        An instance of :model:`news.Article`.
    """
    article = get_object_or_404(Article, slug=slug)

    if request.user in article.downvoted_users.all():
        """ If the user has already downvoted, remove the downvote """
        article.downvotes -= 1
        article.downvoted_users.remove(request.user)
    else:
        """ If the user hasn't downvoted, add the downvote """
        article.downvotes += 1
        article.downvoted_users.add(request.user)

        """ If the user had previously upvoted, remove the upvote """
        if request.user in article.upvoted_users.all():
            article.upvotes -= 1
            article.upvoted_users.remove(request.user)

    article.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``article``
        An instance of :model:`news.Article`.
    ``comment``
        A single comment related to the article.
    ``comment_form``
        An instance of :form:`news.CommentForm`.
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

@login_required
def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``article``
        An instance of :model:`news.Article`.
    ``comment``
        A single comment related to the article.
    """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def new_article(request, slug=None):
    """
    Display a form for submitting a new article to :model:`news.Article` or editing an existing article.

    **Context**

    ``article``
        An instance of :model:`news.Article`, if editing an existing article.
    ``article_form``
        An instance of :form:`news.ArticleForm`.

    **Template:**

    :template:`news/new_article.html`
    """
    if slug:
        article = get_object_or_404(Article, slug=slug)
    else:
        article = None

    if request.method == "POST":
        article_form = ArticleForm(data=request.POST, instance=article)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.slug = slugify(article.title)
            article.author = request.user

            # Set approved to False when editing
            if slug:
                article.approved = False

            article.save()
            messages.success(request, 'Article submitted successfully and is awaiting approval.' 
            if not slug else 'Article updated successfully and is awaiting approval.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        article_form = ArticleForm(instance=article)

    return render(
        request,
        "news/new_article.html",
        {
            "new_article": new_article,
            "article_form": article_form
        },
    )

@login_required
def delete_article(request, slug):
     """
    Delete an individual article.

    **Context**

    ``article``
        An instance of :model:`news.Article`.

    **Template:**

    :view:`user_profile_posts`
    """
    article = get_object_or_404(Article, slug=slug)

    if article.author == request.user:
        article.delete()
        messages.add_message(request, messages.SUCCESS, 'Article deleted successfully!')
    else:
        messages.add_message(request, messages.ERROR, 'You do not have permission to delete this article.')

    return HttpResponseRedirect(reverse('user_profile_posts'))