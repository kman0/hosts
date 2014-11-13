__author__ = 'M'
import os
import platform


def get_hosts_path():
    """ Function to get hosts file path """
    if platform.system() == "Linux":
        return "/etc/hosts"
    elif platform.system() == "Windows":
        # use environment variable value when possible
        win_dir = os.environ.get('WINDIR', None)
        if win_dir:
            return win_dir + r"/system32/drivers/etc/hosts"
        else:
            return r"c:/windows/system32/drivers/etc/hosts"
    else:
        raise Exception('Unsupported Platform. Works in either Linux or Windows.')


def ensure_entry(hostname, address):
    """
    Ensure that the given hostname address resolution happens successfully by placing address hostname entry before
    any potentially conflicting entries.

    For example, consider hosts file:
        8.8.8.8 googledns
        127.0.0.1 googledns
        8.8.4.4 googledns

    >>>
        ensure_entry('googledns', '8.8.4.4')

    The above function call will write a new hosts file with following entries:
        8.8.4.4 googledns
        8.8.8.8 googledns
        127.0.0.1 googledns
        8.8.4.4 googledns

    This will not write to file unless necessary.
    It will not remove conflicting entries from host file for given hostname.

    :param hostname: string
    :param address:
    :return:
    """


def is_hosts_writable(file_path=get_hosts_path()):
    """ Function to determine whether user has write permissions to the hosts file """
    if os.access(file_path, os.W_OK):
        return True

