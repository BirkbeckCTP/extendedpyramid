from pyramid.config import Configurator

from basepyramid import app
from basepyramid import assets
import pyramid
import basepyramid


def includeme(config):
    config.registry.settings.setdefault('webassets.bundles', 'extendedpyramid:assets.yaml')
    config.include('pyramid_webassets')
    #this is instruction to pyramid to override asset from teh base pyramid application
    #config.override_asset(
    #    to_override='basepyramid:templates/base.html.jinja2',
    #   override_with='extendedpyramid:templates/base.html.jinja2')

    config.commit()

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.scan(basepyramid.app)
    config.include(basepyramid.app)
    config.include(__name__)
    return config.make_wsgi_app()
