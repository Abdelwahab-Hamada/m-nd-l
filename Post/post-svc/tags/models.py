from django.db import models

import uuid

class Tag(models.Model):
    class Meta:
        abstract=True

    id=models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID'
    )
    
    label=models.CharField(
        max_length=52,
        unique=True,
        verbose_name='Label'
    )

    def __str__(self):
        return f'{self.label}'

class Item(Tag):
    pass

class Color(Tag):
    pass

class Place(Tag):
    pass
