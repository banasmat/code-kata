# https://codingdojo.org/kata/BankOCR/

from functools import reduce

num_dict = {
    '0': [
        [' ', '_', ' '],
        ['|', ' ', '|'],
        ['|', '_', '|']
    ],
    '1': [
        [' ', ' ', ' '],
        [' ', ' ', '|'],
        [' ', ' ', '|']
    ],
    '2': [
        [' ', '_', ' '],
        [' ', '_', '|'],
        ['|', '_', ' ']
    ],
    '3': [
        [' ', '_', ' '],
        [' ', '_', '|'],
        [' ', '_', '|']
    ],
    '4': [
        [' ', ' ', ' '],
        ['|', '_', '|'],
        [' ', ' ', '|']
    ],
    '5': [
        [' ', '_', ' '],
        ['|', '_', ' '],
        [' ', '_', '|']
    ],
    '6': [
        [' ', '_', ' '],
        ['|', '_', ' '],
        ['|', '_', '|']
    ],
    '7': [
        [' ', '_', ' '],
        [' ', ' ', '|'],
        [' ', ' ', '|']
    ],
    '8': [
        [' ', '_', ' '],
        ['|', '_', '|'],
        ['|', '_', '|']
    ],
    '9': [
        [' ', '_', ' '],
        ['|', '_', '|'],
        [' ', '_', '|']
    ],
}


def decode_number_from_image(num_image: str) -> str:

    input_w = 27
    chars_len = 9
    char_h = 3
    char_w = 3

    char_matrix = [[[' ' for x in range(char_w)] for y in range(char_h)] for z in range(chars_len)]

    for i, line in enumerate(num_image.splitlines()[1:4]):
        char_num = 0
        for j, char in enumerate(line.strip('\n')[:input_w]):
            if j > 0 and j % char_w == 0:
                char_num += 1
                if char_num > chars_len:
                    char_num = 0
            char_matrix[char_num][i][j - char_w * char_num] = char

    result = []

    for char_set in char_matrix:
        for readable_num, num_image in num_dict.items():
            if char_set == num_image:
                result.append(readable_num)

    return ''.join(result)


def is_number_valid(number: str) -> bool:
    cheksum = 0
    i = 1
    for digit in reversed(number):
        cheksum += i * int(digit)
        i += 1

    print(cheksum)

    return cheksum % 11 == 0
