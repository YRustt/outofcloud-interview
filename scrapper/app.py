from aiohttp import web

from routes import setup_routes


application = web.Application()
setup_routes(application)
web.run_app(application)
