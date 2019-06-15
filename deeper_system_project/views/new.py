from pyramid.view import view_config
import datetime

@view_config(route_name='new', renderer='../templates/new.jinja2')
def form_video(request):
    if request.POST:
        name = request.POST['name']
        theme = request.POST['theme']
        video = {
            "name": name,
            "theme": theme,
            "likes": 0,
            "createdAt": datetime.datetime.utcnow()
        }
        request.db['videos'].insert_one(video)
    return {}
