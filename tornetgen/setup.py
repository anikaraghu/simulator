#!/usr/bin/env python

from distutils.core import setup

setup(name='TorNetGen',
      version="1.0.1",
      description='A utility to generate private Tor network configurations',
      author='Rob Jansen',
      url='https://github.com/shadow/tornetgen',
      packages=['tornetgen'],
      scripts=['tornetgen/tornetgen'],
     )
