import requests
from decouple import config

def verify_access_token(uidt,at):
    error=is_valid=None

    payload={
        'UIDT':uidt,
        'AT':at
    }

    response=requests.post(
        config('AUTH_SVC_URL')+'vat/',
        json=payload
    )
    json_response=response.json()

    if response.status_code == 200:
        is_valid=json_response 
    else:
        error=json_response
    return is_valid,error
