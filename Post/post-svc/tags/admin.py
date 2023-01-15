from django.contrib import admin
from .models import (
    Item,
    Color,
    Place
)

admin.site.register(Item) 
admin.site.register(Color)
admin.site.register(Place)