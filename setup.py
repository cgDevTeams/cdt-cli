import os
from setuptools import setup
from setuptools import find_packages

current_dir = os.path.abspath(os.path.dirname(__file__))

requires = [
    'pyyaml',
    'autopep8',
    'docopt'
]

test_requirements = [
    'pytest'
]

setup(
    name='cdt-cli',
    url='https://github.com/cgDevTeams/cdt-cli',
    install_requires=requires,
    python_requires='>=3.7.*, <4',
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'cdt = cdt.cli:main'
        ]
    },
    tests_require=test_requirements,
)