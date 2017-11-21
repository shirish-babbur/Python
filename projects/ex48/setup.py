try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readme():
    with open("README.rst") as f:
        return f.read()

config = {
    'description' : 'My First Project In Python',
    'author' : 'Shirish Babbur',
    'url' : 'Soon!',
    'download_url' : 'https://abc.com/',
    'author_email' : 'bbshirish@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'test_suite' : 'nose.collector',
    'test_require' : ['nose'],
    'packages' : ['ex48'],
    'scripts' : ['bin/starter-engine'],
    'name' : 'Exercise - 48'
}

setup(**config)
