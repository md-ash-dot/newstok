from .models import Comment, Article
from django import forms
from django_summernote.widgets import SummernoteWidget

class CommentForm(forms.ModelForm):
    """
    Form for :model:`news.Comment`
    """
    class Meta:
        model = Comment
        fields = ('body',)


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    """
    Form for :model:`news.Article`
    """
    class Meta:
        model = Article
        fields = ('title', 'category', 'content',)
