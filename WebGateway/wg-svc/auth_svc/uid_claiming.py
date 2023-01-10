import requests
from decouple import config

def get_uid(uidt):
    error=uid=None

    payload={
        'UIDT':uidt,
    }

    response=requests.post(
        config('AUTH_SVC_URL')+'uid/',
        json=payload
    )
    json_response=response.json()

    if response.status_code == 200:
        uid=json_response 
    else:
        error=json_response
    return uid,error
