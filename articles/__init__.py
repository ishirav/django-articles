__version__ = '2.4.2'

default_app_config = 'articles.apps.ArticlesConfig'

from articles.directives import *
try:
    import listeners
except ImportError:
    # this happens when setup.py is grabbing __version__; nothing to worry
    # about
    pass

