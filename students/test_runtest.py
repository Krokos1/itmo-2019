import os
import runtests


def test_path_select():
    """Tests for 'path_select' function."""
    assert runtests.path_select("D:\\univ\\tests\\homework1") == True
    assert runtests.path_select("D:\\univ\\tests") == True


def test_file_select():
    """Tests for 'file_select' function."""
    assert runtests.file_select("D:\\univ\\tests\\homework1", "test_file.py") == True
    assert runtests.file_select("D:\\univ\\tests\\homework1", "test_") == True


if __name__ == '__main__':
    test_path_select()
    test_file_select()
