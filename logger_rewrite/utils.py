import requests
from pathlib import Path
import json
from collections import OrderedDict


def read_json(filename):
    filename = Path(filename)
    with filename.open('rt', encoding='utf-8') as handle:
        return json.load(handle, object_hook=OrderedDict)


def download_config(id):
    url = 'https://raw.githubusercontent.com/cuongngm/logger_rewrite/why/config/{}'.format(id)
    r = requests.get(url)
    config = read_json(r)
    return config


class Cfg(dict):
    def __init__(self, config_dict):
        super(Cfg, self).__init__(**config_dict)
        self.__dict__ = self

    @staticmethod
    def load_config_from_name():
        base_config = download_config('logger_config.json')
        config = download_config('logger_config.json')

        base_config.update(config)
        return Cfg(base_config)
