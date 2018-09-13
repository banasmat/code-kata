# http://codekata.com/kata/kata02-karate-chop/


# errors:
# we don't have initial index when recurring
def binary_chop_recursive(needle, haystack, i=0):

    count = len(haystack)

    if count == 0:
        return -1

    middle_point = int(count / 2)

    if needle == haystack[middle_point]:
        return i + middle_point
    elif needle > haystack[middle_point]:
        i += middle_point+1
        return binary_chop_recursive(needle, haystack[middle_point + 1:], i)
    elif needle < haystack[middle_point]:
        return binary_chop_recursive(needle, haystack[:middle_point], i)


# note: every time i have to look at test data and go step by step
# error: check if count is zero
# remembered from previous: modify the main index to keep track on whole index, not active chunk
# note: had to correct after adding larger ranges to test
def binary_chop_iteration(needle, haystack):
    count = len(haystack) # 16

    if count == 0:
        return -1

    haystack_index = int(count / 2)
    max_iterations = haystack_index + 1
    prev_index = count

    for i in range(0, max_iterations):
        _prev_index = haystack_index

        if needle == haystack[haystack_index]:
            return haystack_index
        elif needle > haystack[haystack_index]:
            haystack_index += int((count - haystack_index)/2)
        elif needle < haystack[haystack_index]:
            haystack_index -= abs(int((prev_index - haystack_index)/2))
            if _prev_index == haystack_index:
                haystack_index -= 1
        prev_index = _prev_index

    return -1


# errors: endless loop
# note: at one point failed only my additional test
# note: I'm not happy that I had to use i and max_iterations
# note: had to correct after adding larger ranges to test
def binary_chop_while_iteration(needle, haystack):
    count = len(haystack)

    if count == 0:
        return -1

    start = 0
    end = count-1

    max_iterations = int(count / 2) + 1
    i = 0

    mid = end

    while needle != haystack[mid] and i <= max_iterations:
        mid = start + int((end - start) / 2)
        if needle > haystack[mid]:
            start = mid
        elif needle < haystack[mid]:
            end = mid

        i += 1

    if haystack[mid] == needle:
        return mid
    return -1


# In this approach there is no need to pass 'global' haystack index as it's assigned as a key to every value
# Also instead of dict it could be a list of tuples (global_index, value)
# Downside: have to iterate all values to build a dict at the beginning (memory error on very large range (0, 2**60)
# Errors: endless recursion (had to add `elif middle_point == first_index`)
def binary_chop_dict_recursive(needle, haystack):

    i = 0
    haystack_dict = {}
    for val in haystack:
        haystack_dict[str(i)] = val
        i += 1

    return _chop_dict_recursive(needle, haystack_dict)


def _chop_dict_recursive(needle, haystack: dict):
    count = len(haystack)

    if count == 0:
        return -1

    first_index = int(next(iter(haystack)))
    last_index = first_index + count

    middle_point = first_index + int((last_index-first_index) / 2)
    middle_point_str = str(middle_point)

    chunk_mid = int(count/2)

    if needle == haystack[middle_point_str]:
        return middle_point
    elif middle_point == first_index:
        return -1
    elif needle > haystack[middle_point_str]:
        return _chop_dict_recursive(needle, dict(list(haystack.items())[chunk_mid+1:]))
    elif needle < haystack[middle_point_str]:
        return _chop_dict_recursive(needle, dict(list(haystack.items())[:chunk_mid]))


