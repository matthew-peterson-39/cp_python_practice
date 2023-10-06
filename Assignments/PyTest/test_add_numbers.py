from add_numbers import add_two_numbers

def test_add_two_numbers():
    assert(add_two_numbers(1, 1) == 2)
    assert(add_two_numbers(5, 5) == 10)
    assert(add_two_numbers(0, 0) ==0)
    assert(add_two_numbers(-1, 0) == 5)