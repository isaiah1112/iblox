# Changelog

## Version 1.5.1
 * Use params= instead of data= for get requests - [Merge Request #1](https://bitbucket.org/isaiah1112/infoblox/pull-requests/1/use-params-instead-of-data-for-get/diff)

## Version 1.5
 * Now compatible with Python 2.7.x and Python 3.5.x
 * Infoblox object can now be used with Python's 'with' statement

## Version 1.4.6
 * Fixed bugs in **add_alias** and **delete_alias** shortcuts
 * Renamed project to iblox (Infoblox as a module name was taken)
 * Releasing as Open Source

## Version 1.4.4
 * Fixed Bug if *disable_warnings* property is not available in requests module

## Version 1.4.3
 * Fixed Bugs with Call Function (Using POST data rather than URL arguments)
 * Disabling SSL warnings (from request module) if ssl verification is turned off

## Version 1.4.2
 * Fixed Bug in **_verify_** method when **_ref** argument doesn't exist
 * Fixed Bug with **_return_type** property when adding/deleting records

## Version 1.4
 * Added **delete_alias** shortcut for deleting aliases/CNAMES from a host
 * Added **add_host_ip** shortcut for adding IPv4 Addresses to a host
 * Added object **view** property for specifying default view to use when creating objects
 * Added kwarg modifiers for
  * _regex
  * _greaterthan
  * _lessthan
 * Added **call** method for accessing object functions via that WAPI (e.g. get_next_available_ip)
 * New Exception Classes

## Version 1.2
 * Added **__fix_plus__** method to convert kwargs that end in **_plus** to end in **+**
 * Added **add_alias** shortcut for adding aliases/CNAMES to a host

## Version 1.1
 * Module now caches session info when talking to the Infoblox WAPI
 * Rewritten add, delete, and modify commands
 * Changed kwarg **record** to **objtype**
 * Ensuring all data passed to Infoblox WAPI is converted to JSON
 * Renamed **find_host** with **get_host** for all methods

## Version 1.0
 * Created Infoblox object
 * Created add, get, delete, modify methods for Infoblox Python Module