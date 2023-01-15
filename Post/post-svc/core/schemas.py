import graphene

from posts.schema import (
    Query as PostsQuery,
    Mutation as PostsMutation
)

from tags.schema import (
    Query as TagsQuery,
    Mutation as TagsMutation
)

class Query(
    PostsQuery,
    TagsQuery,
    graphene.ObjectType
):
    pass

class Mutation(
    PostsMutation,
    TagsMutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)