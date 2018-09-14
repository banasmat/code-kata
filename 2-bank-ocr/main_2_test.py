import pytest
from main_2 import *

test_data = [
    ('000000000', '''
 _  _  _  _  _  _  _  _  _     
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|
    
    '''),
    ('111111111', '''

  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
    
    '''),
    ('222222222', '''
 _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
    
    '''),
    ('333333333', '''
 _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
 _| _| _| _| _| _| _| _| _|
 
    '''),
    ('444444444', '''

|_||_||_||_||_||_||_||_||_|
  |  |  |  |  |  |  |  |  |
 
    '''),
    ('555555555', '''
 _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
 _| _| _| _| _| _| _| _| _|
 
    '''),
    ('666666666', '''
 _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
|_||_||_||_||_||_||_||_||_|
 
    '''),
    ('777777777', '''
 _  _  _  _  _  _  _  _  _ 
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
                         
    '''),
    ('888888888', '''
 _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
|_||_||_||_||_||_||_||_||_|
                         
    '''),
    ('999999999', '''
 _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
 _| _| _| _| _| _| _| _| _|
                         
    '''),
    ('123456789', '''
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
                         
    ''')
]


@pytest.mark.parametrize('expected, arg', test_data)
def test_decode_number_from_image(expected, arg):
    assert decode_number_from_image(arg) == expected
