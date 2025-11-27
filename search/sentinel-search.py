def sentinel_search(arr, target):
    ultimo = arr[len(arr) - 1]
    arr[len(arr) - 1] = target
    i = 0
    while arr[i] != target:
        i += 1

    arr[len(arr) - 1] = ultimo

    if i < len(arr) - 1 or ultimo == target:
        return i

    return -1
