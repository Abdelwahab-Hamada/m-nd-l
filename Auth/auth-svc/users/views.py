from rest_framework import (
    generics,
    views
)
from .serializers import (
    UserSerializer,
    
)
from rest_framework.response import Response
from django.contrib.auth import authenticate

from django.conf import settings

from .models import User

from datetime import (
    datetime,
)

from django.db.models import Q

from .tokens import (
    UserIDToken,
    AccessToken
)

from django.middleware import csrf

class Registration(generics.CreateAPIView):
    serializer_class=UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        csrf.get_token(request) 

        return Response({
                'DATA': response.data,
                'MESSAGE': 'Successfully regestered, you can login now.',
        })

class Authentication(views.APIView):
    def post(self, request, format=None):
        data = request.data
        response = Response()     

        identifier = data.get('identifier')

        if not identifier:
            return  Response({
                "ERORR" : "Missing field:identifier.",
                'MESSAGE': 'You have to provide mobile number,username or email.',
            },status=400)

        try:
            user = User.objects.get(
                Q(mobile_number=identifier) |
                Q(username=identifier) | 
                Q(email=identifier)
            )
            username=user.username

        except User.DoesNotExist:
            return  Response({
                "ERORR" : "Missing credintials:username or  mobile number or email.",
                'MESSAGE': "Sorry we could't find your account.",
            },status=404)

        password = data.get('password', None)   

        logged_user = authenticate(username=username, password=password) 

        if logged_user and logged_user.is_active:
            csrf.get_token(request)   

            response.data={
                "DATA":{
                    settings.AUTH_JWT['UIDT_KEY']:logged_user.user_id_token,
                    settings.AUTH_JWT['AT_KEY']:logged_user.access_token,
                },
                "MESSAGE":"Credintials approved, redirect to "
            }
            return response
        return Response({
            "ERROR" : "Not authorized",
            "MESSAGE":"Invalid username or password!!"
        },status=401)

#Server-side views doesn't need a message on successful response

class UserIDClaiming(views.APIView): 
    def get_user_id(uid_token):

        uid_claims=UserIDToken().get_claims(
            token=uid_token,
        )

        return uid_claims['uid']

    def post(self,request,format=None):
        data = request.data

        try:
            uid_token=data.get(settings.AUTH_JWT['UIDT_KEY']) 

            return Response({
                "DATA":{
                    'uid':UserIDClaiming.get_user_id(uid_token),
                },
            })
        except:
            return Response({
                'ERROR':'User session has timed out.',
                "MESSAGE":"Login again, redirect to login page."
            },status=403)


class AccessTokenClaiming(views.APIView):
    def post(self,request,format=None):
        data = request.data

        try:
            uid_token=data.get(settings.AUTH_JWT['UIDT_KEY'])
            user=User.objects.get(id=UserIDClaiming.get_user_id(uid_token))

            return Response({
                "DATA":{
                    settings.AUTH_JWT['AT_KEY']:user.access_token,
                },
            })     
        except:
            return Response({
                'ERROR':'User session has timed out.',
                "MESSAGE":"Login again, redirect to login page."
            },status=403)

class AccessTokenVerification(views.APIView):
    def post(self,request,format=None):
        data = request.data
        
        try:
            uid_token=data.get(settings.AUTH_JWT['UIDT_KEY'])
            user=User.objects.get(id=UserIDClaiming.get_user_id(uid_token))
            user_private_key=user.private_key
            access_token = data.get(settings.AUTH_JWT['AT_KEY'])

            at_is_valid=is_valid=AccessToken(secret=user_private_key).get_claims(
                token=access_token, 
            )

            return Response({
                "DATA":{
                    'access_verified':at_is_valid,
                },
            })
        except:
            return Response({
                'ERROR':'User session has timed out.',
                "MESSAGE":"Login again, redirect to login page."
            },status=403)

          


