from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField()
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_aggregator:category', args=[self.slug])


class SubCategory(models.Model):
    name = models.CharField()
    slug = models.SlugField(max_length=1000)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_aggregator:category', args=[self.slug])


class Book(models.Model):
    name = models.CharField()
    author = models.CharField(null=True)
    categories = ArrayField(models.CharField(), default=list)
    image_url = models.CharField(null=True)
    genres = ArrayField(models.CharField(), default=list)
    description = models.TextField()
    avg_rating = models.FloatField()
    min_price = models.FloatField()
    max_price = models.FloatField()
    have_electronic_version = models.BooleanField()
    have_physical_version = models.BooleanField()
    sources = models.JSONField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    slug = models.SlugField(max_length=100, unique=True)
    users = models.ManyToManyField(User, related_name='favourite_books')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_aggregator:detail', args=[self.slug])
