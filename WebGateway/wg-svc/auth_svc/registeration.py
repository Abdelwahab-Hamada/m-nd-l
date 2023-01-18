import requests
from decouple import config

def register(req):
    error=is_success=None

    try:
        data=req.json
        if data['name'] and data['password'] and data['password_confirmation'] and (data['email'] or data['mobile_number']):
            payload=data
            
            response=requests.post(
                config('AUTH_SVC_URL')+'register/',
                json=payload
            )
            json_response=response.json()

            

            if response.status_code == 200:
                is_success=json_response                  #response,error
            else:
                error={'MESSAGE':json_response},response.status_code
    except:
        pass
    return is_success,error

    

    