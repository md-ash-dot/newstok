from django.shortcuts import render
from django.views import generic
from .models import Testimonial
from .forms import TestimonialForm

# Create your views here.

class TestimonialList(generic.ListView):
    queryset = Testimonial.objects.filter(status=1)
    template_name = "testimonial_list.html"

def testimonial(request):
    """
    Renders the Testimonial page
    """
    if request.method == "POST":
        testimonial_form = TestimonialForm(data=request.POST)
        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.save()

    testimonial_form = TestimonialForm()

    return render(
        request,
        "testimonial/testimonial.html",
        {
            "testimonial": testimonial,
            "testimonial_form": testimonial_form
        },
    )


    """ testimonial = Testimonial.objects.all().order_by('-updated_on').first() """