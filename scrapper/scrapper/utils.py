import requests

from typing import List, Dict
from xml.etree import ElementTree
from bs4 import BeautifulSoup

from .settings import NEWS_TYPE, GRUB_TYPE
from .config import Config
from .exceptions import NotValidTagsPath


def _get_field_for_news(xml: ElementTree, field: str, config: Config) -> str:
    root = xml

    for tag in config.item_fields[field]:
        for child in root:
            if child.tag == tag:
                root = child
                break
        else:
            raise NotValidTagsPath("Not valid tags path to field %s: %s" % (field, str(config.item_fields[field])))

    return root.text


def _get_items_for_news(xml: ElementTree, config: Config) -> List[Dict[str, str]]:
    root = [xml]

    for tag in config.path_to_items:
        for child in root:
            if child.tag == tag:
                root = child
                break
        else:
            raise NotValidTagsPath("Not valid tags path to items: %s" % str(config.path_to_items))

    result = []
    for child in root:
        if child.tag == config.item_tag:
            item = {field: _get_field_for_news(child, field, config) for field in config.item_fields}
            result.append(item)

            if config.limit is not None and len(result) == config.limit:
                break

    return result


def parse_news(text: str, config: Config) -> List[Dict[str, str]]:
    xml = ElementTree.fromstring(text)
    items = _get_items_for_news(xml, config)
    return items


def _get_grub_child_repr(child, tag: str) -> str:
    if tag == "img":
        return child.attrs["src"]
    elif tag == "a":
        return child.attrs["href"]
    else:
        return child.text


def _get_grub_field(html: BeautifulSoup, field: str, config: Config) -> str:
    options = config.item_fields[field]

    tag = options.get("tag", None)
    item = html.find(name=options["name"], attrs=options["attrs"])
    if tag is not None:
        result = [_get_grub_child_repr(child, tag) for child in item.find_all(tag)]
    else:
        result = item.text

    return result


def parse_grub(text: str, config: Config) -> Dict[str, str]:
    html = BeautifulSoup(text)

    item = {
        field: _get_grub_field(html, field, config) for field in config.item_fields.keys()
    }
    return item


async def fetch_url(config: Config):
    """Function for getting list of detail information about news.

    :param config: instance of Config class
    :return: list of dicts or dict with information about news.
    """

    response = requests.get(config.url)

    if response.status_code == 200:
        text = response.text

        if config.request_type == NEWS_TYPE:
            return parse_news(text, config)
        elif config.request_type == GRUB_TYPE:
            return parse_grub(text, config)
