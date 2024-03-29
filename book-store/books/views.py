import json

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Book

from orders.models import Order, OrderDetail

from .filters import BookFilter
 
from .forms import OrderForm

from django.contrib.auth.decorators import login_required



def index(request):
    # books = Book.objects.all()
    # return render(request, 'books/index.html', {'books':books})
    print(request.COOKIES.get('shopcar', '{}'))
    _filter = BookFilter(request.GET or None, queryset=Book.objects.all())
    return render(request, 'books/index.html', {'filter': _filter})

def show(request, pk):
    book = get_object_or_404(Book, pk=pk)
    f = OrderForm()
    return render(request, 'books/show.html', {'book':book, 'form':f})

#@login_required
def order(request, pk):
    '''
    u = request.user
    o = Order.objects.filter(buyer=u, paid=False).last()
    f = OrderForm(request.POST)
    if not f.is_valid():
        return redirect('books:show', pk)

    c = f.cleaned_data['number']
    if o is None:
        o = Order.objects.create(buyer=u)

    OrderDetail.objects.update_or_create(order=o, book_id=pk, defaults={'count':c})
    # d = OrderDetail.objects.create(order=o, book_id=pk, count=c)
    messages.success(request, "下單成功")
    return redirect('books:index')
    '''

    f = OrderForm(request.POST)
    if not f.is_valid():
        return redirect('books:show', pk)

    c = f.cleaned_data['number']
    response = redirect('books:index')

    if request.user.is_authenticated:
        u = request.user
        o = Order.objects.filter(buyer=u, paid=False).last()

        if o is None:
            o = Order.objects.create(buyer=u)

        # OrderDetail.objects.update_or_create(order=o, book=pk, defaults={'count':c})
        item, created = OrderDetail.objects.get_or_create(order=o, book_id=pk, defaults={'count':c})
        if not created:
            item.count += c
            item.save()
    else:
        shopcar = json.loads(request.COOKIES.get('shopcar', '{}'))
        if str(pk) in shopcar:
            shopcar[str(pk)] += c
        else:
            shopcar[str(pk)] = c
        response.set_cookie('shopcar', json.dumps(shopcar))

    messages.success(request, "下單成功")
    return response
    