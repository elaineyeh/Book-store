from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from books.models import Book


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='使用者')
    buy_time = models.DateTimeField('建立時間', auto_now_add=True)
    paid_time = models.DateTimeField('購買時間', auto_now_add=True)
    paid = models.BooleanField('付款', default=False)
    ship = models.BooleanField('出貨', default=False)

    def __str__(self):
        return str(self.buy_time)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        verbose_name = '訂單'
        verbose_name_plural = '訂單'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='訂單編號', related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='書名編號')
    count = models.PositiveIntegerField('數量', validators=(MinValueValidator(1),))

    def __str__(self):
        return str(self.count) # please return string type for this function. 

    def get_cost(self):
        return self.count * self.book.price

    class Meta:
        unique_together = (
            ('order', 'book'),
        )
        verbose_name = '訂單明細'
        verbose_name_plural = '訂單明細'
