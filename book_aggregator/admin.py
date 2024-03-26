from django.contrib import admin
from book_aggregator.models import Book, Category, SubCategory

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(SubCategory)
