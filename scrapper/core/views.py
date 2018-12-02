import json
import logging
import asyncio
from aiohttp import web

from scrapper.utils import fetch_url
from scrapper.config import make_config


logger = logging.getLogger(__name__)


async def news(request):
    name = request.rel_url.query.get('name')
    limit = request.rel_url.query.get('limit')
    if limit is not None:
        limit = int(limit)

    config = make_config(name=name, limit=limit, request_type='news')
    items = await fetch_url(config)
    text = json.dumps(items, ensure_ascii=False)

    return web.json_response(text=text)


async def grub(request):
    name = request.rel_url.query.get('name')
    url = request.rel_url.query.get('url')

    config = make_config(name=name, url=url, request_type='grub')
    item = await fetch_url(config)
    text = json.dumps(item, ensure_ascii=False)

    return web.json_response(text=text)


async def grubs(request):
    data = json.loads(await request.text())

    name = data['name']
    urls = data['urls']

    configs = (make_config(name=name, url=url, request_type='grub') for url in urls)
    items = await asyncio.gather(*[fetch_url(config) for config in configs])
    text = json.dumps(items, ensure_ascii=False)

    return web.json_response(text=text)


async def register(request):
    pass
