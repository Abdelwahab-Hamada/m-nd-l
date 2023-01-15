from flask import (
    Blueprint,
    request,
    make_response
)

from decouple import config

from datetime import (
    datetime,
    timedelta
)

from . import (
    registeration,
    authentication,
    access_token_claiming,
)

bp=Blueprint('auth_svc', __name__)

@bp.route("/register",methods=["POST"])
def register():
    json_response,error=registeration.register(request)

    if not json_response and not error:
        return "Don't cry goback to your mother :)"

    return json_response if not error else {'MESSAGE':error}

@bp.route("/login",methods=["POST"])
def auth():
    json_response,error=authentication.get_tokens(request)

    if not json_response and not error:
        return "Don't cry goback to your mother (;"

    if error:
        return error

    tokens=json_response['DATA']
    json_response=make_response({
        'DATA':{config('AT_KEY'):tokens[config('AT_KEY')]},
        "MESSAGE":json_response['MESSAGE']
    })
    json_response.set_cookie(
        key = config('UIDT_KEY'), 
        value = tokens[config('UIDT_KEY')],
        expires = datetime.now() + timedelta(days=90),
        secure = False,
        httponly = True,
        samesite = 'None'
    )

    return json_response

@bp.route("/at",methods=["GET"])
def claim_access_token():
    try:
        uidt=request.cookies[config('UIDT_KEY')]
    except:
        return {'MESSAGE':'You have to login first.'},401

    json_response,error=access_token_claiming.get_access_token(uidt)

    return json_response if not error else error