def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('videos', '/')
    config.add_route('video_like', '/videos/{id}/like')
    config.add_route('video_deslike', '/videos/{id}/deslike')
    config.add_route('new', '/new')
