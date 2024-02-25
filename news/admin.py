from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Comment


# Register your models here.
@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    """
    Registers ArticleAdmin in admin for :model:`news.Article`
    and SummernoteModelAdmin

    **Context**

    ``list_display``
        list diplay for title, status, created_on,
        category and approved fields.
    ``search_fields``
        search for title and content fields.
    ``list_filter``
        list by filter for status, approved and created_on.
    ``summernote_fields``
        SummernoteModelAdmin for content.
    """

    list_display = ('title', 'status', 'created_on', 'category', 'approved',)
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'approved')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Registers CommentAdmin in admin for :model:`news.Comment`
    and SummernoteModelAdmin

    **Context**

    ``list_display``
        list diplay for article, author, created_on and approved fields.
    ``search_fields``
        search for article and author fields.
    ``list_filter``
        list by filter for approved and created_on.
    """

    list_display = ('article', 'author', 'created_on', 'approved')
    search_fields = ['article', 'author']
    list_filter = ('approved', 'created_on',)
