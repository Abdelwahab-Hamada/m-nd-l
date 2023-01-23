import gridfs

from bson.objectid import ObjectId

from flask import (
    Blueprint,
    request,
    send_file
)

from auth_svc.decorators import (
    login_required,
    uid_required
)

from . import (
    gql,
    queries,
    mutations,
    database
)

bp=Blueprint('post_svc', __name__,url_prefix='/')

@bp.route("image",methods=["POST"])
def get_image():
    try:
        imageID=request.json['imageID']
        fs=gridfs.GridFS(database.mongo.db)
        image=fs.get(ObjectId(imageID))
    except Exception as error:
        if str(type(error)) == "<class 'gridfs.errors.NoFile'>":
            return {'MESSAGE':'This image had been deleted.'},404
        return {'MESSAGE':'No image for this post.'},404

    return send_file(image, download_name=f"{imageID}.png")

@bp.route("lost-posts",methods=["POST"])
def lost_posts():
    try:
        string=request.json['contains']
    except:
        return {'MESSAGE':'You have to send contains in a json request.'},400

    query=queries.LostPosts()
    query.set_contains(string)
    response=gql.query(query.query)
    return response

@bp.route("found-posts",methods=["POST"])
def found_posts():
    try:
        string=request.json['contains']
    except:
        return {'MESSAGE':'You have to send contains in a json request.'},400
    query=queries.FoundPosts()
    query.set_contains(string)
    response=gql.query(query.query)
    return response
    
@bp.route("items",methods=["POST"])
def items():
    try:
        string=request.json['contains']
    except:
        return {'MESSAGE':'You have to send contains in a json request.'},400

    query=queries.Items()
    query.set_contains(string)
    response=gql.query(query.query)
    return response

@bp.route("item",methods=["POST"])
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
@bp.route("post-image",methods=["POST"])
@login_required
def post_image():
    try:
        files=request.files
        image=files['img']
    except:
        return {'MESSAGE':'Image required.'}
    
    fs=gridfs.GridFS(database.mongo.db)
    imageID = fs.put(image)
    return {'imageID':str(imageID)}

@bp.route("delete-image",methods=["POST"])
@login_required
def delete_image():
    try:
        imageID=request.json['imageID']
    except:
        {'MESSAGE':f'Image id required.'},404
    
    objectId=ObjectId(imageID)
    fs=gridfs.GridFS(database.mongo.db)

    if fs.exists(objectId):
        fs.delete(objectId)
        return {'MESSAGE':f'Image deleted.'}
    return {'MESSAGE':f'Image not exists.'},404


@bp.route("post-lost",methods=["POST"])
@login_required
@uid_required
def post_lost(uid):
    try:        
        vars={
            "uid":uid,
            "description":request.json['description'],
            "imageId":request.json.get('imageId') or None,#get is to avoid error
            "itemId":request.json['itemId'],
            "colorId":request.json['colorId'],
            "placeId":request.json['placeId'],
        }
    except:
        return {'MESSAGE':'''You have to send description,itemId,colorId,placeId in a json request.'''},400

    mutation=mutations.Lost().mutation
    response=gql.mutate(mutation,vars)
    return response

@bp.route("post-found",methods=["POST"])
@login_required
@uid_required
def post_found(uid):
    try:
        vars={
            "uid":uid,
            "description":request.json['description'],
            "imageId":request.json.get('imageId') or None,#get is to avoid error
            "itemId":request.json['itemId'],
            "colorId":request.json['colorId'],
            "placeId":request.json['placeId'],
        }
    except:
        return {'MESSAGE':'''You have to send description,itemId,colorId,placeId in a json request.'''},400

    mutation=mutations.Found().mutation
    response=gql.mutate(mutation,vars)
    return response
    

@bp.route("add-item",methods=["POST"])
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

@bp.route("add-color",methods=["POST"])
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

@bp.route("add-place",methods=["POST"])
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