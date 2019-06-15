from pyramid.config import Configurator

try:
    # for python 2
    from urlparse import urlparse
except ImportError:
    # for python 3
    from urllib.parse import urlparse

from gridfs import GridFS
from pymongo import MongoClient

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes')

        db_url = urlparse(settings['mongo_uri'])
        config.registry.db = MongoClient(
            host='mongodb+srv://admin:1eKJSDKHiuf4@omnistack7-ke2gz.mongodb.net/test?retryWrites=true&w=majority'
        )

        def add_db(request):
            db = config.registry.db[db_url.path[1:]]
            return db
        
        def add_fs(request):
            return GridFS(request.db)

        config.add_request_method(add_db, 'db', reify=True)
        config.add_request_method(add_fs, 'fs', reify=True)

        config.scan()
    return config.make_wsgi_app()
