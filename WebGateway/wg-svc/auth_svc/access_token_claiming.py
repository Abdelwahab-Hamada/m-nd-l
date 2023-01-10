import requests
from decouple import config

def get_access_token(uidt):
    error=access_token=None

    payload={
        'UIDT':uidt,
    }

    response=requests.post(
        config('AUTH_SVC_URL')+'at/',
        json=payload
    )
    json_response=response.json()

    if response.status_code == 200:
        access_token=json_response 
    else:
        error=json_response
    return access_token,error
