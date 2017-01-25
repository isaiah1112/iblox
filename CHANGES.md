# Changelog

## Release 1.5.3
 * Updating dictionaries [3d0558d](https://bitbucket.org/isaiah1112/infoblox/commits/3d0558dd1a331b1a8ec3d58be752e92490b528c0)
 * Code cleanup [d95b707](https://bitbucket.org/isaiah1112/infoblox/commits/d95b707c7770e828a667c085c73a12cd1e09c269)
 * Initializing dictionaries using dict function [0f06e6a](https://bitbucket.org/isaiah1112/infoblox/commits/0f06e6ab47dff693ad19e4548df23310e5802f59)
 * Actually building some documentation for the module... imagine that! [4dd9272](https://bitbucket.org/isaiah1112/infoblox/commits/4dd9272c592c2ad1a8763adf7965dbf54d2ea13b)
 * Automating testing with Tox [72e6373](https://bitbucket.org/isaiah1112/infoblox/commits/72e6373dc0a0160a88bc68b2d37a106e4ab457b1)
 * Updated requirements and added Documentation testing to tox [d08495f](https://bitbucket.org/isaiah1112/infoblox/commits/d08495f8cf6099d0c5f9dfa7792c2a194ffe46bb)
 * Tweaking documentation [dfd6262](https://bitbucket.org/isaiah1112/infoblox/commits/dfd6262177464ce2570e17fd59f4776d672b6e53)
 * Moving to built-in exception classes. [c5dd634](https://bitbucket.org/isaiah1112/infoblox/commits/c5dd634f4078606df385247cc22867343d0d0373)
 * Updated requirements! [55584b3](https://bitbucket.org/isaiah1112/infoblox/commits/55584b362097f4ec6250dc19ecc4f1509300bb3f)
 * Simplifying Sphinx config [9e47657](https://bitbucket.org/isaiah1112/infoblox/commits/9e47657c12417dc4abea63c236d418ea91c03912)
 * Going to host iblox documentation at pythonhosted.org [1125d53](https://bitbucket.org/isaiah1112/infoblox/commits/1125d5368e334895092bfed3259eb2f164796611)

## Release 1.5.2
 * Protecting internal calls so that Infoblox could be sublcassed if needed [150b89e](https://bitbucket.org/isaiah1112/infoblox/commits/150b89e38117f155131795d8b1164c1a002ef00b)

## Release 1.5.1
 * Use params= instead of data= for get requests - [Merge Request #1](https://bitbucket.org/isaiah1112/infoblox/pull-requests/1/use-params-instead-of-data-for-get/diff)

## Release 1.5
 * Now compatible with Python 2.7.x and Python 3.5.x
 * Infoblox class can now be used with Python's 'with' statement

## Release 1.4.6
 * Fixed bugs in **add_alias** and **delete_alias** shortcuts
 * Renamed project to iblox (Infoblox as a module name was taken)
 * Releasing as Open Source

## Release 1.4.4
 * Fixed Bug if *disable_warnings* property is not available in requests module

## Release 1.4.3
 * Fixed Bugs with Call Function (Using POST data rather than URL arguments)
 * Disabling SSL warnings (from request module) if ssl verification is turned off

## Release 1.4.2
 * Fixed Bug in **_verify_** method when **_ref** argument doesn't exist
 * Fixed Bug with **_return_type** property when adding/deleting records

## Release 1.4
 * Added **delete_alias** shortcut for deleting aliases/CNAMES from a host
 * Added **add_host_ip** shortcut for adding IPv4 Addresses to a host
 * Added **view** property for specifying default view to use when creating objects
 * Added kwarg modifiers for
  * _regex
  * _greaterthan
  * _lessthan
 * Added **call** method for accessing object functions via that WAPI (e.g. get_next_available_ip)
 * New Exception Classes

## Release 1.2
 * Added **__fix_plus__** method to convert kwargs that end in **_plus** to end in **+**
 * Added **add_alias** shortcut for adding aliases/CNAMES to a host

## Release 1.1
 * Module now caches session info when talking to the Infoblox WAPI
 * Rewritten add, delete, and modify commands
 * Changed kwarg **record** to **objtype**
 * Ensuring all data passed to Infoblox WAPI is converted to JSON
 * Renamed **find_host** with **get_host** for all methods

## Release 1.0
 * Created Infoblox class
 * Created add, get, delete, modify methods for Infoblox Python Module