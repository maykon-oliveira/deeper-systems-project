from pyramid.view import view_config
from bson.son import SON

@view_config(route_name='videos', renderer='../templates/videos.jinja2')
def listVideos(request):
    videos = None
    try:
        sort = request.params['sort']
        if sort:
            pipeline = [
                # { "$group" : { "_id" : "$theme" } } ,
                { "$project": {
                    "theme": 1,
                    "score": {
                        "$subtract": [ "$likes" , { "$divide": [ "$deslikes", 2] } ]
                        }
                    }
                },
                { "$sort": { "score": -1 } }
            ]
            videos = request.db['videos'].aggregate(pipeline)
            return {'videos': videos, 'sorted': True}
        else:
            videos = request.db['videos'].find()
            return {'videos': videos, 'sorted': False}
    except:
        videos = request.db['videos'].find()
        return {'videos': videos, 'sorted': False}