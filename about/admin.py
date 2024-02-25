from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Registers About in admin for :model:`about.About` and SummernoteModelAdmin

    **Context**

    ``summernote_fields``
        SummernoteModelAdmin for content.
    """

    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Registers CollaborateRequest in admin for :model:`about.CollaborateRequest`

    **Context**

    ``list_display``
        list diplay for message and read fields.
    """

    list_display = ('message', 'read',)
