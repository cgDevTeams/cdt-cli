import os
import sys
import platform
import datetime
from pathlib import Path
import yaml


class Config(object):

    def __init__(self, name='', *args):
        super(Config, self).__init__()
        self.name = name
        self.data = dict()
        self.config_path = self.create_config_path()

        if not self.config_path.exists():
            self._create_initial_config()
        else:
            self.load_config()


    def create_config_path(self):
        """
        Create user config path
        """
        config_filename = '{}.yaml'.format(self.name)

        if platform.system() == 'Windows':
            config_dir = Path(os.getenv('APPDATA'), 'cdt')

        elif platform.system() == 'Linux' or 'Darwin':
            config_dir = Path(os.getenv('HOME'), '.cdt')

        else:
            print('This platform is not suported.')
            return

        if not config_dir.exists():
            config_dir.mkdir(parents=True)

        config_path = config_dir / config_filename

        return config_path


    def _create_initial_config(self):
        """
        If config file doesn't exist, this will be called after checking.
        """
        data = {
            'user': os.getenv('USERNAME'),
            'create_date': str(datetime.date.today())
        }

        self.save_config(data)


    def load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as cf:
            self.data = yaml.safe_load(cf)


    def save_config(self, data):
        with open(self.config_path, 'w', encoding='utf-8') as cf:
            self.data = yaml.safe_dump(data, cf)