from jwt import (
    encode,
    decode,
    ExpiredSignatureError
)    

from datetime import (
    datetime,
)

from django.conf import settings

class AbstractToken:
    def __init__(self,secret=None,**kwargs):
        self._secret=secret or settings.AUTH_JWT['DEFAULT_SECRET']
        self._kwargs=kwargs

    @property
    def life_time(self):
        return settings.AUTH_JWT['LONG_LIFETIME']

    @property
    def __exp(self):
        return (
            datetime.now() 
            + 
            self.life_time
        )

    @property
    def __payload(self):
        return {
            'exp':self.__exp,
            **self._kwargs
        }

    def __validate(self,exp,**kwargs):
        if datetime.now() > datetime.utcfromtimestamp(exp):
                raise Exception("Expired token")
        return kwargs or True

    def get_token(self):
        return encode(
            self.__payload,
            self._secret
        )

    def get_claims(self,token):
        try:
            decoded_token=decode(
                token, 
                self._secret, 
                algorithms=["HS256"]
            )
            return self.__validate(**decoded_token)            
        except Exception as e:
            raise e

        
class AccessToken(AbstractToken):
    @property
    def life_time(self):
        return settings.AUTH_JWT['SHORT_LIFETIME']

class UserIDToken(AbstractToken):
    pass
        

    

    

        