import graphene

from graphene import (
    relay,
)

from posts.models import (
    Lost,
    Found
)

from graphql_relay import from_global_id

class PostLost(relay.ClientIDMutation):
    class Input: 
        uid=graphene.String(required=True)
        description=graphene.String(required=True)
        image_id=graphene.String(required=False)
        item_id=graphene.String(required=True)
        color_id=graphene.String(required=True)
        place_id=graphene.String(required=True)

    posted=graphene.Boolean()

    def mutate_and_get_payload(
        root,
        info,
        item_id,
        color_id,
        place_id, 
        **input): 
        
        input['item_id']=from_global_id(item_id)[1]
        input['color_id']=from_global_id(color_id)[1]
        input['place_id']=from_global_id(place_id)[1] 
        post=Lost.objects.create(
            **input
        )

        return PostLost(posted=True)

class PostFound(relay.ClientIDMutation):
    class Input: 
        uid=graphene.String(required=True)
        description=graphene.String(required=True)
        image_id=graphene.String(required=False)
        item_id=graphene.String(required=True)
        color_id=graphene.String(required=True)
        place_id=graphene.String(required=True)

    posted=graphene.Boolean()

    def mutate_and_get_payload(
        root,
        info,
        item_id,
        color_id,
        place_id, 
        **input): 
        
        input['item_id']=from_global_id(item_id)[1]
        input['color_id']=from_global_id(color_id)[1]
        input['place_id']=from_global_id(place_id)[1]
        post=Found.objects.create(
            **input
        )

        return PostFound(posted=True)