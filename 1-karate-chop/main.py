# http://codekata.com/kata/kata02-karate-chop/


def iteration(needle, haystack):
    for i, num in enumerate(haystack):
        if num == needle:
            return i
    return -1


# errors:
# we don't have initial index when recurring
def binary_chop_recursive(_needle, _haystack):

    def __binary_chop(needle, haystack, i):
        count = len(haystack)

        if count == 0:
            return -1

        middle_point = int(count / 2)

        if needle == haystack[middle_point]:
            return i + middle_point
        elif needle > haystack[middle_point]:
            i += middle_point+1
            return __binary_chop(needle, haystack[middle_point + 1:], i)
        elif needle < haystack[middle_point]:
            return __binary_chop(needle, haystack[:middle_point], i)

    return __binary_chop(_needle, _haystack, 0)


# every time i have to look at test data and go step by step
# error: check if count is zero
# remembered from previous: modify the main index to keep track on whole index, not active chunk
def binary_chop_iteration(needle, haystack):
    count = len(haystack)

    if count == 0:
        return -1

    max_iterations = int(count / 2) + 1
    haystack_index = int(count / 2)

    for i in range(0, max_iterations):
        if needle == haystack[haystack_index]:
            return haystack_index
        elif needle > haystack[haystack_index]:
            haystack_index += int((count - haystack_index)/2)
        elif needle < haystack[haystack_index]:
            haystack_index = int(haystack_index/2)

    return -1

