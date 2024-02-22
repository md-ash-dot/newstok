# Generated by Django 4.2.10 on 2024-02-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.IntegerField(choices=[(0, 'General'), (1, 'Technology'), (2, 'Business'), (3, 'Science')], default=0),
        ),
    ]