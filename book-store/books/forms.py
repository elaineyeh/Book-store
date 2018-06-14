from django.forms import Form, IntegerField


class OrderForm(Form):
    number = IntegerField(label='購買數量')
