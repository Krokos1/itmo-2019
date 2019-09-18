# -*- coding: utf-8 -*-

"""Tests for framework."""
import importlib
import os

import runtests


def test_get_dirname():
    """Tests for 'get_dirname' function."""
    assert runtests.get_dirname('') == os.getcwd()


def test_path_select():
    """Tests for 'path_select' function."""
    str1 = os.getcwd()
    if not (runtests.path_select(str1)):
        raise AssertionError()


def test_file_select():
    """Tests for 'file_select' function."""
    str1 = os.getcwd()
    if not (runtests.file_select(str1, 'test_file.py')):
        raise AssertionError()


def test_prints():
    """Tests for 'prints' function."""
    func_list = importlib.import_module('test_file')
    file1 = 'test_file.py'
    module1 = 'funcs1'
    if not (runtests.prints(module1, func_list, file1)):
        raise AssertionError()


if __name__ == '__main__':
    test_path_select()
    test_file_select()
    test_get_dirname()
    test_prints()
