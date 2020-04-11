"""Format files to each format rules.
Currently supports: Python files.

usage:
    format N <files>...
    format [-h]

positional:
    <files>  single file or mutiliple files, or directory for recursive formatting.

options:
    -h, --help  show this help message and exit
"""

import subprocess

from docopt import docopt


def main():
    args = docopt(__doc__)

    subprocess.call(['autopep8', '--recursive', '--in-place', args['<files>']])
