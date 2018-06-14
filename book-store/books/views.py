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
    _filter = BookFilter(request.GET or None, queryset=Book.objects.all())
    return render(request, 'books/index.html', {'filter': _filter})

def show(request, pk):
    book = get_object_or_404(Book, pk=pk)
    f = OrderForm()
    return render(request, 'books/show.html', {'book':book, 'form':f})

@login_required
def order(request, pk):
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
    