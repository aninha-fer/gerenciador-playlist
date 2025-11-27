import copy


def insertion_sort(arr_arg):
    """Return a sorted copy of `arr_arg` using insertion sort.

    Uses a deep copy to mirror JavaScript's `structuredClone` behavior.
    """
    array = copy.deepcopy(arr_arg)

    for i in range(len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = value

    return array
