from django.test import TestCase

from .models import (
    Lost,
    Found
)

from tags.models import (
    Item,
    Color,
    Place
)

import uuid

class LostPost(TestCase):
    def setUp(self):
        item=Item.objects.create(label="wallet")
        color=Color.objects.create(label="brown")
        place=Place.objects.create(label="Cairo")
        Lost.objects.create(
            uid=uuid.uuid4(),
            description='i lost my wallet in downtown it`s contains my Id ,1k egp and credit card , i`m not from cairo,please i want 50 pound to go home :(',
            image_id=None,
            item=item,
            color=color,
            place=place
        )
        

    def test_user_can_post_lost(self):
        lostPost=Lost.objects.get(place__label="Cairo")
        
        self.assertEqual(lostPost.item.label,'wallet')

class FoundPost(TestCase):
    def setUp(self):
        item=Item.objects.create(label="wallet")
        color=Color.objects.create(label="brown")
        place=Place.objects.create(label="Cairo")
        Lost.objects.create(
            uid=uuid.uuid4(),
            description='i lost my wallet in downtown it`s contains my Id ,1k egp and credit card , i`m not from cairo,please i want 50 pound to go home :(',
            image_id=None,
            item=item,
            color=color,
            place=place
        )
        

    def test_user_can_post_found(self):
        lostPost=Lost.objects.get(place__label="Cairo")
        
        self.assertEqual(lostPost.item.label,'wallet')

