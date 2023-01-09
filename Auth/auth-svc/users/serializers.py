from rest_framework import (
    serializers,
    validators
) 

from .models import User

class UserSerializer(serializers.ModelSerializer):
    mobile_number=serializers.RegexField(
        '[0-9]',
        max_length=11, 
        min_length=11, 
        allow_blank=True,
        validators=[
            validators.UniqueValidator(
                queryset=User.objects.all(),
                message='This mobile number has already been taken.'
            ),
        ],
        error_messages={
            'max_length':'Ensure mobile number has no more than 11 digits.',
            'min_length':'Ensure mobile number has no less than 11 digits.'
        },
        write_only=True

    )
    
    name=serializers.RegexField(
        '',
        max_length=50, 
        min_length=1, 
        validators=[
        ],
        error_messages={
            'max_length':'This name is too long. It must contain at most 50 characters.',
            'min_length':'This name is too short. It must contain at least 1 character',
            'blank':'You have to provide your name.',
            'required':'You have to provide your name.',

        },
        write_only=True

    )
    
    password=serializers.CharField(
        max_length=128, 
        min_length=8, 
        validators=[
            
        ],
        error_messages={
            'max_length':'This password is too long. It must contain at most 128 characters.',
            'min_length':'This password is too short. It must contain at least 8 characters.',
            'blank':'You have to enter a password.',
            'required':'You have to enter a password.',

        },
        write_only=True

    )

    password_confirmation=serializers.CharField(
        max_length=128, 
        min_length=8, 
        validators=[
            
        ],
        error_messages={
            'max_length':'This password is too long. It must contain at most 128 characters.',
            'min_length':'This password is too short. It must contain at least 8 characters.',
            'blank':'You have to congirm the password.',
            'required':'You have to congirm the password.',

        },
        write_only=True

    )

    class Meta:
        model=User
        fields=('name','password','password_confirmation','email','mobile_number','username')
        extra_kwargs={
            'email':{'write_only': True},

        }

    def validate_mobile_number(self,value):
        if not value:
            return None
        return value

    def validate_email(self,value):
        if not value:
            return None
        return value

    def validate(self,attrs):
        password1=attrs['password']
        password2=attrs['password_confirmation']
        email_address=attrs['email']
        phone_number=attrs['mobile_number']
        
        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError('The password confirmation does not match.')
        del attrs['password_confirmation']

        if not email_address and not phone_number:
            raise serializers.ValidationError('Please enter your Email or Mobile Number.')

        return attrs

        
    def create(self,kwargs):
        user=User.objects.create_user(
            **kwargs
        )
            
        return user


         

