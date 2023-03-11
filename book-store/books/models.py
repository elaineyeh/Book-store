import os
import time

from django.db import models


def book_directory_path(instance, filename):
    # return 'books/{}/{}'.format(instance.id, filename)
    return os.path.join('books', str(time.time()), filename)


class Category(models.Model):
    name = models.CharField('類別', max_length=32, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '類別'
        verbose_name_plural = '類別'


class Publisher(models.Model):
    name = models.CharField('名稱', max_length=32)
    address = models.CharField('地址', max_length=128)
    phone = models.CharField('電話', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = '出版商'



class Tag(models.Model):
    name = models.CharField('標籤', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '標籤'
        verbose_name_plural = '標籤'



class Author(models.Model):
    name = models.CharField('名稱', max_length=32)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'



class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='類別')
    title = models.CharField('書名', max_length=64)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, verbose_name='出版商')
    price = models.PositiveIntegerField('價錢')
    description = models.TextField('簡介', max_length=500)
    image = models.ImageField('圖片', upload_to=book_directory_path)
    tags = models.ManyToManyField(Tag, verbose_name='標籤')
    authors = models.ManyToManyField(Author, verbose_name='作者')
    count = models.PositiveIntegerField('庫存', default=0)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '書籍'
        verbose_name_plural = '書籍'
