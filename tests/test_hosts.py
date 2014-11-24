import os

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


def test_file_is_file(monkeypatch):
    monkeypatch.setattr('os.path.isfile', lambda x: False)
    with pytest.raises(IOError) as exec_info:
        obj = hosts.Hosts(hosts_path='non-existing-file')
    assert 'File not found' in str(exec_info.value)


def test_file_is_writable(monkeypatch, tmpdir):
    raise pytest.skip("skip")
    monkeypatch.setattr('os.access', lambda x, y: False)

    temp_file = 'temp_hosts'
    p = tmpdir.mkdir("test_file_is_writable").join("temp_hosts")
    p.write("content")
    with pytest.raises(IOError) as exec_info:
        print(os.getcwd())
        obj = hosts.Hosts(hosts_path='test_file_is_writable/' + temp_file)
        obj.save()
    assert 'fail text - write new ---- File not found' in str(exec_info.value)

