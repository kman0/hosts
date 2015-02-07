from collections import defaultdict

__author__ = 'M'
import os
import platform


def get_hosts_path():
    """
    Function to get hosts file path
    :return: str, points to hosts file.

    :raises: Exception('Unsupported Platform')

    """
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
    pass


class Hosts(object):
    """

    """

    def __init__(self, hosts_path=None):
        """
        :param hosts_path: Location of hosts file
        """
        self._ips = defaultdict()
        if not hosts_path:
            self.hosts_path = get_hosts_path()
        else:
            self.hosts_path = hosts_path
        self._reload()

    def _reload(self):
        """
        Reloads the hosts file from disk. Un saved changes are lost!
        :return:
        """
        if not os.path.isfile(self.hosts_path):
            raise IOError('File not found: %s' % self.hosts_path)

        # load hosts file with comments and strip
        self._raw_lines = [line.strip() for line in open(self.hosts_path).readlines()]

        # weed out comments
        self._lines = {sno: line for sno, line in enumerate(self._raw_lines) if not line.startswith('#') and line != ''}

    def _new_lines_with_comments(self):
        """
        Multiplex comment lines with processed lines
        :return:
        """
        #todo: code this part! :D
        return [self._lines[sno] for sno in self._lines]

    def save(self):
        """ Writes the changes to the hosts file"""
        if not os.access(self.hosts_path, os.W_OK):
            raise IOError('Unable to write to file: %s' % self.hosts_path)
        contents = '\n'.join(self._new_lines_with_comments())
        with open(self.hosts_path, 'w') as fpw:
            fpw.writelines(contents + '\n')


