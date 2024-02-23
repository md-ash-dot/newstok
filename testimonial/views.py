from django.shortcuts import render
from django.views import generic
from .models import Testimonial

# Create your views here.

class TestimonialList(generic.ListView):
    queryset = Testimonial.objects.filter(status=1)
    template_name = "testimonial_list.html"

def open_testimonial(request):
    """
    Renders the Testimonial page
    """
    testimonial = Testimonial.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "testimonial/testimonial.html",
        {"testimonial": testimonial},
    )