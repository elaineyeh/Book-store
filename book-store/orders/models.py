from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from books.models import Book


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.PROTECT)
    buy_time = models.DateTimeField(auto_now_add=True)
    paid_time = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    ship = models.BooleanField(default=False)

    def __str__(self):
        return str(self.buy_time)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(validators=(MinValueValidator(1),))

    def __str__(self):
        return str(self.count) # please return string type for this function. 

    class Meta:
        unique_together = (
            ('order', 'book'),
        )