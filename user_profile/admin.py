from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# Register your models here.
@admin.site.register(Post)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)