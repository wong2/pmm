# -*-coding:utf-8-*-

import os
import errno


def ensure_dir(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def ensure_file(path):
    """
    ensures that the file exists, also create the missing directories
    """
    basedir = os.path.dirname(path)
    ensure_dir(basedir)
    open(path, 'a').close()
