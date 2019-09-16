import funcs1


def test_sum():
    """Tests for my_sum funtion."""
    assert funcs1.my_sum(1, 2) == 3
    assert round(funcs1.my_sum(2.1, 4.2), 2) == 6.3


def test_mult():
    """Tests for my_mult funtion."""
    assert funcs1.my_mult(2, 2) == 4
    assert funcs1.my_mult(1, 1) == 1
    assert funcs1.my_mult(19.7, 0) == 0
    assert funcs1.my_mult(-6, -4) == 24
    assert funcs1.my_mult(6, -4) == -24
    assert funcs1.my_mult(6, 4) == 24


def test_div():
    """Tests for my_div funtion."""
    assert funcs1.my_div(1, 1) == 1
    assert funcs1.my_div(5, 2) == 2.5
    assert funcs1.my_div(6, 2) == 3.0
    try:
        funcs1.my_div(1, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False 


if __name__ == '__main__':
    test_div()
    test_mult()
    test_sum()
