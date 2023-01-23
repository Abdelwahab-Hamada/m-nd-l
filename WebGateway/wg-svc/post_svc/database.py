import gridfs

from flask_pymongo import PyMongo

from decouple import config

mongo = PyMongo()
uri=f"mongodb://{config('DB_USER') }:{config('DB_PASSWORD')}@{config('DB_HOST')}:27017/{config('DB')}?authSource=admin"
