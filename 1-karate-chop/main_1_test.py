import pytest
from main_1 import *
from random import randint

large_list_len = 2*40
large_list_num = randint(0, large_list_len-1)

test_data = [
  (-1, (3, [])),
  (-1, (3, [1])),
  (0, (1, [1])),
  #
  (0, (1, [1, 3, 5])),
  (1, (3, [1, 3, 5])),
  (2, (5, [1, 3, 5])),
  (-1, (0, [1, 3, 5])),
  (-1, (2, [1, 3, 5])),
  (-1, (4, [1, 3, 5])),
  (-1, (6, [1, 3, 5])),
  #
  (0, (1, [1, 3, 5, 7])),
  (1, (3, [1, 3, 5, 7])),
  (2, (5, [1, 3, 5, 7])),
  (3, (7, [1, 3, 5, 7])),
  (-1, (0, [1, 3, 5, 7])),
  (-1, (2, [1, 3, 5, 7])),
  (-1, (4, [1, 3, 5, 7])),
  (-1, (6, [1, 3, 5, 7])),
  (-1, (8, [1, 3, 5, 7])),
  (5, (6, [1, 2, 3, 4, 5, 6, 7])),
  (10, (10, range(0, 16))),
  (0, (0, range(0, 16))),
  (large_list_num, (large_list_num, range(0, large_list_len)))
]


@pytest.mark.parametrize('expected, args', test_data)
def test_binary_chop_recursive(expected, args):
    assert binary_chop_recursive(args[0], args[1]) == expected


@pytest.mark.parametrize('expected, args', test_data)
def test_binary_chop_iteration(expected, args):
    assert binary_chop_iteration(args[0], args[1]) == expected


@pytest.mark.parametrize('expected, args', test_data)
def test_binary_chop_while_iteration(expected, args):
    assert binary_chop_while_iteration(args[0], args[1]) == expected


@pytest.mark.parametrize('expected, args', test_data)
def test_binary_chop_dict_recursive(expected, args):
    assert binary_chop_dict_recursive(args[0], args[1]) == expected


@pytest.mark.parametrize('expected, args', test_data)
def test_binary_chop_multiple_results_with_one_or_zero_results(expected, args):
    if expected == -1:
        expected = tuple()
    else:
        expected = tuple([expected])
    assert binary_chop_multiple_results(args[0], args[1]) == expected


def test_binary_chop_multiple_results():
    assert binary_chop_multiple_results(3, [1, 2, 3, 3, 5, 6, 7]) == (2, 3)
    assert binary_chop_multiple_results(1, [1, 1, 1, 3, 5, 6, 7]) == (0, 1, 2)
