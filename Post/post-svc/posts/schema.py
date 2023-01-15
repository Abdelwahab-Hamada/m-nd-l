import graphene

from graphene_django.filter import DjangoFilterConnectionField

from .gql.types import (
    LostPostType,
    FoundPostType
)

from .gql.mutations import (
    PostLost,
    PostFound
)

class Query(graphene.ObjectType):
    lostPosts=DjangoFilterConnectionField(LostPostType)
    foundPosts=DjangoFilterConnectionField(FoundPostType)

class Mutation(graphene.ObjectType):
    lost=PostLost.Field()
    found=PostFound.Field()

