from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def user_profile(request):

    if request.user.is_authenticated:
        return render(
            request,
            "user_profile/user_profile.html"
        )
    else:
        return HttpResponseRedirect('../')
