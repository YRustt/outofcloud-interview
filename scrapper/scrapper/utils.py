import requests

from typing import List, Dict
from xml.etree import ElementTree
from bs4 import BeautifulSoup

from .settings import NEWS_TYPE, GRUB_TYPE
from .config import Config


def _get_field(xml: ElementTree, field: str, config: Config) -> str:
    root = xml

    for tag in config.item_fields[field]:
        for child in root:
            if child.tag == tag:
                root = child
                break
        else:
            raise ValueError("Not valid tags path to field %s: %s" % (field, str(config.item_fields[field])))

    return root.text


def _get_items(xml: ElementTree, config: Config) -> List[Dict[str, str]]:
    root = [xml]

    for tag in config.path_to_items:
        for child in root:
            if child.tag == tag:
                root = child
                break
        else:
            raise ValueError("Not valid tags path to items: %s" % str(config.path_to_items))

    result = []
    for child in root:
        if child.tag == config.item_tag:
            item = {field: _get_field(child, field, config) for field in config.item_fields}
            result.append(item)

            if config.limit is not None and len(result) == config.limit:
                break

    return result


def parse_news(text: str, config: Config) -> List[Dict[str, str]]:
    xml = ElementTree.fromstring(text)
    items = _get_items(xml, config)
    return items


def parse_grub(text: str, config: Config) -> Dict[str, str]:
    html = BeautifulSoup(text)

    # TODO: add method for getting field value
    item = {
        field: html.find(**options).text for field, options in config.item_fields.items()
    }
    return item


async def fetch_url(config: Config):
    response = requests.get(config.url)

    if response.status_code == 200:
        text = response.text

        if config.request_type == NEWS_TYPE:
            return parse_news(text, config)
        elif config.request_type == GRUB_TYPE:
            return parse_grub(text, config)
