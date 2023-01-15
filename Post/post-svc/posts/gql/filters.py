from posts.models import (
    Lost,
    Found
)

import django_filters

from django_filters import OrderingFilter


class LostPostsFilter(django_filters.FilterSet):
    class Meta:
        model=Lost
        fields={
            'item__label':['icontains',],
            'color__label':['icontains',],
            'place__label':['icontains',],
        }
        
    order_by = OrderingFilter(
        fields=(
            'created_on',
        )
    )

class FoundPostsFilter(django_filters.FilterSet):
    class Meta:
        model=Found
        fields={
            'item__label':['icontains',],
            'color__label':['icontains',],
            'place__label':['icontains',],
        }
        
    order_by = OrderingFilter(
        fields=(
            'created_on',
        )
    )