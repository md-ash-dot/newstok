# Generated by Django 4.2.10 on 2024-02-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
