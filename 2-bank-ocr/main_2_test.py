import pytest
from main_2 import *


test_number_images = [
    (('000000000', ()), ('''
 _  _  _  _  _  _  _  _  _     
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
    
    ''', False)),
    (('111111111', ()), ('''

  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |

    ''', False)),
    (('222222222', ()), ('''
 _  _  _  _  _  _  _  _  _
 _| _| _| _| _| _| _| _| _|
|_ |_ |_ |_ |_ |_ |_ |_ |_

    ''', False)),
    (('333333333', ()), ('''
 _  _  _  _  _  _  _  _  _
 _| _| _| _| _| _| _| _| _|
 _| _| _| _| _| _| _| _| _|

    ''', False)),
    (('444444444', ()), ('''

|_||_||_||_||_||_||_||_||_|
  |  |  |  |  |  |  |  |  |

    ''', False)),
    (('555555555', ()), ('''
 _  _  _  _  _  _  _  _  _
|_ |_ |_ |_ |_ |_ |_ |_ |_
 _| _| _| _| _| _| _| _| _|

    ''', False)),
    (('666666666', ()), ('''
 _  _  _  _  _  _  _  _  _
|_ |_ |_ |_ |_ |_ |_ |_ |_
|_||_||_||_||_||_||_||_||_|

    ''', False)),
    (('777777777', ()), ('''
 _  _  _  _  _  _  _  _  _
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |

    ''', False)),
    (('888888888', ()), ('''
 _  _  _  _  _  _  _  _  _
|_||_||_||_||_||_||_||_||_|
|_||_||_||_||_||_||_||_||_|

    ''', False)),
    (('999999999', ()), ('''
 _  _  _  _  _  _  _  _  _
|_||_||_||_||_||_||_||_||_|
 _| _| _| _| _| _| _| _| _|

    ''', False)),
    (('123456789', ()), ('''
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

    ''', False)),
    (('000000051', ()), ('''
 _  _  _  _  _  _  _  _    
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |
    
    ''', True)),
    (('111111115 ERR', ()), ('''
                         _ 
  |  |  |  |  |  |  |  ||_
  |  |  |  |  |  |  |  | _|
    
    ''', True)),
    (('49006771? ILL', ()), ('''
    _  _  _  _  _  _     
|_||_|| || ||_   |  |  | _ 
  | _||_||_||_|  |  |  | _|
                      
    ''', True)),
    (('1234?678? ILL', ()), ('''
    _  _     _  _  _  _  _ 
  | _| _||_| _ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _ 
                         
    ''', True)),
    (('711111111', ()), ('''

  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |

    ''', True)),
    (('777777177', ()), ('''
 _  _  _  _  _  _  _  _  _
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |

    ''', True)),
    (('200800000', ()), ('''
 _  _  _  _  _  _  _  _  _
 _|| || || || || || || || |
|_ |_||_||_||_||_||_||_||_|

    ''', True)),
    (('333393333', ()), ('''
 _  _  _  _  _  _  _  _  _
 _| _| _| _| _| _| _| _| _|
 _| _| _| _| _| _| _| _| _|

    ''', True)),
    (('888888888 AMB', ('888886888', '888888880', '888888988')), ('''
 _  _  _  _  _  _  _  _  _
|_||_||_||_||_||_||_||_||_|
|_||_||_||_||_||_||_||_||_|

    ''', True)),
    (('555555555 AMB', ('555655555', '559555555')), ('''
 _  _  _  _  _  _  _  _  _
|_ |_ |_ |_ |_ |_ |_ |_ |_
 _| _| _| _| _| _| _| _| _|

    ''', True)),
    (('666666666 AMB', ('666566666', '686666666')), ('''
 _  _  _  _  _  _  _  _  _
|_ |_ |_ |_ |_ |_ |_ |_ |_
|_||_||_||_||_||_||_||_||_|

    ''', True)),
    (('999999999 AMB', ('899999999', '993999999', '999959999')), ('''
 _  _  _  _  _  _  _  _  _
|_||_||_||_||_||_||_||_||_|
 _| _| _| _| _| _| _| _| _|

    ''', True)),
    (('490067715 AMB', ('490067115', '490067719', '490867715')), ('''
    _  _  _  _  _  _     _
|_||_|| || ||_   |  |  ||_
  | _||_||_||_|  |  |  | _|

    ''', True)),
    (('123456789', ()), ('''
    _  _     _  _  _  _  _
 _| _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

    ''', True)),
    (('000000051', ()), ('''
 _     _  _  _  _  _  _
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |

    ''', True)),
    (('490867715', ()), ('''
    _  _  _  _  _  _     _
|_||_|| ||_||_   |  |  | _
  | _||_||_||_|  |  |  | _|

    ''', True)),
]

test_numbers_for_validation = [
    (True, '000000000'),
    (True, '000000051'),
    (True, '123456789'),
    (True, '345882865'),
    (False, '000000052'),
    (False, '111111111'),
    (False, '987654321'),
]

test_similar_numbers = [
    (('8',), (
        (' ', ' ', ' '),
        ('|', '_', '|'),
        ('|', '_', '|')
    )),
    (('0', '6', '9'), (
        (' ', '_', ' '),
        ('|', '_', '|'),
        ('|', '_', '|')
    )),
    (('7',), (
        (' ', ' ', ' '),
        (' ', ' ', '|'),
        (' ', ' ', '|')
    )),
    (('9', '6'), (
        (' ', '_', ' '),
        ('|', '_', ' '),
        (' ', '_', '|')
    )),
]


@pytest.mark.parametrize('expected, args', test_number_images)
def test_decode_number_from_image(expected, args):
    result = decode_number_from_image(args[0], validate=args[1])
    assert result[0] == expected[0]
    assert sorted(result[1]) == sorted(expected[1])


@pytest.mark.parametrize('expected, arg', test_numbers_for_validation)
def test_number_validation(expected, arg):
    assert is_number_valid(arg) == expected


@pytest.mark.parametrize('expected, arg', test_similar_numbers)
def test_finding_similar_numbers(expected, arg):
    assert find_similar_numbers(arg) == expected
