from . import views
from django.urls import path

urlpatterns = [
    path('', views.TestimonialList.as_view(), name='testimonial'),
    path('new', views.testimonial, name='new_testimonial')
]