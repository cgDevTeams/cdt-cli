from pprint import pprint

from . import config

def main(args):
    user_conf = config.Config('user')
    pprint(user_conf.data)
    print('User config is created at : {}'.format(user_conf.config_path))