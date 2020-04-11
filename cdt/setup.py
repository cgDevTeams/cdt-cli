"""Setup environemnt as creating config file.

usage:
    setup N
    setup [-h]

options:
    -h, --help  show this help message and exit
"""

from docopt import docopt

from pprint import pprint

from . import config

def main():
    args = docopt(__doc__)

    user_conf = config.Config('user')
    pprint(user_conf.data)
    print('User config is created at : {}'.format(user_conf.config_path))