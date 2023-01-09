from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)

import uuid

from .managers import UserManager

from .tokens import (
    AccessToken,
    UserIDToken
)

class User(AbstractUser):
    id=models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID'
    )

    username=models.CharField(
        blank=True,
        max_length=15,
        unique=True,
        verbose_name='username'
    )

    email=models.EmailField(
        blank=True,
        max_length=254,
        null=True,
        unique=True,
        verbose_name='email address',
    )

    mobile_number=models.CharField(
        blank=True,
        max_length=11, 
        null=True,
        unique=True,
        verbose_name='mobile number',
    )

    first_name=None
    last_name=None

    name= models.CharField(
        max_length=50,
        verbose_name='full name'
    )
    
    secret_key=models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name='secret key',
    )

    objects=UserManager()

    REQUIRED_FIELDS =[]

    def __str__(self):
        return self.username

    def update_SK(self):
        self.secret_key=uuid.uuid4()
        self.save()

    @property
    def private_key(self):
        return self.secret_key.hex

    @property
    def access_token(self):
        return AccessToken(
            secret=self.private_key,
        ).get_token()

    @property
    def user_id_token(self):
        return UserIDToken(
            uid=self.id.hex
        ).get_token()

    
        


        

    



    



