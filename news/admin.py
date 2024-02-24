from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on', 'category')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
#admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('article', 'author', 'created_on', 'approved',)
    search_fields = ['article', 'author']
    list_filter = ('approved', 'created_on',)