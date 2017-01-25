#!/usr/bin/env python2
# coding=utf-8
"""Setup file for iblox module
"""

from setuptools import setup

setup(name='iblox',
      version='1.5.2',
      description='Infoblox WAPI Module',
      author='Jesse Almanrode',
      author_email='jesse@almanrode.com',
      url='http://pythonhosted.org/iblox',
      py_modules=['iblox'],
      license='GNU Lesser General Public License v3 or later (LGPLv3+)',
      install_requires=['future==0.16.0',
                        'requests==2.13.0',
                        'simplejson==3.10.0',
                        ],
      platforms=['Darwin', 'Linux'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: Unix',
          'Operating System :: Darwin',
          'Operating System :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
