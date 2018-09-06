import pytest
from main import *

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
]


@pytest.mark.parametrize('expected, args', test_data)
def test_binary_chop_recursive(expected, args):
    assert binary_chop_recursive(args[0], args[1]) == expected

@pytest.mark.parametrize('expected, args', test_data)
def test_binary_chop_iteration(expected, args):
    assert binary_chop_iteration(args[0], args[1]) == expected
