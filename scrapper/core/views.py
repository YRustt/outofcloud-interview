import json
import asyncio
from aiohttp import web

from scrapper.utils import fetch_url
from scrapper.config import make_config
from scrapper.settings import GlobalConfig


async def news(request):
    """Handler for getting list of news.

    :param request:

    e.g.: GET /news?name={name:str}&limit={limit:Optional[int]}
    where
        name - registered service's name
        limit - news count

    :return: json representations for list of news (see scrapper/utils.py)
    """

    name = request.rel_url.query.get('name')
    limit = request.rel_url.query.get('limit')
    if limit is not None:
        limit = int(limit)

    config = make_config(name=name, limit=limit, request_type='news')
    items = await fetch_url(config)
    text = json.dumps(items, ensure_ascii=False)

    return web.json_response(text=text)


async def grub(request):
    """Handler for getting detail information for one news

    :param request:

    e.g.: GET /grub?name={name:str}&url={url:str}
    where
        name - registered service's name
        url - url to news from news endpoint's response

    :return: json representation for one news (see scrapper/utils.py)
    """

    name = request.rel_url.query.get('name')
    url = request.rel_url.query.get('url')

    config = make_config(name=name, url=url, request_type='grub')
    item = await fetch_url(config)
    text = json.dumps(item, ensure_ascii=False)

    return web.json_response(text=text)


async def grubs(request):
    """Handler for getting detail information for many news

    :param request:

    e.g.: POST /grub
    with json {"name": "{name}", "urls": ["{url}", ...]}
    where
        name - registered service's name
        urls - list of urls to news from news endpoint's response

    :return: json representation for list of news details
    """

    data = json.loads(await request.text())

    name = data['name']
    urls = data['urls']

    configs = (make_config(name=name, url=url, request_type='grub') for url in urls)
    items = await asyncio.gather(*[fetch_url(config) for config in configs])
    text = json.dumps(items, ensure_ascii=False)

    return web.json_response(text=text)


async def register(request):
    """Handler for registering new service

    :param request:

    e.g.: POST /register
    with json {"name": "{name}", "config": {...}}
    where
        name - registered service's name
        config - dict with information about service (see scrapper/config.py)

    :return:
    """

    global_config = GlobalConfig()

    if request.method == 'POST':
        data = json.loads(await request.text())

        name = data['name']
        config = data['config']

        global_config.register(name=name, config=config)

        return web.Response(reason='registered')
    elif request.method == 'GET':
        keys = list(global_config.keys())
        text = json.dumps(keys, ensure_ascii=False)

        return web.json_response(text)
