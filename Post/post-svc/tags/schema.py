import graphene

from graphene import (
    relay,
)

from graphene_django.filter import DjangoFilterConnectionField

from .gql.types import (
    ItemType,
    ColorType,
    PlaceType
)

from .gql.mutations import (
    CreateItem,
    CreateColor,
    CreatePlace
)

class Query(graphene.ObjectType):
    item=relay.Node.Field(ItemType)
    items=DjangoFilterConnectionField(ItemType)
    colors=DjangoFilterConnectionField(ColorType)
    places=DjangoFilterConnectionField(PlaceType)

class Mutation(graphene.ObjectType):
    item=CreateItem.Field()
    color=CreateColor.Field()
    place=CreatePlace.Field()