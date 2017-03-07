# -*-coding:utf-8-*-

import os
import shlex
from configparser import ConfigParser
from distutils.util import strtobool

from pip.locations import legacy_config_file
from pmm.utils import ensure_file


class ConfigFile(object):
    def __init__(self):
        self.config_parser = ConfigParser()
        if os.path.exists(self.path):
            self.config_parser.read(self.path)

    def get(self, section, name, default=None):
        return self.config_parser.get(section, name, fallback=default)

    def getbool(self, section, name, default=None):
        try:
            return strtobool(self.get(section, name, 'false'))
        except ValueError:
            return False

    def set(self, section, name, value):
        if not self.config_parser.has_section(section):
            self.config_parser.add_section(section)

        self.config_parser.set(section, name, value)

        ensure_file(self.path)
        with open(self.path, 'w') as fp:
            self.config_parser.write(fp)

    def getlist(self, section, option, default=None):
        if not self.config_parser.has_option(section, option):
            return [] if default is None else default

        value = self.get(section, option)
        if '\n' in value:
            return [item.strip()
                    for item in value.splitlines() if item.strip()]
        else:
            return shlex.split(value)


class PipConfig(ConfigFile):
    # TODO: use new config file path.
    path = legacy_config_file

    def get_index_url(self):
        return self.get('global', 'index-url')

    def set_index_url(self, index_url):
        return self.set('global', 'index-url', index_url)

    def get_index_servers(self):
        servers = []
        for sect in self.getlist('global', 'index-servers'):
            url = self.get(sect, 'index')
            if url:
                servers.append({
                    'index': url,
                    'info': self.get(sect, 'info', 'n/a')
                })
        return servers
