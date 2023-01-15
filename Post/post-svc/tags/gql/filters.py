from tags.models import (
    Item,
    Color,
    Place
)

import django_filters

from django_filters import OrderingFilter


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model=Item
        fields={
            'label':['contains'],
        }
        
    order_by = OrderingFilter(
        
        fields=(
            'label',
        )
    )

class ColorFilter(django_filters.FilterSet):
    class Meta:
        model=Color
        fields={
            'label':['contains',],
        }
        
    order_by = OrderingFilter(
        
        fields=(
            'label',
        )
    )

class PlaceFilter(django_filters.FilterSet):
    class Meta:
        model=Place
        fields={
            'label':['contains',],
        }
        
    order_by = OrderingFilter(
        
        fields=(
            'label',
        )
    )