from .models import Testimonial
from django import forms


class TestimonialForm(forms.ModelForm):
    """
    Form for :model:`testimonial.Testimonial`
    """
    class Meta:
        model = Testimonial
        fields = ('name', 'email', 'testimonial', 'rating',)