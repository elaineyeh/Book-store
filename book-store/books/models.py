import os
import time

from django.db import models


def book_directory_path(instance, filename):
    # return 'books/{}/{}'.format(instance.id, filename)
    return os.path.join('books', str(time.time()), filename)


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=64)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to=book_directory_path)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.title)