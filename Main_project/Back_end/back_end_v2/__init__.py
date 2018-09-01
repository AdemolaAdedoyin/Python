from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')
    config.add_static_view(name='static', path='static')
    config.add_route('home', '/')
    config.add_route('home1', '/home')
    config.add_route('get_all_words', '/getAllWords')
    config.add_route('get_one_where', '/get/{word}/{pos}')
    config.add_route('get_all_videos', '/getAllVideos')
    config.add_route('create', '/create')
    config.add_route('get_all_universaltags', '/getAllTags')
    config.add_route('delete_where', '/delete/{table_name}/{location}={id}')
    config.add_route('update_where', '/update/{table_name}')
    config.scan()
    return config.make_wsgi_app()
