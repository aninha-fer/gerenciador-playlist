def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (right + left) // 2

        if arr[middle] == target:
            return middle

        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
