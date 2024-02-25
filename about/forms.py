from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form for :model:`about.CollaborateRequest`
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')