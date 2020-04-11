import os
import sys
import glob
from importlib import import_module

commands = [
    'setup'
]


def main():
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    if command in commands:
        module = import_module('cdt.{}'.format(command))
        module.main(args)
    else:
        exit('{} is not a cdt command. See "cdt help".'.format(command))