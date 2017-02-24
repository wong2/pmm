#-*-coding:utf-8-*-

import requests
import requests_cache
from collections import OrderedDict

requests_cache.install_cache(expire_after=600)  # cache api result for 10min

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
    for mirror, data in mirrors_data.iteritems():
        mirrors.append((mirror, data['status'].lower()))
    mirrors.sort(key=lambda (mirror, status): list(STATUS_LABELS).index(status))
    return [mirror for mirror, status in mirrors]