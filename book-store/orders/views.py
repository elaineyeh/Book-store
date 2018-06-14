import json

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages as m
from django.utils import timezone

from .forms import DeleteConfirmForm

from books.models import Book
from books.filters import BookFilter

from .models import Order, OrderDetail
from .forms import PaidConfirmForm


@login_required
def index(request):
    orders = Order.objects.filter(buyer=request.user, paid=True)
    return render(request, 'orders/index.html', {'orders': orders})


@login_required
def show(request, pk):
    order = get_object_or_404(Order, pk=pk, buyer=request.user, paid=True)
    details = OrderDetail.objects.select_related('book').filter(order=order)
    total = sum([i.book.price * i.count for i in details])
    return render(request, 'orders/show.html', {
        'order': order,
        'details': details,
        'total': total,
    })


@login_required
def paid(request):
    order = Order.objects.filter(buyer=request.user, paid=False).last()
    details = OrderDetail.objects.select_related('book').filter(order=order)
    form = PaidConfirmForm(request.POST or None)
    if not details:
        _filter = BookFilter(request.GET or None, queryset=Book.objects.all())
        m.error(request, '尚未購入商品')
        return render(request, 'books/index.html', {'filter': _filter})
    else:
        if form.is_valid() and form.cleaned_data['check']:

            for detail in details:
                book = get_object_or_404(Book, id=detail.book_id)
                book.count = book.count - detail.count
                book.save()

            order.paid = True
            order.ship = True
            order.paid_time = timezone.now()
            order.save()

            m.success(request, '結帳成功')
            return redirect('orders:show', order.id)

    total = sum([i.book.price * i.count for i in details])

    return render(request, 'orders/paid.html', {
        'details': details,
        'form': form,
        'total': total,
    })


def shopcar_index(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(buyer=request.user, paid=False).last()
        details = OrderDetail.objects.select_related('book').filter(order=order)
    else:
        details = []
        shopcar_dict = json.loads(request.COOKIES.get('shopcar', '{}'))
        books = Book.objects.filter(id__in=shopcar_dict.keys())
        for book, count in zip(books, shopcar_dict.values()):
            details.append({'book': book, 'count': count})

    return render(request, 'orders/shopcar_index.html', {'shopcars': details})


def shopcar_delete(request, pk):
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        response = redirect('orders:shopcars')
        if request.user.is_authenticated:
            order = Order.objects.filter(buyer=request.user, paid=False).last()
            OrderDetail.objects.filter(order=order, book_id=pk).delete()
        else:
            shopcar = json.loads(request.COOKIES.get('shopcar', '{}'))
            del shopcar[str(pk)]
            response.set_cookie('shopcar', json.dumps(shopcar))

        m.success(request, '移除成功')
        return response

    return render(request, 'orders/delete_confirm.html', {
        'form': form,
        'title': '移除購物車'
    })
