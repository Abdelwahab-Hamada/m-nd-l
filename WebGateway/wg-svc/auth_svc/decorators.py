from flask import request
from functools import wraps

from auth_svc import (
    access_token_verification,
    uid_claiming
)

from decouple import config

def login_required(view): 
    @wraps(view)
    def inner(*args,**kwargs):
        try:
            uidt=request.cookies[config('UIDT_KEY')]
            at=request.headers[config('AT_KEY')]
        except:
            return {'MESSAGE':'You have to login first.'},401

        valid,error=access_token_verification.verify_access_token(uidt,at)

        if valid:
            return view(*args,**kwargs)
        return error
    return inner

def uid_required(view): 
    @wraps(view)
    def inner(*args,**kwargs):
        try:
            uidt=request.cookies[config('UIDT_KEY')]
        except:
            return {'MESSAGE':'You have to login first.'},401

        uid,error=uid_claiming.get_uid(uidt)

        if uid:
            return view(uid=uid,*args,**kwargs)
        return error
    return inner