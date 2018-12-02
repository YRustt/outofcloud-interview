from typing import Optional, Tuple, Dict
from dataclasses import dataclass

from .settings import NEWS_TYPE, GRUB_TYPE, GlobalConfig


@dataclass(
    init=True,
    repr=True,
    eq=False,
    order=False,
    unsafe_hash=False,
    frozen=True
)
class Config:
    name: str
    url: str
    limit: Optional[int]
    request_type: str
    path_to_items: Tuple[str]
    item_tag: str
    item_fields: Dict[str, Tuple[str]]


def make_config(**kwargs):
    global_config = GlobalConfig()

    name = kwargs.get('name')
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
            limit=None,
            path_to_items=None,
            item_tag=None,
            item_fields=item_fields
        )
    else:
        raise ValueError('Not valid request type')


