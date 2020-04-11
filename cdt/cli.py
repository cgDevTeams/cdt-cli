import os
import sys
import glob
from importlib import import_module

commands = [
    'setup',
    'format',
]


def main():

    if not len(sys.argv) >= 2:
        exit('This tool needs command with base command "cdt". See "cdt help" help to check available commands.')

    command = sys.argv[1]

    if command in commands:
        module = import_module('cdt.{}'.format(command))
        module.main()
    elif command == 'help':
        exit('''Available cdt commands: {}. To see each help, excute "cdt <commnd> -h"'''.format(
            ', '.join(['"{}"'.format(c) for c in commands])))
    else:
        exit('"{}" is not a cdt command. See "cdt help".'.format(command))
