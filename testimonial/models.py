from django.db import models

RATING = ((0, "0 STAR"), (1, "1 STAR"), (2, "2 STARS"), (3, "3 STARS"), (4, "4 STARS"), (5, "5 STARS"))
STATUS = ((0, "Not Published"), (1, "Published"))


# Create your models here.
class Testimonial(models.Model):
    """
    Stores a single testimonial entry.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    testimonial = models.TextField()
    rating = models.IntegerField(choices=RATING, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
