from django.db import models

import uuid

from tags.models import (
    Item,
    Color,
    Place
)

class Post(models.Model):
    class Meta:
        abstract=True
        ordering = ['created_on']

    id=models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID'
    )

    uid=models.UUIDField(
        verbose_name='User ID'
    )

    description=models.TextField(
        verbose_name='Description'
    )

    image_id=models.UUIDField(
        blank=True,
        null=True,
        verbose_name='Image ID'
    )

    created_on=models.DateTimeField(
        auto_now_add=True
    )

    item=models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Item'
    )

    color=models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        verbose_name='Color'
    )
    
    place=models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Place'
    )

    def __str__(self):
        return f'{self.color.label} {self.item.label}'


class Lost(Post):
    class Meta:
        verbose_name_plural = "Lost Posts"

class Found(Post):
    class Meta:
        verbose_name_plural = "Found Posts"

    
