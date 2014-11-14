__author__ = 'M'

import hosts
import pytest


def test_platform_linux(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Linux')
    assert hosts.get_hosts_path() == '/etc/hosts'


def test_platform_windows_windir(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Windows')
    monkeypatch.setattr('os.environ.get', lambda x, y: 'R:\\Windows')
    assert hosts.get_hosts_path() == 'R:\\Windows/system32/drivers/etc/hosts'


def test_platform_windows_no_env(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Windows')
    monkeypatch.setattr('os.environ.get', lambda x, y: None)
    assert hosts.get_hosts_path() == 'c:/windows/system32/drivers/etc/hosts'


def test_platform_unexpected(monkeypatch):
    monkeypatch.setattr('platform.system', lambda: 'Brand New')
    with pytest.raises(Exception) as exec_info:
        hosts.get_hosts_path()
    assert 'Unsupported Platform' in str(exec_info.value)


def test_file_writable(monkeypatch):
    monkeypatch.setattr('os.access')
    obj = hosts.Hosts()
