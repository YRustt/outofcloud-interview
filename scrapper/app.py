from aiohttp import web

from core.routes import setup_routes
from scrapper.settings import GlobalConfig


GlobalConfig().init()

application = web.Application()
setup_routes(application)
web.run_app(application)
