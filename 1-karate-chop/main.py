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


# errors: endless loop
# note: at one point failed only my additional test
# note: I'm not happy that I had to use i and max_iterations
def binary_chop_while_iteration(needle, haystack):
    count = len(haystack)

    if count == 0:
        return -1

    start = 0
    end = int(count/2)

    max_iterations = int(count / 2) + 1
    i = 0

    while start != end and i <= max_iterations:
        if needle == haystack[end]:
            start = end
        elif needle > haystack[end]:
            start = end
            end += int((count-end)/2)
        elif needle < haystack[end]:
            end = int((end-start)/2)
        i += 1

    if haystack[end] == needle:
        return end
    return -1
