import os
from setuptools import setup

current_dir = os.path.abspath(os.path.dirname(__file__))

requires = [
    'pyyaml'
]

test_requirements = [
    'pytest'
]

packages = [
    'cdt'
]

setup(
    name='cdt-cli',
    url='https://github.com/cgDevTeams/cdt-cli',
    install_requires=requires,
    python_requires='>=3.7.*, <4',
    entry_points={
        'console_scripts': [
            'cdt = cdt.cli:main'
        ]
    },
    tests_require=test_requirements,
)