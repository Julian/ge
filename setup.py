import os

from setuptools import find_packages, setup

from ge import __version__


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy"
]

setup(
    name="ge",
    version=__version__,
    packages=find_packages(),
    py_modules=(),
    author="Julian Berman",
    author_email="Julian@GrayVines.com",
    classifiers=classifiers,
    description="",
    license="MIT",
    long_description=long_description,
    url="",
)
