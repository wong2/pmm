# -*-coding:utf-8-*-

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
STATUS_LABELS = {
    'green': 3,
    'yellow': 2,
    'red': 1,
    'unavailable': 0,
}


def fetch_mirrors_data():
    api_url = 'https://www.pypi-mirrors.org/data.json'
    r = requests.get(api_url, verify=False)
    return r.json()


def get_mirrors_data():
    mirrors = []
    mirrors_data = fetch_mirrors_data()
    for mirror, data in mirrors_data.items():
        data['index'] = mirror
        data['status'] = data.get('status', 'unavailable').lower()
        data['info'] = "{location}, status: {status}".format(**data)
        mirrors.append(data)
    mirrors.sort(key=lambda x: STATUS_LABELS.get(x['status'], 0), reverse=True)
    return mirrors
