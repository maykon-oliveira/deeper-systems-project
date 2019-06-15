from pyramid.view import view_config


@view_config(route_name='videos', renderer='../templates/videos.jinja2')
def listVideos(request):
    videos = request.db['videos'].find()
    return {'videos': videos}
