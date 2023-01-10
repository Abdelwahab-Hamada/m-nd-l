from flask import (
    Flask,
    request,
    make_response
)

from auth_svc import (
    registeration,
    authentication,
    uid_claiming,
    access_token_claiming,
    access_token_verification
)

from decouple import config

from datetime import (
    datetime,
    timedelta
)

app=Flask(__name__)

@app.route("/register",methods=["POST"])
def register():
    json_response,error=registeration.register(request)

    if not json_response and not error:
        return "Don't cry goback to your mother :)"

    return json_response if not error else error


@app.route("/login",methods=["POST"])
def auth():
    json_response,error=authentication.get_tokens(request)
    tokens=json_response['DATA']

    if not json_response and not error:
        return "Don't cry goback to your mother (;"

    if error:
        return error

    response=make_response({
        config('AT_KEY'):tokens[config('AT_KEY')],
        "MESSAGE":json_response['MESSAGE']
    })
    response.set_cookie(
        key = config('UIDT_KEY'), 
        value = tokens[config('UIDT_KEY')],
        expires = datetime.now() + timedelta(days=90),
        secure = False,
        httponly = True,
        samesite = 'None'
    )

    return response

@app.route("/uid",methods=["GET"])
def claim_uid():
    try:
        uidt=request.cookies[config('UIDT_KEY')]
    except:
        return {'ERROR':'You have to login first.'}

    json_response,error=uid_claiming.get_uid(uidt)
    
    return json_response if not error else error

@app.route("/at",methods=["GET"])
def claim_access_token():
    try:
        uidt=request.cookies[config('UIDT_KEY')]
    except:
        return {'ERROR':'You have to login first.'}

    json_response,error=access_token_claiming.get_access_token(uidt)

    return json_response if not error else error

@app.route("/vat",methods=["GET"])
def verify_access_token():
    try:
        uidt=request.cookies[config('UIDT_KEY')]
        at=request.headers[config('AT_KEY')]
    except:
        return {'ERROR':'You have to login first.'}

    json_response,error=access_token_verification.verify_access_token(uidt,at)

    return json_response if not error else error

    