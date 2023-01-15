from flask import (
    Blueprint,
    request,
    make_response
)

from auth_svc.decorators import (
    login_required,
    uid_required
)

from . import (
    gql,
    queries,
    mutations
)

bp=Blueprint('post_svc', __name__,url_prefix='/')

@bp.route("lost",methods=["GET"])
def lost_posts():
    try:
        string=request.json['contains']
    except:
        return {'MESSAGE':'You have to send contains in a json request.'},400

    query=queries.LostPosts()
    query.set_contains(string)
    response=gql.query(query.query)
    return response

@bp.route("found",methods=["GET"])
def found_posts():
    try:
        string=request.json['contains']
    except:
        return {'MESSAGE':'You have to send contains in a json request.'},400
    query=queries.FoundPosts()
    query.set_contains(string)
    response=gql.query(query.query)
    return response
    
@bp.route("items",methods=["GET"])
def items():
    try:
        string=request.json['contains']
    except:
        return {'MESSAGE':'You have to send contains in a json request.'},400

    query=queries.Items()
    query.set_contains(string)
    response=gql.query(query.query)
    return response

@bp.route("item",methods=["GET"])
def item():
    try:
        id=request.json['id']
    except:
        return {'MESSAGE':'You have to send id in a json request.'},400

    query=queries.Item()
    query.set_contains(id)
    response=gql.query(query.query)
    return response

#mutations
@bp.route("lost",methods=["POST"])
@login_required
@uid_required
def post_lost(uid):
    try:
        vars={
            "uid":uid,
            "description":request.json['description'],
            "imageId":None,
            "itemId":request.json['itemId'],
            "colorId":request.json['colorId'],
            "placeId":request.json['placeId'],
        }
    except:
        return {'MESSAGE':'''You have to send description,itemId,colorId,placeId in a json request.'''},400

    mutation=mutations.Lost().mutation
    response=gql.mutate(mutation,vars)
    return response

@bp.route("found",methods=["POST"])
@login_required
@uid_required
def post_found(uid):
    try:
        vars={
            "uid":uid,
            "description":request.json['description'],
            "imageId":None,
            "itemId":request.json['itemId'],
            "colorId":request.json['colorId'],
            "placeId":request.json['placeId'],
        }
    except:
        return {'MESSAGE':'''You have to send description,itemId,colorId,placeId in a json request.'''},400

    mutation=mutations.Found().mutation
    response=gql.mutate(mutation,vars)
    return response
    

@bp.route("item",methods=["POST"])
@login_required
def add_item():
    try:
        vars={
            'label':request.json['label'],
        }
    except:
        return {'MESSAGE':'You have to send label in a json request.'},400

    mutation=mutations.Item().mutation
    response=gql.mutate(mutation,vars)
    return response

@bp.route("color",methods=["POST"])
@login_required
def add_Color():
    try:
        vars={
            'label':request.json['label'],
        }
    except:
        return {'MESSAGE':'You have to send label in a json request.'},400

    mutation=mutations.Color().mutation
    response=gql.mutate(mutation,vars)
    return response

@bp.route("place",methods=["POST"])
@login_required
def add_place():
    try:
        vars={
            'label':request.json['label'],
        }
    except:
        return {'MESSAGE':'You have to send label in a json request.'},400

    mutation=mutations.Place().mutation
    response=gql.mutate(mutation,vars)
    return response