from setuptools import setup, find_packages
from great import GREAT_COMMANDS
setup(
    name='great',
    version='0.1',
    packages=['great'],
    description="for when it's really great",
    entry_points={
        'console_scripts': [
            '{}=great.great:main'.format(name) for name in GREAT_COMMANDS
        ],
    },
)
