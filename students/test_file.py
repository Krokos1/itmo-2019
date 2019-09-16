# -*- coding: utf-8 -*-

import funcs1


def test_sum():
    """Tests for my_sum funtion."""
    assert funcs1.my_sum(1, 2) == 3
    assert funcs1.my_sum(5, 2) == 7
    assert funcs1.my_sum(0, 0) == 0


def test_mult():
    """Tests for my_mult funtion."""
    assert funcs1.my_mult(2, 2) == 4
    assert funcs1.my_mult(1, 1) == 1


def test_div():
    """Tests for my_div funtion."""
    assert funcs1.my_div(1, 1) == 1
    assert funcs1.my_div(6, 3) == 2
    assert funcs1.my_div(8, 1) == 8


if __name__ == '__main__':
    test_div()
    test_mult()
    test_sum()
