from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Testimonial


# Register your models here.
@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    """
    Registers TestimonialAdmin in admin for :model:`testimonial.Testimonial` and SummernoteModelAdmin

    **Context**

    ``list_display``
        list diplay for name, email, status and created_on fields.
    ``search_fields``
        search for name and email fields.
    ``list_filter``
        list by filter for status and created_on.
    ``summernote_fields``
        SummernoteModelAdmin for testimonial.
    """

    list_display = ('name', 'email', 'status', 'created_on')
    search_fields = ['name', 'email']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('testimonial',)

    


