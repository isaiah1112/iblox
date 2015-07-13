#!/usr/bin/env python2
# coding=utf-8
"""Setup file for infoblox module"""

from distutils.core import setup

import infoblox

setup(name='infoblox',
      version=infoblox.__version__,
      description='Python Infoblox WAPI Module',
      author='Jesse Almanrode',
      author_email='jesse@almanrode.com',
      url='https://bitbucket.org/isaiah1112/infoblox',
      py_modules=['infoblox'],
      license='GNU Lesser General Public License v3 or later (LGPLv3+)',
      install_requires=['simplejson>=3.6.5',
                        'requests>=2.7.0',
                        ],
      platforms='any',
      classifiers=[
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
