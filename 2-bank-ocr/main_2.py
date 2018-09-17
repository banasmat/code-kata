# https://codingdojo.org/kata/BankOCR/

from functools import reduce

num_dict = {
    (
        (' ', '_', ' '),
        ('|', ' ', '|'),
        ('|', '_', '|')
    ): '0',
    (
        (' ', ' ', ' '),
        (' ', ' ', '|'),
        (' ', ' ', '|')
    ): '1',
    (
        (' ', '_', ' '),
        (' ', '_', '|'),
        ('|', '_', ' ')
    ): '2',
    (
        (' ', '_', ' '),
        (' ', '_', '|'),
        (' ', '_', '|')
    ): '3',
    (
        (' ', ' ', ' '),
        ('|', '_', '|'),
        (' ', ' ', '|')
    ): '4',
    (
        (' ', '_', ' '),
        ('|', '_', ' '),
        (' ', '_', '|')
    ): '5',
    (
        (' ', '_', ' '),
        ('|', '_', ' '),
        ('|', '_', '|')
    ): '6',
    (
        (' ', '_', ' '),
        (' ', ' ', '|'),
        (' ', ' ', '|')
    ): '7',
    (
        (' ', '_', ' '),
        ('|', '_', '|'),
        ('|', '_', '|')
    ): '8',
    (
        (' ', '_', ' '),
        ('|', '_', '|'),
        (' ', '_', '|')
    ): '9',
}


def decode_number_from_image(num_image: str, validate=True) -> tuple:

    input_w = 27
    chars_len = 9
    char_h = 3
    char_w = 3

    nums_matrix = [[[' ' for x in range(char_w)] for y in range(char_h)] for z in range(chars_len)]

    for row_i, line in enumerate(num_image.splitlines()[1:4]):
        num_i = 0
        for char_i, char in enumerate(line.strip('\n')[:input_w]):
            if char_i > 0 and char_i % char_w == 0:
                num_i += 1
                if num_i > chars_len:
                    num_i = 0
            nums_matrix[num_i][row_i][char_i - char_w * num_i] = char

    # Converting to tuples for faster dict search
    for num_i, num in enumerate(nums_matrix):
        for row_i, row in enumerate(nums_matrix[num_i]):
            nums_matrix[num_i][row_i] = tuple(nums_matrix[num_i][row_i])
        nums_matrix[num_i] = tuple(nums_matrix[num_i])

    result = []
    result_alternatives = []
    suffix = ''

    replacement_map = {}

    for i, num in enumerate(nums_matrix):
        try:
            result.append(num_dict[num])
        except KeyError:
            replacements = find_similar_numbers(num)
            if len(replacements) > 0:
                replacement_map[str(i)] = replacements
            result.append('?')
            suffix = ' ILL'

    if len(replacement_map) == 1:
        replacement_i, replacement_vals = replacement_map.popitem()

        replacement_i = int(replacement_i)
        replacement_vals = list(replacement_vals)

        initial_val = result[replacement_i]
        valid_alternatives = []

        for replacement_val in replacement_vals:
            result[replacement_i] = replacement_val
            if is_number_valid(result):
                valid_alternatives.append(''.join(result))
            else:
                replacement_vals.remove(replacement_val)

        if len(replacement_vals) == 1:
            result[replacement_i] = replacement_vals[0]
            suffix = ''
        elif len(replacement_vals) > 1:
            result[replacement_i] = initial_val
            suffix = ' AMB'
            result_alternatives = valid_alternatives

    if validate and suffix == '' and not is_number_valid(result):

        valid_alternatives = []

        for i, num in enumerate(result):
            similar_numbers = find_similar_numbers(nums_matrix[i], num)

            for similar_number in similar_numbers:
                _result = result.copy()
                _result[i] = similar_number
                if is_number_valid(''.join(_result)):
                    valid_alternatives.append(_result)

        len_valid_alternatives = len(valid_alternatives)
        if len_valid_alternatives == 0:
            suffix = ' ERR'
        elif len_valid_alternatives == 1:
            suffix = ''
            result = valid_alternatives.pop()
        else:
            valid_alternatives = list((map(lambda x: ''.join(x), valid_alternatives)))
            suffix = ' AMB'
            result_alternatives = valid_alternatives

    result = ''.join(result)

    return result + suffix, result_alternatives

# def __find_possible_replacements()


def is_number_valid(number: str) -> bool:
    checksum = 0
    i = 1
    for digit in reversed(number):
        checksum += i * int(digit)
        i += 1

    return checksum % 11 == 0


def find_similar_numbers(number_image, recognized_number=None) -> tuple:

    _num_dict = num_dict.copy()

    if recognized_number is not None:
        for img, num in _num_dict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            if num == recognized_number:
                del _num_dict[img]
                break

    results = []

    number_image = list(number_image)

    for row_i, row in enumerate(number_image):

        for char_i, char in enumerate(row):
            if char == ' ':
                possible_chars = ('|', '_')
            else:
                possible_chars = (' ',)
            initial_char = char
            for replacement_char in possible_chars:
                number_image[row_i] = __assign_tuple_value(number_image[row_i], char_i, replacement_char)

                try:
                    results.append(num_dict[tuple(number_image)])
                except KeyError:
                    continue

            number_image[row_i] = __assign_tuple_value(number_image[row_i], char_i, initial_char)

    return tuple(results)


def __assign_tuple_value(tup, val_i, val):
    tup = list(tup)
    tup[val_i] = val
    tup = tuple(tup)
    return tup
