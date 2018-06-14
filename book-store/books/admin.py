from django.contrib import admin

from .models import Category, Publisher, Tag, Book, Author


admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(Author)