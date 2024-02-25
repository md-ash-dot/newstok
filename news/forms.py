from .models import Comment, Article
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for :model:`news.Comment`
    """
    class Meta:
        model = Comment
        fields = ('body',)


class ArticleForm(forms.ModelForm):
    """
    Form for :model:`news.Article`
    """
    class Meta:
        model = Article
        fields = ('title', 'category', 'content',)
