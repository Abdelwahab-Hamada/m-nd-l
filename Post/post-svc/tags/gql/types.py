from graphene import (
    relay,
)

import graphene,graphene_django

from tags.models import (
    Item,
    Color,
    Place
)

from django.db.models import Count,Max

from .filters import (
    ItemFilter,
    ColorFilter,
    PlaceFilter
)

class ItemType(graphene_django.DjangoObjectType):
    class Meta:
        model=Item
        filterset_class=ItemFilter
        interfaces = (relay.Node, )

class ColorType(graphene_django.DjangoObjectType):
    class Meta:
        model=Color
        filterset_class=ColorFilter
        interfaces = (relay.Node, )

class PlaceType(graphene_django.DjangoObjectType):
    class Meta:
        model=Place
        filterset_class=PlaceFilter
        interfaces = (relay.Node, )
        

    