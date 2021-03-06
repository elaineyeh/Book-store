# Generated by Django 2.0.5 on 2018-06-20 07:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180603_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '訂單明細', 'verbose_name_plural': '訂單明細'},
        ),
        migrations.AlterModelOptions(
            name='orderdetail',
            options={'verbose_name': '訂單', 'verbose_name_plural': '訂單'},
        ),
        migrations.AlterField(
            model_name='order',
            name='buy_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='建立時間'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='使用者'),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='付款'),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='購買時間'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ship',
            field=models.BooleanField(default=False, verbose_name='出貨'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='書名編號'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='count',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='數量'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='訂單編號'),
        ),
    ]
