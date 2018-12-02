import os
from aiohttp import web

from core.routes import setup_routes
from scrapper.settings import GlobalConfig


DEBUG = os.environ.get('DEBUG')


GlobalConfig().init()

application = web.Application()
setup_routes(application)

