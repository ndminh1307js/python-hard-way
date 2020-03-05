try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project Skeleton',
    'author': 'Dang Minh',
    'url': 'none',
    'downloadUrl': 'Where to download it',
    'authorEmail': 'ndminh1307js@gmail.com',
    'version': '0.1',
    'installRequires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectskeleton'
}

setup(**config)
