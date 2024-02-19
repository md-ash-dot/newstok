from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article

# Create your views here.


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1)
    template_name = "news/index.html"
    paginate_by = 6


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

    return render(
        request,
        "news/article_detail.html",
        {
            "article": article,
            "comments": comments,
            "comment_count": comment_count,
        },
    )