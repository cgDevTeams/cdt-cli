"""Command Line Tools for CG Dev Teams.

usage:
    cdt N ...
    cdt [-h | -v]

options:
    -h --help     show this help message and exit
    -v --version  show cdt package version
"""

import os
import sys
from importlib import import_module

from docopt import docopt

from . import __version__

commands = [
    'setup',
    'format',
]


def main():
    args = docopt(__doc__)

    if not args['N'] and not args['--version']:
        exit('This tool needs command with base command "cdt". See "cdt help" help to check available commands.')
    elif args['--version']:
        exit(__version__.__version__)

    command = args['N'][0]

    if command in commands:
        module = import_module('cdt.{}'.format(command))
        module.main()
    elif command == 'help':
        exit('''Available cdt commands: {}.\nTo see each help, excute "cdt <commnd> -h"'''.format(
            ', '.join(['"{}"'.format(c) for c in commands])))
    else:
        exit('"{}" is not a cdt command. See "cdt help".'.format(command))
