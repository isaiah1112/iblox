# [infoblox][]

## Overview

[infoblox][] is a wrapper for [Infoblox's WAPI](https://www.infoblox.com/).
It uses Python's request module to handle session caching and is very flexible.

## License

[infoblox][] is released under the [GNU Lesser General Public License v3.0][],
see the file LICENSE and LICENSE.lesser for the license text.

## Installation

Currently there is not an installation script. The most straightforward way to
get infoblox.py working is to:

  - ensure that **requests** and **json** modules are installed,

  - copy, move or link the file *infoblox.py*, located in the repository
    root directory, to your project directory

*I am working on getting the infoblox module into PyPi so hopefully these steps will soon go away*

## Contributing

Comments and enhancements are very welcome.

Report any issues or feature requests on the [BitBucket bug
tracker](https://bitbucket.org/isaiah1112/infoblox/issues?status=new&status=open). Please include a minimal
(not-) working example which reproduces the bug and, if appropriate, the
 traceback information.  Please do not request features already being worked
towards (see the TODO file).

Code contributions are encouraged: please feel free to [fork the
project](https://bitbucket.org/isaiah1112/infoblox) and submit pull requests.

## More information

- [Infoblox DDI](https://www.infoblox.com/)


[GNU Lesser General Public License v3.0]: http://choosealicense.com/licenses/lgpl-3.0/ "LGPL v3"

[infoblox]: https://bitbucket.org/isaiah1112/infoblox "Infoblox Module"