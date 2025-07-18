from flask import current_app, g
from pymongo import MongoClient


def init_db(app):
    @app.before_request
    def before_request():
        g.mongo_client = MongoClient(app.config.get('MONGO_URI'))
        g.db = g.mongo_client.get_default_database()

    @app.teardown_request
    def teardown_request(exception):
        client = g.pop('mongo_client', None)
        if client is not None:
            client.close()
