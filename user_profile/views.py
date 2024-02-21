from django.shortcuts import render
from .models import Post


# Create your views here.

def user_post(request):
    """
    Renders the User Profile page
    """
    post = Post.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "user_profile/user_profile.html",
        {"user_profile": user_profile},
    )