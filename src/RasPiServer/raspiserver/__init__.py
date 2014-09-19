from pyramid.config import Configurator
import logging
log = logging.getLogger(__name__)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    log.info('Starting RaspiServer...')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('led_mode_on', 'led_mode_on')
    config.add_route('led_mode_off', 'led_mode_off')
    config.add_route('led_on', 'led_on')
    config.add_route('led_off', 'led_off')
    config.add_route('shutdown', 'shutdown')
    config.scan()
    log.info('RaspiServer Started')
    return config.make_wsgi_app()
