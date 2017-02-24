#-*-coding:utf-8-*-

import requests
from collections import OrderedDict

STATUS_LABELS = OrderedDict([
    ('green', 'fresh'),
    ('yellow', 'aging'),
    ('red', 'old'),
    ('unavailable', 'n/a'),
])

def fetch_mirrors_data():
    api_url = 'https://www.pypi-mirrors.org/data.json'
    r = requests.get(api_url)
    return r.json()


def get_mirrors_data():
    mirrors = []
    mirrors_data = fetch_mirrors_data()
    for mirror, data in mirrors_data.items():
        mirrors.append((mirror, data['status'].lower()))
    mirrors.sort(key=lambda x: list(STATUS_LABELS).index(x[1]))
    return [mirror for mirror, status in mirrors]
