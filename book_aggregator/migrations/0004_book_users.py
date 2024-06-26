# Generated by Django 5.0.3 on 2024-03-20 10:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_aggregator', '0003_alter_subcategory_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='favourite_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
