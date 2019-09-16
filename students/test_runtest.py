# -*- coding: utf-8 -*-

import os
import runtests


def test_path_select():
    """Tests for 'path_select' function."""
    if not (runtests.path_select('D:\\univ\\tests\\homework1')):
        raise AssertionError()
    if not (runtests.path_select('D:\\univ\\tests')):
        raise AssertionError()


def test_file_select():
    """Tests for 'file_select' function."""

    if not (runtests.file_select('D:\\univ\\tests\\homework1', 'test_file.py')):
        raise AssertionError()


if __name__ == '__main__':
    test_path_select()
    test_file_select()
