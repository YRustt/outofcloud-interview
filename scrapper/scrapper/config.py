from typing import Tuple, Dict
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
    limit: int
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
    elif request_type == GRUB_TYPE:
        url = kwargs.get('url')
        limit = None
    else:
        raise ValueError('Not valid request type')

    return Config(
        name=name,
        url=url,
        request_type=request_type,
        limit=limit,
        path_to_items=global_config[name][request_type]['path_to_items'],
        item_tag=global_config[name][request_type]['item_tag'],
        item_fields=global_config[name][request_type]['item_fields']
    )
