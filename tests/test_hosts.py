__author__ = 'M'

import hosts


def test_pass():
    pass


def test_platform():
    import platform
    if platform.system() == "Linux":
        assert hosts.get_hosts_path() == '/etc/hosts'