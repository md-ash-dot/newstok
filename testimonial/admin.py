from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'status', 'created_on')
    search_fields = ['name', 'email']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('testimonial',)

    

# Register your models here.
