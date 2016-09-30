import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-publishing",
    version="0.1-alpha",
    packages=find_packages(),
    license="MIT License",
    description="A basic django app to publish models with a workflow and permissions",
    long_description=README,
    url="https://wwww.s-v.de",
    author="Scholz & Volkmer (Domenik Jones)",
    author_email="d.jones@s-v.de",
)