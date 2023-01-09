from django.contrib.auth.models import (
    BaseUserManager,
)

import re
import unidecode

class UserManager(BaseUserManager):
    def __generate_username(self,name):
        name_translated_to_english=unidecode.unidecode(name)
        sanitized_username=re.sub('[^a-zA-Z0-9-_]','',name_translated_to_english)

        return sanitized_username

    def __get_generated_unique_username(self,name):
        counter=1
        unique_username=username=self.__generate_username(name)

        while self.model.objects.filter(username=unique_username):
            unique_username=username+str(counter)
            counter+=1

        return unique_username

    def create_user(self,password=None, **kwargs):
        if not kwargs['username'] and kwargs['name']:
            kwargs['username']=self.__get_generated_unique_username(kwargs['name'])
        elif not kwargs['username']:
            raise ValueError('Users must provide a kwargs username or name')
            
        user=self.model(
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_staff(self,**kwargs):
        user=self.create_user(
            **kwargs
        )

        user.is_staff=True
        user.save(using=self._db)
        return user

    def create_superuser(self,**kwargs):
        user=self.create_staff(
            name='super:'+kwargs['username'],
            **kwargs
        )

        user.is_superuser=True
        user.save(using=self._db)
        return user