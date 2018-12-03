from typing import Optional, Tuple, Dict
from dataclasses import dataclass

from .settings import NEWS_TYPE, GRUB_TYPE, GlobalConfig
from .exceptions import NotRegisteredService, NotValidRequestType


@dataclass(
    init=True,
    repr=True,
    eq=False,
    order=False,
    unsafe_hash=False,
    frozen=True
)
class Config:
    """Information for making request.

    Attributes:
        name - registered service's name
        url - url for making request
        limit - count of items which need to fetch
        request_type - type of request ('news' or 'grub')
        path_to_items - list of xml tags (path to items) (used only for 'news' request_type)
        item_tag - xml tag for item (used only for 'news' request_type)
        item_fields - dict with information about fields which need to fetch (see scrapper/config.json)
    """

    name: str
    url: str
    limit: Optional[int] = None
    request_type: Optional[str] = None
    path_to_items: Optional[Tuple[str]] = None
    item_tag: Optional[str] = None
    item_fields: Optional[Dict[str, Tuple[str]]] = None


def make_config(**kwargs):
    """Function for creating config."""

    global_config = GlobalConfig()

    name = kwargs.get('name')
    if name not in global_config:
        raise NotRegisteredService()

    request_type = kwargs.get('request_type')

    if request_type == NEWS_TYPE:
        url = global_config[name][request_type]['url']
        limit = kwargs.get('limit')

        path_to_items = kwargs.get('path_to_items') or global_config[name][request_type]['path_to_items']
        item_tag = kwargs.get('item_tag') or global_config[name][request_type]['item_tag']
        item_fields = kwargs.get('item_fields') or global_config[name][request_type]['item_fields']

        return Config(
            name=name,
            url=url,
            request_type=request_type,
            limit=limit,
            path_to_items=path_to_items,
            item_tag=item_tag,
            item_fields=item_fields
        )
    elif request_type == GRUB_TYPE:
        url = kwargs.get('url')

        item_fields = kwargs.get('item_fields') or global_config[name][request_type]['item_fields']

        return Config(
            name=name,
            url=url,
            request_type=request_type,
            item_fields=item_fields
        )
    else:
        raise NotValidRequestType()


