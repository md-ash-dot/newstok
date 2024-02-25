from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from .models import Testimonial
from .forms import TestimonialForm


# Create your views here.
class TestimonialList(generic.ListView):
    """
    Displays Testimonials in a List View from
    :model:`testimonial.Testimonial`.
    `
    **Context**

    ``queryset``
        A filter of testimonial with satus 1 published.
    **TEMPLATE**

    :template:`testimonial_list.html`
    """
    queryset = Testimonial.objects.filter(status=1)
    template_name = "testimonial_list.html"


def testimonial(request):
    """
    Renders the Testimonial form page for users to submit a testimonial.

    **Context**

    ``testimonial_form``
        The instance of :form:`testimonial.TestimonialForm`.
    **TEMPLATE**

    :template:`testimonial/new_testimonial.html`
    """
    if request.method == "POST":
        testimonial_form = TestimonialForm(data=request.POST)
        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.save()
            messages.success(request, "Your testimonial form has been submitted")
            return redirect("testimonial")
    else:
        testimonial_form = TestimonialForm()

    return render(
        request,
        "testimonial/new_testimonial.html",
        {
            "testimonial_form": testimonial_form
        },
    )
