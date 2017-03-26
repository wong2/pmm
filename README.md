### PyPi Mirror Manager [![PyPI](https://img.shields.io/pypi/v/pmm.svg)](https://pypi.python.org/pypi/pmm)

![command line demo](demo.gif)

#### Installation

    pip install pmm

#### Usage

    usage: pmm [-h] [-m]

    Select PyPI index server used by pip.

    optional arguments:
      -h, --help     show this help message and exit
      -m, --mirrors  download list of PyPI mirrors and add them to selection

#### Configuration

You can add package indexes to your `pip.conf` file. Example:

    [global]
    use-wheel = True
    index-url = https://pypi.python.org/simple
    index-servers =
        pypi
        pypi-test
        my-devpi

    [pypi]
    index = pypi.python.org

    [pypi-test]
    index = testpypi.python.org/pypi

    [my-devpi]
    index = devpi.example.com/main/dev
    info = Development team local package index

If you have any indexes listed in the `index-servers` setting in the `globals`
section, `pmm` will then only offer these indexes for selection, unless you use
the `-m` command line option.

#### Authors

* [wong2](https://github.com/wong2)
* [SpotlightKid](https://github.com/SpotlightKid)

#### Credits

* inspired by https://github.com/Pana/nrm
* mirrors data from https://www.pypi-mirrors.org/
* [pick](https://github.com/wong2/pick) for the interactive selection list
