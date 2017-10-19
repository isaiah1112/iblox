#!/usr/bin/env python
# coding=utf-8
"""Integration and unit Tests for iblox Python Module"""
from __future__ import print_function
import os
import requests_mock
import sys
import unittest
import warnings
from builtins import str


__author__ = 'Jesse Almanrode'

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
import iblox


@requests_mock.Mocker()
class Testiblox(unittest.TestCase):

    def setUp(self):
        """ Even though this looks like a real connection, it isn't
        """
        self.iblox_conn = iblox.Infoblox('https://localhost/wapi/v2.3.1', username='admin', password='infoblox')

    def test_get(self, mock_adapter):
        """ Test Infoblox.get method
        """
        mock_adapter.get(requests_mock.ANY, json=[{'_ref': 'view/ZG5zLnZpZXckLl9kZWZhdWx0:default/true', 'is_default': True, 'name': 'default'}])
        result = self.iblox_conn.get(objtype='view', name='default')
        self.assertTrue(isinstance(result, list))
        self.assertEquals(len(result), 1)
        self.assertTrue(isinstance(result[0], dict))
        self.assertEquals(result[0]['_ref'], 'view/ZG5zLnZpZXckLl9kZWZhdWx0:default/true')
        pass

    def test_add(self, mock_adapter):
        """ Test Infoblox.add method
        """
        mock_adapter.post(requests_mock.ANY, json='zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3Q:unittest.example/default')
        result = self.iblox_conn.add(objtype='zone_auth', fqdn='unittest.example')
        self.assertTrue(isinstance(result, str))
        self.assertEquals(result, 'zone_auth/ZG5zLnpvbmUkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3Q:unittest.example/default')
        pass

    def test_add_host(self, mock_adapter):
        """ Test Infoblox.add_host method
        """
        mock_adapter.post(requests_mock.ANY, json='record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default')
        result = self.iblox_conn.add_host('testhost.unittest.example', '192.168.2.8', comment='Created by test_infoblox.py')
        self.assertTrue(isinstance(result, str))
        self.assertEquals(result, 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default')
        pass

    def test_add_alias(self, mock_adapter):
        """ Test Infoblox.add_alias method
        """
        mock_adapter.get(requests_mock.ANY, json=[{'_ref': 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default', 'ipv4addrs': [{'_ref': 'record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQuX2RlZmF1bHQuZXhhbXBsZS51bml0dGVzdC50ZXN0aG9zdC4xOTIuMTY4LjIuOC4:192.168.2.8/testhost.unittest.example/default', 'configure_for_dhcp': False, 'host': 'testhost.unittest.example', 'ipv4addr': '192.168.2.8'}], 'name': 'testhost.unittest.example', 'view': 'default'}])
        mock_adapter.put(requests_mock.ANY, json='record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default')
        result = self.iblox_conn.add_alias('testhost.unittest.example', 'testalias.unittest.example')
        self.assertTrue(isinstance(result, str))
        self.assertEquals(result, 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default')
        pass

    def test_delete_alias(self, mock_adapter):
        """ Test Infoblox.delete_alias method
        """
        mock_adapter.get(requests_mock.ANY, json=[{'_ref': 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default', 'ipv4addrs': [{'_ref': 'record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQuX2RlZmF1bHQuZXhhbXBsZS51bml0dGVzdC50ZXN0aG9zdC4xOTIuMTY4LjIuOC4:192.168.2.8/testhost.unittest.example/default', 'configure_for_dhcp': False, 'host': 'testhost.unittest.example', 'ipv4addr': '192.168.2.8'}], 'name': 'testhost.unittest.example', 'view': 'default'}])
        mock_adapter.delete(requests_mock.ANY, json='record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default')
        result = self.iblox_conn.delete_alias('testhost.unittest.example', 'testalias.unittest.example')
        self.assertTrue(isinstance(result, dict))
        self.assertEquals(result['_ref'], 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default')
        pass

    def test_delete_host(self, mock_adapter):
        """ Test Infoblox.delete_host method
        """
        mock_adapter.get(requests_mock.ANY, json=[{'_ref': 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default', 'ipv4addrs': [{'_ref': 'record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQuX2RlZmF1bHQuZXhhbXBsZS51bml0dGVzdC50ZXN0aG9zdC4xOTIuMTY4LjIuOC4:192.168.2.8/testhost.unittest.example/default', 'configure_for_dhcp': False, 'host': 'testhost.unittest.example', 'ipv4addr': '192.168.2.8'}], 'name': 'testhost.unittest.example', 'view': 'default'}])
        mock_adapter.delete(requests_mock.ANY, json='record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default')
        result = self.iblox_conn.get_host_by_name('testhost.unittest.example')[0]
        result = self.iblox_conn.delete(result['_ref'])
        self.assertTrue(isinstance(result, str))
        self.assertEquals(result, 'record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmV4YW1wbGUudW5pdHRlc3QudGVzdGhvc3Q:testhost.unittest.example/default')
        pass


if __name__ == '__main__':
    with warnings.catch_warnings(record=True):
        unittest.main(failfast=True)
