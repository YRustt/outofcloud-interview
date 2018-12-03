from aiohttp import web

from core.routes import setup_routes
from scrapper.settings import GlobalConfig
from scrapper.exceptions import (
    NotRegisteredService,
    NotInitializedGlobalConfig,
    NotValidRequestType,
    NotValidTagsPath
)


@web.middleware
async def error_middleware(request, handler):
    try:
        response = await handler(request)
        return response
    except (NotRegisteredService, NotInitializedGlobalConfig, NotValidRequestType, NotValidTagsPath) as ex:
        return web.json_response({"error": str(ex)}, status=500)


GlobalConfig().init()

application = web.Application(middlewares=[error_middleware])
setup_routes(application)

