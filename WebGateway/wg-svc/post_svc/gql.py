import requests
from decouple import config

def query(query):
    return requests.post(
        url=config('POST_SVC_URL'), 
        json={
            "query": query
        }
    ).json()

def mutate(query,vars):
    return requests.post(
        url=config('POST_SVC_URL'), 
        json={
            "query": query,
            'variables':vars
        }
    ).json()