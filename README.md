hosts [![Build Status](https://travis-ci.org/manojklm/hosts.svg?branch=master)](https://travis-ci.org/manojklm/hosts)
=====

Python wrapper to manage hosts file. Supports python 3.2, 3.3 and 3.4.

Usage:

    >>> from hosts import Hosts
    >>> hosts_obj = Hosts() # load hosts file automatically for windows and linux
    >>> hosts_obj = Hosts(hosts_file='/ect/hosts') # point to specific hosts file

Save:

    >>> hosts_obj.save()    # writes data back to hosts file


Changelog:

    0.1 - Reads, removes comments and writes hosts file