from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'buy_time', 'get_pdf')

    def get_pdf(self, obj):
        url = reverse("orders:order_pdf", args=[obj.id])
        return mark_safe('''<a href='%s' onclick="window.open(this.href, '', 'width=1000,height=500'); return false;">PDF</a>''' % (url))

    get_pdf.short_description = 'PDF'


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)