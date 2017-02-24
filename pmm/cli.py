#-*-coding:utf-8-*-

from __future__ import print_function

import blindspin
import crayons
from pick import pick

from pmm import config
from pmm.data import get_mirrors_data


def format_index_url(mirror):
    return 'https://{mirror}/simple'.format(mirror=mirror)


def main():
    with blindspin.spinner():
        mirrors = get_mirrors_data()

    current_index_url = config.get_index_url()

    current_index, choices = 0, []
    for i, mirror in enumerate(mirrors):
        if format_index_url(mirror) == current_index_url:
            current_index = i
        choices.append(mirror)

    choosed_mirror, _ = pick(choices, indicator='=>', default_index=current_index)

    choosed_index_url = format_index_url(choosed_mirror)
    config.set_index_url(choosed_index_url)

    print(u'✨  using mirror {} now'.format(crayons.cyan(choosed_index_url)))


if __name__ == '__main__':
    main()