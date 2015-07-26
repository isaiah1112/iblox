#!/usr/bin/env python2
# coding=utf-8
"""Unit Tests for iblox Python Module"""
__author__ = 'Jesse Almanrode'

import os
import sys
import unittest
from simplejson.decoder import JSONDecodeError

here = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(here)
sys.path.append(project)
import iblox

# You must change the following URL to a valid instance of Infoblox.  I suggest using your lab/test env
wapiurl = 'https://infoblox.example.com/wapi/v1.7.1/'
wapiuser = 'admin'
wapipass = 'infoblox'


class Testiblox(unittest.TestCase):
    def setUp(self):
        global wapiurl, wapiuser, wapipass
        self.iblox_conn = iblox.Infoblox(wapiurl, username=wapiuser, password=wapipass)

    def assert_zone_exists(self):
        result = self.iblox_conn.get(objtype='zone_auth', fqdn='unittest.example')
        assert isinstance(result, list)
        if len(result) == 0:
            return False
        else:
            return True

    def assert_host_exists(self):
        result = self.iblox_conn.get(objtype='record:host', name='testhost.unittest.example')
        assert isinstance(result, list)
        if len(result) == 0:
            return False
        else:
            return True

    def test_000_Login(self):
        try:
            result = self.iblox_conn.get(objtype='view', name='default')
            if type(result) is dict:
                self.fail(result['text'])
            elif type(result) is list:
                self.assertIsInstance(result[0], dict)
        except JSONDecodeError:
            self.fail('Unable to login to Infoblox instance')

    def test_001_Add_Zone(self):
        self.assertFalse(self.assert_zone_exists())
        result = self.iblox_conn.add(objtype='zone_auth', fqdn='unittest.example')
        self.assertIsInstance(result, unicode)

    def test_002_Add_Host(self):
        self.assertTrue(self.assert_zone_exists())
        self.assertFalse(self.assert_host_exists())
        result = self.iblox_conn.add_host('testhost.unittest.example', '192.168.2.2', comment='Created by test_infoblox.py')
        self.assertIsInstance(result, unicode)

    def test_003_Add_Alias(self):
        self.assertTrue(self.assert_zone_exists())
        self.assertTrue(self.assert_host_exists())
        result = self.iblox_conn.add_alias('testhost.unittest.example', 'testalias.unittest.example')
        self.assertIsInstance(result, unicode)

    def test_004_Delete_Alias(self):
        self.assertTrue(self.assert_zone_exists())
        self.assertTrue(self.assert_host_exists())
        result = self.iblox_conn.delete_alias('testhost.unittest.example', 'testalias.unittest.example')
        self.assertIsInstance(result, unicode)

    def test_010_Delete_Host(self):
        self.assertTrue(self.assert_zone_exists())
        self.assertTrue(self.assert_host_exists())
        result = self.iblox_conn.get_host_by_name('testhost.unittest.example')[0]
        result = self.iblox_conn.delete(result['_ref'])
        self.assertIsInstance(result, unicode)

    def test_020_Delete_Zone(self):
        self.assertTrue(self.assert_zone_exists())
        zone = self.iblox_conn.get(objtype='zone_auth', fqdn='unittest.example')[0]
        result = self.iblox_conn.delete(zone['_ref'])
        self.assertIsInstance(result, unicode)

if __name__ == '__main__':
    unittest.main(failfast=True)
