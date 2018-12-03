import os
import json

from .exceptions import NotInitializedGlobalConfig


NEWS_TYPE = 'news'
GRUB_TYPE = 'grub'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILENAME = os.path.join(BASE_DIR, 'config.json')


class GlobalConfig:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def init(self):
        with open(CONFIG_FILENAME, 'r') as f:
            self.config = json.load(f)

    def save(self):
        if not hasattr(self, 'config'):
            raise NotInitializedGlobalConfig()

        with open(CONFIG_FILENAME, 'w') as f:
            json.dumps(self.config)

    def register(self, name, config):
        if not hasattr(self, 'config'):
            raise NotInitializedGlobalConfig()

        self.config[name] = config
        self.save()

    def __iter__(self, name):
        if not hasattr(self, 'config'):
            raise NotInitializedGlobalConfig()

        return iter(self.config)

    def __getitem__(self, item):
        if not hasattr(self, 'config'):
            raise NotInitializedGlobalConfig()

        return self.config[item]
