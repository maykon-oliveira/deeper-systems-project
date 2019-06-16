from pyramid.view import view_config
from pyramid.response import Response
from bson.objectid import ObjectId


@view_config(route_name='video_like')
def likeAVideo(request):
    video = request.db['videos'].find_one_and_update({'_id': ObjectId(request.matchdict['id'])}, {'$inc': {'likes': 1}})
    return Response(location=request.route_url('videos'), status_code=302)

@view_config(route_name='video_deslike')
def deslikeAVideo(request):
    video = request.db['videos'].find_one_and_update({'_id': ObjectId(request.matchdict['id'])}, {'$inc': {'deslikes': 1}})
    return Response(location=request.route_url('videos'), status_code=302)