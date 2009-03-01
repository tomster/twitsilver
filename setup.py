from setuptools import setup, find_packages
from os import path

DEST_DIR = path.join(path.expanduser("~"), 
    "Desktop/")

version = '0.1.8'

setup(name='twitsilver',
    version=version,
    description="A Quicksilver client for twitter",
    long_description=open("README.txt").read() + "\n" +
        open(path.join("README.txt")).read(),
    classifiers=[
    "Development Status :: 3 - Alpha",
    "Environment :: MacOS X",
    "Operating System :: MacOS :: MacOS X",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: BSD License",
    "Topic :: Communications",
    ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='Quicksilver twitter OSX',
    author='Tom Lazar',
    author_email='tom@tomster.org',
    url='http://tomster.org/',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      # -*- Extra requirements: -*-
      "py_Growl",
      "twitter",
    ],
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    tweet=twitsilver.tweet:main
    install_twitsilver_action=twitsilver.install_twitsilver_action
    """,
    )

