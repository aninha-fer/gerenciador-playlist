import copy


def bubble_sort(array_arg):
    """Return a sorted copy of `array_arg` using bubble sort.

    Uses a deep copy to mirror JavaScript's `structuredClone` behavior.
    """
    arr = copy.deepcopy(array_arg)

    # Loop until no swaps are made
    foi_modificado = True
    while foi_modificado:
        foi_modificado = False
        for i in range(len(arr) - 1):
            numero_atual = arr[i]
            proximo_numero = arr[i + 1]

            if numero_atual > proximo_numero:
                foi_modificado = True
                # swap
                arr[i], arr[i + 1] = proximo_numero, numero_atual

    return arr
