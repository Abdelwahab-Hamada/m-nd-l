import requests
from decouple import config

def get_tokens(req):
    error=tokens=None

    try:
        data=req.json
        if data['identifier'] and data['password']:
            payload=data
            
            response=requests.post(
                config('AUTH_SVC_URL')+'auth/',
                json=payload
            )
            json_response=response.json()

            if response.status_code == 200:
                tokens=json_response                #response,error
            else:
                error=json_response,response.status_code
    except:
        pass
    return tokens,error

    

    