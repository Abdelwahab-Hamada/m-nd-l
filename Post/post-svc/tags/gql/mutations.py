import graphene

from tags.models import (
    Item,
    Color,
    Place
)

from .types import (
    ItemType,
    ColorType,
    PlaceType
)

class CreateItem(graphene.Mutation):
    class Arguments:
        label=graphene.String()

    node=graphene.Field(ItemType)
    
    def mutate(_,info,**kwargs):
        item,_=Item.objects.get_or_create(
            **kwargs
        )

        return CreateItem(node=item)

class CreateColor(CreateItem):
    node=graphene.Field(ColorType)
    
    def mutate(_,info,**kwargs):
        color,_=Color.objects.get_or_create(
            **kwargs
        )

        return CreateItem(node=color)

class CreatePlace(CreateItem):
    node=graphene.Field(PlaceType)

    def mutate(_,info,**kwargs):
        place,_=Place.objects.get_or_create(
            **kwargs
        )

        return CreateItem(node=place)


