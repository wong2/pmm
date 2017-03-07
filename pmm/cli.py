# -*-coding:utf-8-*-
"""Select PyPI index server used by pip."""

from __future__ import print_function

import argparse
import re
import sys

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import blindspin
import crayons
from pick import pick

from pmm.config import PipConfig
from pmm.data import get_mirrors_data


def format_index_url(url):
    if not re.match(r'\w+://', url):
        url = 'https://' + url
    if not url.endswith('/simple'):
        url = url.rstrip('/') + '/simple'
    return url


def main(args=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        '-m',
        '--mirrors',
        action="store_true",
        help="download list of PyPI mirrors and add them to selection")
    args = ap.parse_args(sys.argv[1:] if args is None else args)

    pip_config = PipConfig()
    urls = OrderedDict()
    for server in pip_config.get_index_servers():
        f_url = format_index_url(server['index'])
        urls[f_url] = server

    if not urls and not args.mirrors:
        print(crayons.yellow("No indexes found in {0}".format(pip_config.path)))

    if args.mirrors or not urls:
        print(crayons.magenta("Downloading mirror list"), end=' ')
        with blindspin.spinner():
            for mirror in get_mirrors_data():
                f_url = format_index_url(mirror['index'])
                urls[f_url] = mirror

    current_index_url = pip_config.get_index_url()
    current_index, choices = 0, []

    for i, url in enumerate(urls):
        if current_index_url and url == current_index_url:
            current_index = i
        choices.append("{index} ({info})".format(**urls[url]))

    try:
        _, index = pick(choices, indicator='=>', default_index=current_index)
    except KeyboardInterrupt:
        return 1

    chosen_url = tuple(urls)[index]
    pip_config.set_index_url(chosen_url)
    print('Changed pip index-url to {}'.format(crayons.cyan(chosen_url)))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
