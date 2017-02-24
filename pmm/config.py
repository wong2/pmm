#-*-coding:utf-8-*-

import os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

from pip.locations import legacy_config_file
from pmm.utils import ensure_file


def get_pip_config_file_path():
    '''TODO: use new config file path
    '''
    return legacy_config_file


class PipConfig(object):

    def __init__(self):
        self.path = get_pip_config_file_path()
        self.config_parser = ConfigParser()
        if os.path.exists(self.path):
            self.config_parser.read(self.path)

    def get(self, section, name):
        if not self.config_parser.has_section(section):
            return
        return self.config_parser.get(section, name)

    def set(self, section, name, value):
        if not self.config_parser.has_section(section):
            self.config_parser.add_section(section)

        self.config_parser.set(section, name, value)

        ensure_file(self.path)
        with open(self.path, 'w') as fp:
            self.config_parser.write(fp)


pip_config = PipConfig()


def get_index_url():
    return pip_config.get('global', 'index-url')


def set_index_url(index_url):
    return pip_config.set('global', 'index-url', index_url)
