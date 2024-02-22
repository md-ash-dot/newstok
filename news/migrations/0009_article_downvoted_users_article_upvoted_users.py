# Generated by Django 4.2.10 on 2024-02-22 20:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0008_article_downvotes_article_upvotes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='downvoted_users',
            field=models.ManyToManyField(blank=True, related_name='downvoted_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='upvoted_users',
            field=models.ManyToManyField(blank=True, related_name='upvoted_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
