# python3
from random import randint


def partition3(array, left, right):

    # print("-----i ")
    # print("partition left " + str(left) + " right " + str(right))
    pivot_index = left
    pivot_value = array[left]
    border_end = left
    repeat_count = 0

    # setting numbers to left and right of pivot values based on size comparing
    # skipping first since it is our pivot
    for i in range(left + 1, right + 1):
        # print("-----i " + str(i))
        # print(array[left:right+1])
        if array[i] == pivot_value:
            repeat_count = repeat_count + 1
            border_end += 1
            array[i], array[border_end] = array[border_end], array[i]
            pivot_index = pivot_index + 1
            # print("equal! pivotIndex " + str(pivot_index) + " repeat count " + str(repeat_count) + " border end " + str(border_end))
        elif array[i] < pivot_value:
            border_end += 1
            array[i], array[border_end] = array[border_end], array[i]
            array[border_end], array[pivot_index - repeat_count] = array[pivot_index - repeat_count], array[border_end]
            pivot_index = pivot_index + 1
            # print("less! pivotIndex " + str(pivot_index) + " repeat count " + str(repeat_count) + " border end " + str(border_end))

        else:
            # print("else! pivotIndex " + str(pivot_index) + " repeat count " + str(repeat_count) + " border end " + str(border_end))
            continue

    # m1 is based on end of border - times the number was repeated
    # ex [1, 2, 2, 2, 3, 4] pivot value = 2 so end border(m2) would be 3 and it
    # is REPEATED(after first instance) twice so 3 - 2 = 1 therefore m1 = 1 and m2 = 3
    m1 = border_end - repeat_count
    return m1, border_end


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
