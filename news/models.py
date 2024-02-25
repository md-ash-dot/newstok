from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = ((0, "General"), (1, "Technology"), (2, "Business"), (3, "Science"))

# Create your models here.
class Article(models.Model):
    """
    Stores a single article entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_articles")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    upvoted_users = models.ManyToManyField(User, related_name='upvoted_articles', blank=True)
    downvoted_users = models.ManyToManyField(User, related_name='downvoted_articles', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    def total_votes(self):
        return self.upvotes + self.downvotes
    def score(self):
        return self.upvotes - self.downvotes
    def has_user_upvoted(self, user):
        return user in self.upvoted_users.all()
    def has_user_downvoted(self, user):
        return user in self.downvoted_users.all()

    

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`news.article`.
    """
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"