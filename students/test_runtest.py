# -*- coding: utf-8 -*-

import runtests


def test_path_select():
    """Tests for 'path_select' function."""
    str1 = 'D:\\univ\\tests\\homework1'
    if not (runtests.path_select(str1)):
        raise AssertionError()
    str1 = 'D:\\univ\\tests'
    if not (runtests.path_select(str1)):
        raise AssertionError()


def test_file_select():
    """Tests for 'file_select' function."""
    str1 = 'D:\\univ\\tests\\homework1'
    if not (runtests.file_select(str1, 'test_file.py')):
        raise AssertionError()


if __name__ == '__main__':
    test_path_select()
    test_file_select()
