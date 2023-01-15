from graphene import (
    relay,
)

import graphene,graphene_django


from django.utils import timezone
import humanize

from posts.models import (
    Lost,
    Found
)

from .filters import (
    LostPostsFilter,
    FoundPostsFilter
)

class LostPostType(graphene_django.DjangoObjectType):
    class Meta:
        model=Lost
        filterset_class=LostPostsFilter
        interfaces = (relay.Node, )

    readable_time=graphene.String()

    def resolve_readable_time(instance,info):
        now= timezone.now()
        created_on=instance.created_on
        readable_time=humanize.naturaltime(now - created_on)
        return readable_time

class FoundPostType(LostPostType):
    class Meta:
        model=Found
        filterset_class=FoundPostsFilter
        interfaces = (relay.Node, )