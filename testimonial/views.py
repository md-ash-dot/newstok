from django.shortcuts import render
from django.views import generic
from .models import Testimonial

# Create your views here.

class TestimonialList(generic.ListView):
    queryset = Testimonial.objects.filter(status=1)
    template_name = "testimonial_list.html"