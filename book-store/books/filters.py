from django_filters import FilterSet, CharFilter, NumberFilter

from .models import Book


class BookFilter(FilterSet):
    title = CharFilter(label='標題', lookup_expr='icontains')
    description = CharFilter(label='簡介', lookup_expr='icontains')
    price_from = NumberFilter(label='價錢下限',
                              field_name='price',
                              lookup_expr='gte')
    price_to = NumberFilter(label='價錢上限',
                            field_name='price',
                            lookup_expr='lte')

    class Meta:
        model = Book
        fields = (
            'title',
            'description',
            'publisher',
            'authors',
            'category',
            'tags',
        )
